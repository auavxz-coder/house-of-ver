import hmac
import json
import urllib.error
import urllib.parse
import urllib.request
import streamlit as st

st.set_page_config(page_title="HOUSE OF VÈR | Private Orders",page_icon="✦",layout="wide")
st.markdown("""<style>
.stApp{background:#fff5e9;color:#493425}
h1,h2,h3{color:#92682c!important;font-family:Georgia,serif}
.stButton button{background:#946d36;color:white;border:0}
</style>""",unsafe_allow_html=True)

def secret(name):
    try:
        return str(st.secrets.get(name,"")).strip()
    except Exception:
        return ""

def query(method, route, payload=None):
    base=secret("SUPABASE_URL").rstrip("/")
    key=secret("SUPABASE_SERVICE_ROLE_KEY")
    if not base.startswith("https://") or not key:
        raise RuntimeError("Database credentials not configured")
    headers={"apikey":key,"Authorization":"Bearer "+key,
             "Content-Type":"application/json","Prefer":"return=representation"}
    req=urllib.request.Request(base+"/rest/v1/"+route,
            data=json.dumps(payload).encode() if payload is not None else None,
            headers=headers,method=method)
    with urllib.request.urlopen(req,timeout=12) as response:
        return json.loads(response.read().decode() or "[]")

st.title("HOUSE OF VÈR")
st.caption("PRIVATE ORDER MANAGEMENT • ADMIN ONLY")
if not secret("ADMIN_PASSWORD"):
    st.error("Admin access is not configured. Set ADMIN_PASSWORD in this app's Streamlit Secrets before use.")
    st.stop()

if not st.session_state.get("admin_logged_in",False):
    with st.form("login"):
        password=st.text_input("Admin password",type="password")
        submit=st.form_submit_button("Sign in")
    if submit:
        if hmac.compare_digest(password,secret("ADMIN_PASSWORD")):
            st.session_state.admin_logged_in=True
            st.rerun()
        else:
            st.error("Incorrect password")
    st.stop()

if st.button("Sign out"):
    st.session_state.admin_logged_in=False
    st.rerun()

try:
    orders=query("GET","orders?select=*&order=created_at.desc&limit=200")
except urllib.error.HTTPError as exc:
    status = exc.code
    if status in (401, 403):
        st.error("Supabase rejected access (HTTP " + str(status) + "). Check the admin app's private API key and database permissions.")
    elif status == 404:
        st.error("Orders API endpoint not found (HTTP 404). Check that the orders table is available through the Data API.")
    else:
        st.error("Supabase returned HTTP " + str(status) + ". Check API settings and table access.")
    st.stop()
except RuntimeError:
    st.error("Missing Supabase connection settings in this admin app's Secrets.")
    st.stop()
except Exception:
    st.error("Unable to connect to Supabase. Check the project URL and service availability.")
    st.stop()

col1,col2,col3=st.columns(3)
col1.metric("Recent orders",len(orders))
col2.metric("Awaiting payment",sum(o.get("payment_status")=="awaiting_verification" for o in orders))
col3.metric("To prepare",sum(o.get("fulfillment_status")=="new" for o in orders))
st.info("Payment statuses are updated manually. Verify transactions in Ziina before marking an order paid.")
for order in orders:
    oid=str(order.get("order_id",""))
    with st.expander(f'{oid} | AED {order.get("total")} | {order.get("payment_status")}'):
        st.write("Customer:",order.get("customer_name"))
        st.write("Email:",order.get("email"))
        st.write("Instagram:",order.get("instagram") or "Not provided")
        st.write("Phone:",order.get("phone"))
        st.write("Delivery:",order.get("emirate"),"—",order.get("area"))
        st.write("Address:",order.get("address"))
        st.write("Quantity:",order.get("quantity"),"| Delivery fee: AED",order.get("delivery_fee"))
        pay_values=["awaiting_verification","paid_verified","failed","refunded"]
        fulfillment=["new","preparing","shipped","delivered","cancelled"]
        with st.form("update_"+oid):
            payment=st.selectbox("Payment",pay_values,index=pay_values.index(order.get("payment_status")) if order.get("payment_status") in pay_values else 0)
            status=st.selectbox("Fulfillment",fulfillment,index=fulfillment.index(order.get("fulfillment_status")) if order.get("fulfillment_status") in fulfillment else 0)
            if st.form_submit_button("Save changes"):
                try:
                    query("PATCH","orders?order_id=eq."+urllib.parse.quote(oid,safe=""),
                          {"payment_status":payment,"fulfillment_status":status})
                    st.success("Updated")
                    st.rerun()
                except Exception:
                    st.error("Unable to update order")
if not orders:
    st.write("No orders have been saved yet. The storefront order-submission connection is not active.")
