import json
import urllib.parse
import re
import uuid
import urllib.request
import streamlit as st

def save_order(name, phone, email, instagram, address, emirate, area, quantity, price, delivery, is_gift=False, gift_message="", customer_token=None):
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
    gift_message = gift_message.strip()
    if len(gift_message) > 300:
        raise ValueError("Gift message must be 300 characters or less.")
    record = {'order_id': order_id, 'customer_name': name, 'phone': phone, 'email': email.lower(),
        'instagram': instagram.lstrip('@'), 'address': address, 'emirate': emirate, 'area': area,
        'quantity': quantity, 'subtotal': price*quantity, 'delivery_fee': delivery,
        'total': price*quantity+delivery, 'payment_status': 'awaiting_verification',
        'fulfillment_status': 'new'}
    if customer_token:
        # Verify Supabase-issued access token server-side before associating an order.
        public_key=str(st.secrets["SUPABASE_PUBLISHABLE_KEY"]).strip()
        verify_headers={"apikey":public_key,"Authorization":"Bearer "+customer_token}
        verify_req=urllib.request.Request(url+"/auth/v1/user",headers=verify_headers)
        with urllib.request.urlopen(verify_req,timeout=12) as response:
            user=json.loads(response.read().decode())
        if not user.get("id") or user.get("email","").lower()!=email.lower():
            raise ValueError("Signed-in email must match the order email")
        record["user_id"]=user["id"]
    if is_gift:
        record['is_gift'] = True
        record['gift_message'] = gift_message
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

def choose_payment(order_id, method, expected_total):
    """Atomically lock one payment method to one order."""
    if method not in ("ziina", "cod"):
        raise ValueError("Unsupported payment method")
    import urllib.parse
    base = str(st.secrets["SUPABASE_URL"]).strip().rstrip("/")
    key = str(st.secrets["SUPABASE_SERVICE_ROLE_KEY"]).strip()
    headers = {"apikey": key, "Content-Type": "application/json", "Prefer": "return=representation"}
    if not key.startswith("sb_secret_"):
        headers["Authorization"] = "Bearer " + key
    route = "/rest/v1/orders?order_id=eq." + urllib.parse.quote(order_id, safe="")
    with urllib.request.urlopen(urllib.request.Request(base+route, headers=headers), timeout=12) as response:
        rows = json.loads(response.read().decode())
    if len(rows) != 1:
        raise RuntimeError("Order not found")
    row = rows[0]
    original = int(row["subtotal"]) + int(row["delivery_fee"])
    if original != expected_total:
        raise ValueError("Order amount mismatch")
    if row["payment_status"] != "awaiting_verification":
        raise ValueError("Payment method already selected for this order")
    total = original + (5 if method == "cod" else 0)
    status = {"ziina": "ziina_pending", "cod": "cod_pending"}[method]
    locked_route = route + "&payment_status=eq.awaiting_verification"
    request = urllib.request.Request(base+locked_route,
        data=json.dumps({"total":total, "payment_status":status}).encode(),
        headers=headers, method="PATCH")
    with urllib.request.urlopen(request, timeout=12) as response:
        result = json.loads(response.read().decode())
    if len(result) != 1 or int(result[0]["total"]) != total:
        raise ValueError("Payment method has already been selected")
    return total

def payment_state(order_id):
    """Read authoritative payment method state, not browser session state."""
    import urllib.parse
    url = str(st.secrets["SUPABASE_URL"]).strip().rstrip("/")
    key = str(st.secrets["SUPABASE_SERVICE_ROLE_KEY"]).strip()
    headers = {"apikey": key}
    if not key.startswith("sb_secret_"):
        headers["Authorization"] = "Bearer " + key
    route = "/rest/v1/orders?select=payment_status,total&order_id=eq." + urllib.parse.quote(order_id, safe="")
    with urllib.request.urlopen(urllib.request.Request(url+route,headers=headers),timeout=12) as response:
        rows = json.loads(response.read().decode())
    if len(rows) != 1:
        raise RuntimeError("Order not found")
    return rows[0]

def lookup_order_status(order_id, email, phone):
    """Only return limited status information after matching three order credentials."""
    import urllib.parse
    order_id = order_id.strip().upper()
    email = email.strip().lower()
    phone = phone.strip()
    if not re.fullmatch(r"VER-[A-F0-9]{12}", order_id):
        return None
    if not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email):
        return None
    if not re.fullmatch(r"[+0-9() -]{7,30}", phone):
        return None
    base = str(st.secrets["SUPABASE_URL"]).strip().rstrip("/")
    key = str(st.secrets["SUPABASE_SERVICE_ROLE_KEY"]).strip()
    headers = {"apikey": key}
    if not key.startswith("sb_secret_"):
        headers["Authorization"] = "Bearer " + key
    params = urllib.parse.urlencode({
        "select":"order_id,fulfillment_status,payment_status",
        "order_id":"eq."+order_id,
        "email":"eq."+email,
        "phone":"eq."+phone,
        "limit":"1"
    })
    request = urllib.request.Request(base+"/rest/v1/orders?"+params,headers=headers)
    with urllib.request.urlopen(request,timeout=12) as response:
        rows=json.loads(response.read().decode())
    return rows[0] if rows else None
