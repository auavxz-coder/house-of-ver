import json
import urllib.request
import urllib.error
import streamlit as st

def _settings():
    url=str(st.secrets["SUPABASE_URL"]).strip().rstrip("/")
    key=str(st.secrets["SUPABASE_PUBLISHABLE_KEY"]).strip()
    if not url.startswith("https://") or not key:
        raise RuntimeError("Customer accounts are not configured")
    return url,key

def _request(path, method="GET", body=None, token=None):
    url,key=_settings()
    headers={"apikey":key,"Content-Type":"application/json"}
    if token:
        headers["Authorization"]="Bearer "+token
    req=urllib.request.Request(url+path,method=method,headers=headers,
        data=json.dumps(body).encode() if body is not None else None)
    try:
        with urllib.request.urlopen(req,timeout=12) as response:
            return json.loads(response.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        if e.code in (400,401,403,422):
            raise ValueError("Account request could not be completed. Check your details or verify your email.")
        raise RuntimeError("Account service temporarily unavailable")

def signup(email,password):
    return _request("/auth/v1/signup","POST",{"email":email.strip().lower(),"password":password})

def signin(email,password):
    return _request("/auth/v1/token?grant_type=password","POST",{"email":email.strip().lower(),"password":password})

def refresh(refresh_token):
    return _request("/auth/v1/token?grant_type=refresh_token","POST",{"refresh_token":refresh_token})

def current_user(token):
    return _request("/auth/v1/user",token=token)

def recover(email):
    return _request("/auth/v1/recover","POST",{"email":email.strip().lower()})

def get_profile(token):
    rows=_request("/rest/v1/customer_profiles?select=cart_qty,full_name,phone,instagram,address,emirate,area&limit=1",token=token)
    return rows[0] if rows else {}

def save_profile(token, user_id, **fields):
    allowed={"cart_qty","full_name","phone","instagram","address","emirate","area"}
    payload={k:v for k,v in fields.items() if k in allowed}
    payload["user_id"]=user_id
    url,key=_settings()
    headers={"apikey":key,"Authorization":"Bearer "+token,"Content-Type":"application/json",
             "Prefer":"resolution=merge-duplicates,return=representation"}
    req=urllib.request.Request(url+"/rest/v1/customer_profiles",method="POST",
        headers=headers,data=json.dumps(payload).encode())
    try:
        with urllib.request.urlopen(req,timeout=12) as response:
            return json.loads(response.read().decode() or "[]")
    except urllib.error.HTTPError:
        raise RuntimeError("Could not save account details")

def my_orders(token):
    return _request("/rest/v1/rpc/my_order_summaries","POST",{},token=token)

def my_order_details(token, order_id):
    """Only the signed-in owner can retrieve order details through a scoped RPC."""
    return _request("/rest/v1/rpc/my_order_details", "POST", {"requested_order_id":order_id},token=token)
