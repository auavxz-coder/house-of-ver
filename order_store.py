import json
import urllib.parse
import re
import uuid
import urllib.request
import streamlit as st

def save_order(name, phone, email, instagram, address, emirate, area, quantity, price, delivery):
    name, phone, email, instagram, address = [x.strip() for x in (name, phone, email, instagram, address)]
    if not all([name, phone, email, instagram, address]):
        raise ValueError('Complete all required fields.')
    if not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+', email):
        raise ValueError('Enter a valid email address.')
    if not re.fullmatch(r'[+0-9() -]{7,30}', phone):
        raise ValueError('Enter a valid phone number.')
    if not re.fullmatch(r'[A-Za-z0-9._]{1,30}', instagram.lstrip('@')):
        raise ValueError('Enter a valid Instagram username.')
    if not 1 <= quantity <= 20:
        raise ValueError('Invalid quantity.')
    try:
        url = str(st.secrets['SUPABASE_URL']).strip().rstrip('/')
        key = str(st.secrets['SUPABASE_SERVICE_ROLE_KEY']).strip()
    except (KeyError, FileNotFoundError):
        raise RuntimeError('Order storage has not been configured.')
    if not url.startswith('https://') or not key:
        raise RuntimeError('Invalid database configuration.')
    order_id = 'VER-' + uuid.uuid4().hex[:12].upper()
    record = {'order_id': order_id, 'customer_name': name, 'phone': phone, 'email': email.lower(),
        'instagram': instagram.lstrip('@'), 'address': address, 'emirate': emirate, 'area': area,
        'quantity': quantity, 'subtotal': price*quantity, 'delivery_fee': delivery,
        'total': price*quantity+delivery, 'payment_status': 'awaiting_verification',
        'fulfillment_status': 'new'}
    headers = {'apikey': key, 'Content-Type': 'application/json', 'Prefer': 'return=representation'}
    if not key.startswith('sb_secret_'):
        headers['Authorization'] = 'Bearer ' + key
    request = urllib.request.Request(url + '/rest/v1/orders', data=json.dumps(record).encode(), headers=headers, method='POST')
    with urllib.request.urlopen(request, timeout=12) as response:
        saved = json.loads(response.read().decode())
    if not saved or saved[0].get('order_id') != order_id:
        raise RuntimeError('Order save could not be confirmed.')
    return order_id

def upload_payment_proof(order_id, file):
    """Upload a private receipt; never interpret a screenshot as confirmed payment."""
    if not file:
        raise ValueError("Upload your Ziina payment screenshot.")
    mime = file.type
    if mime not in ("image/png", "image/jpeg"):
        raise ValueError("Only PNG or JPEG screenshots are allowed.")
    data = file.getvalue()
    if len(data) > 5 * 1024 * 1024:
        raise ValueError("Screenshot must be smaller than 5 MB.")
    try:
        url = str(st.secrets["SUPABASE_URL"]).strip().rstrip("/")
        key = str(st.secrets["SUPABASE_SERVICE_ROLE_KEY"]).strip()
    except (KeyError, FileNotFoundError):
        raise RuntimeError("Receipt storage is not configured.")
    suffix = "png" if mime == "image/png" else "jpg"
    object_path = order_id + "/" + uuid.uuid4().hex + "." + suffix
    headers = {"apikey": key, "Content-Type": mime, "x-upsert": "false"}
    if not key.startswith("sb_secret_"):
        headers["Authorization"] = "Bearer " + key
    storage_url = url + "/storage/v1/object/payment-proofs/" + object_path
    request = urllib.request.Request(storage_url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(request, timeout=15) as response:
        response.read()
    update_headers = {"apikey": key, "Content-Type": "application/json", "Prefer": "return=representation"}
    if not key.startswith("sb_secret_"):
        update_headers["Authorization"] = "Bearer " + key
    update_url = url + "/rest/v1/orders?order_id=eq." + urllib.parse.quote(order_id, safe="")
    update = urllib.request.Request(update_url,
        data=json.dumps({"payment_proof_path": object_path}).encode(),
        headers=update_headers, method="PATCH")
    with urllib.request.urlopen(update, timeout=12) as response:
        saved = json.loads(response.read().decode())
    if not saved or saved[0].get("payment_proof_path") != object_path:
        raise RuntimeError("Receipt association could not be confirmed.")
    return object_path
