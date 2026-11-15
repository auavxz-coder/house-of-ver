import json
import re
import uuid
import urllib.request
import streamlit as st

def save_order(name, phone, email, instagram, address, emirate, area, quantity, price, delivery):
    name, phone, email, instagram, address = [x.strip() for x in (name, phone, email, instagram, address)]
    if not all([name, phone, email, address]):
        raise ValueError('Complete all required fields.')
    if not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+', email):
        raise ValueError('Enter a valid email address.')
    if not re.fullmatch(r'[+0-9() -]{7,30}', phone):
        raise ValueError('Enter a valid phone number.')
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
