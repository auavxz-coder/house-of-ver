import base64
from pathlib import Path
import streamlit as st

st.set_page_config(page_title='HOUSE OF VÈR | The Essence of Presence', page_icon='✦', layout='wide', initial_sidebar_state='collapsed')
BASE=Path(__file__).parent

def img_data(name):
    p=BASE/name
    mime='image/jpeg' if p.suffix.lower() in ('.jpg','.jpeg') else 'image/png'
    return f'data:{mime};base64,{base64.b64encode(p.read_bytes()).decode()}'

if 'lang' not in st.session_state: st.session_state.lang='English'
ar=st.session_state.lang=='العربية'
copy={
 'nav':('THE ESSENCE OF PRESENCE','جوهر الحضور'),
 'intro':('A presence that lingers.','حضور يترك أثره.'),
 'desc':('A signature fragrance from HOUSE OF VÈR. Discover VÈR, a statement of quiet confidence.','عطر مميز من هاوس أوف ڤير. اكتشفي ڤير، تعبير عن الثقة الهادئة.'),
 'product':('VÈR — EAU DE PARFUM','ڤير — عطر'),
 'size':('100 ml · UAE delivery','١٠٠ مل · التوصيل داخل الإمارات'),
 'order':('ORDER VIA INSTAGRAM','اطلب عبر إنستغرام'),
 'profile':('Visit our Instagram profile','زيارة حسابنا على إنستغرام'),
 'about_title':('THE HOUSE','عن الدار'),
 'about':('HOUSE OF VÈR is built around the essence of presence: a fragrance made to be remembered.','تتمحور هوية هاوس أوف ڤير حول جوهر الحضور، عطر يبقى في الذاكرة.'),
 'delivery_title':('UAE DELIVERY','التوصيل داخل الإمارات'),
 'delivery':('Orders are arranged by Instagram direct message. Delivery availability, timing and fees are confirmed before your order is finalized.','يتم تنسيق الطلبات عبر رسائل إنستغرام. نؤكد توفر التوصيل وموعده ورسومه قبل تأكيد الطلب.'),
 'notice':('Orders are placed through Instagram messages. No card payments are taken on this website.','الطلبات تتم عبر رسائل إنستغرام، ولا يتم تحصيل أي مدفوعات بالبطاقة عبر هذا الموقع.'),
 'contact':('STAY IN TOUCH','تواصلي معنا'),
}
def t(k): return copy[k][1 if ar else 0]
art=img_data('brand_art.png'); perfume=img_data('perfume.jpg')
notes_image = (BASE / "notes.jpg.png").exists()
st.markdown('''<style>
@import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Cormorant+Garamond:wght@400;500;600&family=DM+Sans:wght@400;500&display=swap');
:root{--gold:#a8782c;--ink:#463121;--cream:#fff4e6}
.stApp{background:#fff5e9;color:var(--ink)}
.block-container{max-width:1150px;padding-top:1.2rem;padding-bottom:3rem}
header[data-testid="stHeader"]{background:transparent}
#MainMenu,footer{visibility:hidden}
.brand-shell{border:double 5px #b8893b;background:#fff2e4;position:relative;overflow:hidden;min-height:410px;padding:35px 28px 42px;text-align:center;box-shadow:0 12px 35px #77532c16}
.brand-shell:before{content:'';position:absolute;inset:0;background-image:url('ART');background-position:center;background-size:100% 100%;opacity:.23;pointer-events:none}
.brand-shell>*{position:relative}
.sun{font-size:4rem;color:#b88a40;line-height:1.3}.brand{font-family:'Cormorant Garamond',serif;font-size:clamp(2.5rem,7vw,5.2rem);font-weight:500;letter-spacing:.055em;color:#986821;margin:0}.tag{font-family:'Cormorant Garamond',serif;letter-spacing:.25em;color:#9a722e;font-size:clamp(.85rem,2vw,1.2rem)}
.section-title{font-family:'Cormorant Garamond','Amiri',serif;font-size:clamp(2rem,4vw,3.5rem);color:#8d6226;text-align:center;margin:38px 0 10px}.copy{font-family:'Cormorant Garamond','Amiri',serif;font-size:clamp(1.3rem,2.5vw,1.7rem);text-align:center;max-width:680px;margin:0 auto 18px;line-height:1.65}.muted{color:#826d57;text-align:center;font-size:.95rem}.goldline{width:75px;border-top:1px solid #ac813a;margin:20px auto}.bottle{max-width:390px;margin:28px auto 12px}.bottle img{width:100%;border-radius:3px;box-shadow:0 15px 38px #4e30222b}.price{font-family:'Cormorant Garamond',serif;font-size:2.2rem;text-align:center;color:#8d6226}
.order{display:block;max-width:340px;margin:20px auto 10px;background:#946d36;color:#fff9f1!important;text-decoration:none!important;text-align:center;padding:17px 20px;letter-spacing:.12em;font-family:'DM Sans','Amiri',sans-serif;font-size:.85rem;transition:background .2s}.order:hover{background:#6f4c25}.secondary{display:block;text-align:center;color:#8b642d!important;text-decoration:underline!important;margin-bottom:24px}.fine{border-top:1px solid #c9aa78;margin:42px auto 0;max-width:760px}.rtl{direction:rtl}.footer{text-align:center;font-family:'Cormorant Garamond',serif;letter-spacing:.13em;color:#a17a44;margin-top:30px}
@media(max-width:650px){.brand-shell{min-height:310px;padding:24px 12px}.brand-shell:before{background-size:cover}.sun{font-size:3rem}.block-container{padding-left:1rem;padding-right:1rem}}
</style>'''.replace('ART',art),unsafe_allow_html=True)



import html

PRICE = 240
DELIVERY = 30
EMIRATES = ["Dubai", "Ras Al Khaimah", "Sharjah", "Ajman", "Abu Dhabi", "Umm Al Quwain", "Fujairah"]
WESTERN = ["المرفأ", "الرويس", "الظنة", "السلع", "غياثي", "بدع المطاوعة", "بينونة", "مدينة زايد", "بدع زايد", "مرابع الظفرة", "ليوا"]
ALAIN_30 = ["ناهل", "الساد"]
ALAIN_50 = ["سويحان", "رماح", "الخزنة", "أبو سمرة", "الختم", "الظاهرة", "العراد", "بوكريه", "الوقن", "القوع"]
# Verified area grouping. Ambiguous border-region localities stay in a separate
# regional selector rather than being incorrectly assigned to Sharjah.
SPECIAL_BY_EMIRATE = {
    "Sharjah": ["وادي الحلو"],
    "Ras Al Khaimah": ["شوكة", "وادي اصفني", "وادي اصفي"],
    "Fujairah": ["السيجي", "كدرا"],
    "Ajman": ["مصفوت", "مزيرع"],
    "Dubai": ["حتا", "المنيعي", "الحويلات"],
}
UNVERIFIED_REMOTE = ["وادي ممدوح", "مكن", "صعير", "وادي العجيلي", "رافاق", "جيما"]
EMIRATES.append("Other remote delivery areas / مناطق بعيدة أخرى")

def delivery_options(emirate):
    standard = ["Standard area / منطقة عادية"]
    if emirate == "Abu Dhabi":
        return standard + ["Western Region / المنطقة الغربية — " + x for x in WESTERN] + ["Al Ain / العين — " + x for x in ALAIN_30 + ALAIN_50]
    if emirate == "Other remote delivery areas / مناطق بعيدة أخرى":
        return ["Select remote area / اختر المنطقة — " + x for x in UNVERIFIED_REMOTE]
    return standard + ["Special area / منطقة خاصة — " + x for x in SPECIAL_BY_EMIRATE.get(emirate, [])]

def delivery_fee(area):
    return 50 if area.split(" — ")[-1] in WESTERN + ALAIN_50 else 30

def delivery_timing(area):
    name = area.split(" — ")[-1]
    if name in WESTERN:
        return ("Western Region delivery days: Sunday, Tuesday and Thursday.",
                "توصيل المنطقة الغربية أيام الأحد والثلاثاء والخميس.")
    if name in ALAIN_30 + ALAIN_50:
        return ("Delivery within two days.", "التوصيل خلال يومين.")
    return ("Delivery time will be confirmed before dispatch.", "سيتم تأكيد موعد التوصيل قبل الشحن.")


def local(en, arabic):
    return arabic if ar else en

st.markdown('<div style="text-align:center;padding:12px 8px 8px"><div style="font-family:Cormorant Garamond,serif;font-size:clamp(36px,7vw,68px);color:#986821;letter-spacing:.05em">HOUSE OF VÈR</div><div style="font-family:Cormorant Garamond,serif;letter-spacing:.16em;color:#9a722e;font-size:clamp(12px,2vw,19px)">THE ESSENCE OF PRESENCE</div></div>', unsafe_allow_html=True)
st.markdown("""<style>
div.stButton > button[kind="primary"]{background:#946d36;color:white;border-radius:2px;border:0;min-height:48px}
div.stButton > button{min-height:44px}
@media(max-width:650px){.block-container{padding:1rem .85rem 3rem}.bottle{max-width:280px;margin:12px auto}.section-title{margin:22px 0 10px}.copy{font-size:1.3rem}.price{font-size:2rem}}

/* Consistent cream and gold checkout controls regardless of Streamlit dark mode */
.stApp [data-testid="stForm"]{background:#fff8ef!important;border:1px solid #c7a677!important;border-radius:8px!important;padding:20px!important}
.stApp [data-testid="stWidgetLabel"] p,.stApp label,.stApp [data-testid="stMarkdownContainer"] p{color:#493425}
.stApp div[data-baseweb="input"],.stApp div[data-baseweb="textarea"],.stApp div[data-baseweb="select"]>div,.stApp [data-testid="stNumberInput"] input{
 background:#fffdf9!important;color:#493425!important;border-color:#cbb28b!important
}
.stApp input,.stApp textarea,.stApp input:focus,.stApp textarea:focus{background:#fffdf9!important;color:#493425!important;-webkit-text-fill-color:#493425!important;caret-color:#493425!important}
.stApp input::placeholder,.stApp textarea::placeholder{color:#8c7a65!important;opacity:1!important}
.stApp [data-baseweb="select"] span,.stApp [data-baseweb="select"] div{color:#493425}
.stApp [data-testid="stFormSubmitButton"] button,.stApp div.stButton>button[kind="primary"]{
 background:#946d36!important;color:#fffaf2!important;border:1px solid #946d36!important;font-weight:600!important
}
.stApp [data-testid="stFormSubmitButton"] button p,.stApp div.stButton>button[kind="primary"] p{color:#fffaf2!important}
.stApp [data-testid="stFormSubmitButton"] button:hover{background:#765122!important}
.stApp [data-testid="stRadio"] label p{color:#493425!important}
@media(max-width:650px){.stApp [data-testid="stForm"]{padding:14px!important}}

.stApp [data-testid="stAlert"]{background:#fff9ef!important;border:1px solid #d7b98d!important;color:#60482e!important;border-radius:6px!important}
.stApp [data-testid="stAlert"] *{color:#60482e!important}
.stApp div.stButton>button{background:#946d36!important;color:#fffaf2!important;border:1px solid #946d36!important;font-weight:600!important;border-radius:4px!important}
.stApp div.stButton>button p,.stApp div.stButton>button span{color:#fffaf2!important}
.stApp div.stButton>button:hover{background:#765122!important;color:white!important}
.stApp [data-testid="stRadio"] label{background:transparent!important}

/* Elegant cream-and-gold language picker and right-aligned menu */
.stApp [data-testid="stSelectbox"] label p{color:#986821!important;font-family:'Cormorant Garamond','Amiri',serif!important;letter-spacing:.06em;font-size:15px!important}
.stApp [data-testid="stSelectbox"] [data-baseweb="select"]>div{background:#fff5e9!important;border:1px solid #c7a578!important;border-radius:2px!important;box-shadow:none!important;color:#7e5a2a!important}
.stApp [data-testid="stSelectbox"] [data-baseweb="select"] span{color:#7e5a2a!important}
.stApp [data-testid="stPopover"] button{background:transparent!important;border:0!important;box-shadow:none!important;color:#986821!important;font-family:'Cormorant Garamond','Amiri',serif!important;letter-spacing:.1em!important;font-size:18px!important}
.stApp [data-testid="stPopover"] button p{color:#986821!important}
.stApp [data-testid="stPopover"] button:hover{background:#f8ebd9!important}
@media(max-width:650px){.stApp [data-testid="stPopover"] button{font-size:15px!important}.stApp [data-testid="stSelectbox"]{max-width:170px;margin-left:auto}}

/* Force the language control to blend into the champagne background */
.stApp .st-key-lang [data-baseweb="select"],
.stApp .st-key-lang [data-baseweb="select"] > div,
.stApp .st-key-lang [data-baseweb="select"] > div > div,
.stApp .st-key-lang [data-baseweb="select"] input {
 background-color:#fff5e9!important;
 background:#fff5e9!important;
 color:#8d6226!important;
 -webkit-text-fill-color:#8d6226!important;
 border-color:#c7a578!important;
 box-shadow:none!important;
}
.stApp .st-key-lang [data-baseweb="select"] *{color:#8d6226!important}
.stApp .st-key-lang label,.stApp .st-key-lang label p{color:#8d6226!important}

/* Minimal language switch beside menu */
.stApp [data-testid="stSegmentedControl"]{margin:0!important}
.stApp [data-testid="stSegmentedControl"] button{
 background:transparent!important;border:0!important;box-shadow:none!important;
 color:#986821!important;font-family:'Cormorant Garamond','Amiri',serif!important;
 font-size:16px!important;letter-spacing:.04em!important;padding:6px 9px!important
}
.stApp [data-testid="stSegmentedControl"] button[aria-checked="true"],
.stApp [data-testid="stSegmentedControl"] button[aria-pressed="true"],
.stApp [data-testid="stSegmentedControl"] button[data-state="on"]{
 background:#f3e4cd!important;color:#79521e!important;border-bottom:1px solid #a8782c!important
}
.stApp [data-testid="stSegmentedControl"] button:hover{background:#f7ead7!important}
@media(max-width:650px){.stApp [data-testid="stSegmentedControl"] button{font-size:13px!important;padding:5px 5px!important}}

/* Text-only gold language links; override the global button theme */
.stApp .st-key-lang_en button,.stApp .st-key-lang_ar button,
.stApp div.stButton.st-key-lang_en>button,.stApp div.stButton.st-key-lang_ar>button{
background:transparent!important;background-color:transparent!important;
border:0!important;border-radius:0!important;box-shadow:none!important;
padding:2px 4px!important;min-height:32px!important;height:32px!important;
color:#986821!important;-webkit-text-fill-color:#986821!important;
font-family:'Cormorant Garamond','Amiri',serif!important;font-size:16px!important;
letter-spacing:.03em!important
}
.stApp .st-key-lang_en button p,.stApp .st-key-lang_ar button p,
.stApp .st-key-lang_en button span,.stApp .st-key-lang_ar button span{
color:#986821!important;-webkit-text-fill-color:#986821!important;font-size:16px!important
}
.stApp .st-key-lang_en button:hover,.stApp .st-key-lang_ar button:hover{background:transparent!important;color:#79521e!important}
.stApp .st-key-lang_en button:focus,.stApp .st-key-lang_ar button:focus{box-shadow:none!important;outline:none!important}

@media(max-width:650px){.stApp .st-key-lang_en button,.stApp .st-key-lang_ar button{font-size:13px!important;padding:0!important}}

/* Language selector: selected radio dot clearly identifies active language */
.stApp [data-testid="stRadio"] [role="radiogroup"]{justify-content:center;gap:14px!important}
.stApp [data-testid="stRadio"] label{background:transparent!important;color:#8d6226!important}
.stApp [data-testid="stRadio"] label p{color:#8d6226!important;font-family:'Cormorant Garamond','Amiri',serif!important;font-size:17px!important}
.stApp [data-testid="stRadio"] input[type="radio"]{accent-color:#a8782c!important}
.stApp [data-testid="stRadio"] [data-baseweb="radio"]>div:first-child{background:transparent!important;border-color:#a8782c!important}
.stApp [data-testid="stRadio"] [aria-checked="true"] [data-baseweb="radio"]>div:first-child{border-color:#a8782c!important}
</style>""", unsafe_allow_html=True)

if "cart_qty" not in st.session_state:
    st.session_state.cart_qty = 0
if "page" not in st.session_state:
    st.session_state.page = "shop"

def go_to(destination):
    st.session_state.page = destination

nav_left, nav_lang, nav_right = st.columns([4.5, 1.8, 1.3], gap="small")
with nav_lang:
    selected_language = st.radio(
        "Language / اللغة",
        ["EN", "عربي"],
        index=1 if st.session_state.lang == "العربية" else 0,
        horizontal=True,
        label_visibility="collapsed",
        key="language_radio",
    )
    st.session_state.lang = "العربية" if selected_language == "عربي" else "English"
    ar = st.session_state.lang == "العربية"
with nav_right:
    with st.popover("☰  MENU" if not ar else "☰  القائمة", use_container_width=True):
        st.button(local("PERFUME", "العطر"), key="menu_perfume", use_container_width=True, on_click=go_to, args=("shop",))
        st.button(local("CART & PAYMENT", "السلة والدفع") + f" ({st.session_state.cart_qty})", key="menu_cart", use_container_width=True, on_click=go_to, args=("cart",))
if ar:
    st.markdown('<style>.stApp .st-key-lang_ar button{border-bottom:1px solid #986821!important}</style>',unsafe_allow_html=True)
else:
    st.markdown('<style>.stApp .st-key-lang_en button{border-bottom:1px solid #986821!important}</style>',unsafe_allow_html=True)
nav = st.session_state.page

if nav == "shop":
    st.markdown(f'<div class="bottle"><img src="{perfume}" alt="VÈR perfume bottle"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="price">AED {PRICE}</div><div class="muted">{local("VÈR Eau de Parfum · 100 ml", "عطر ڤير · ١٠٠ مل")}</div>', unsafe_allow_html=True)
    qty = st.number_input(local("Quantity", "الكمية"), min_value=1, max_value=20, value=1, step=1)
    if st.button(local("ADD TO CART", "أضف إلى السلة"), type="primary", use_container_width=True):
        st.session_state.cart_qty += int(qty)
        st.session_state.page = "cart"
        st.rerun()
    st.markdown(f'<a class="secondary" href="https://ig.me/m/houseofver_" target="_blank" rel="noopener noreferrer">{local("Prefer to order via Instagram?", "تفضل الطلب عبر إنستغرام؟")}</a>', unsafe_allow_html=True)
    st.markdown(f'<div class="fine"></div><div class="section-title">{t("about_title")}</div><div class="copy">{t("about")}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="fine"></div><div class="section-title">{local("FRAGRANCE NOTES", "نوتات العطر")}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="copy">{local("Top: Pink Pepper · Warm Spice", "المقدمة: فلفل وردي · توابل دافئة")}<br>{local("Heart: Elegant Florals", "القلب: نفحات زهرية أنيقة")}<br>{local("Base: Rich Woods · Leather · Amber · Musk", "القاعدة: أخشاب غنية · جلد · عنبر · مسك")}</div>', unsafe_allow_html=True)
    if notes_image:
        notes_src = img_data('notes.jpg.png')
        st.markdown(f'<div style="max-width:560px;margin:20px auto"><img src="{notes_src}" alt="VÈR fragrance notes" style="display:block;width:100%;height:auto;border-radius:4px"></div>', unsafe_allow_html=True)

else:
    st.markdown(f'<div class="section-title">{local("YOUR SHOPPING BAG", "سلة التسوق")}</div>', unsafe_allow_html=True)
    if st.session_state.cart_qty == 0:
        st.markdown(f'<div style="background:#fff9ef!important;color:#60482e!important;border:1px solid #d7b98d;border-left:4px solid #a8782c;border-radius:6px;padding:18px 20px;margin:12px 0 16px;font-size:17px">{local("Your bag is empty.", "سلتك فارغة.")}</div>', unsafe_allow_html=True)
        if st.button(local("Shop VÈR", "تسوق ڤير"), use_container_width=True):
            st.session_state.page = "shop"
            st.rerun()
    else:
        cart_qty = st.number_input(local("VÈR Eau de Parfum · 100 ml — Quantity", "عطر ڤير · ١٠٠ مل — الكمية"), min_value=0, max_value=20, step=1, key="cart_qty")
        if cart_qty == 0:
            st.session_state.page = "shop"
            st.rerun()
        emirate = st.selectbox(local("Delivery emirate", "إمارة التوصيل"), EMIRATES)
        area = st.selectbox(local("Delivery area", "منطقة التوصيل"), delivery_options(emirate))
        delivery = delivery_fee(area)
        timing_en, timing_ar = delivery_timing(area)
        st.markdown(f'<div style="background:#fff9ef;color:#684d2e;border:1px solid #c8aa79;border-left:4px solid #a8782c;padding:14px 16px;border-radius:5px;font-size:15px;line-height:1.6">{html.escape(local(timing_en, timing_ar))}</div>', unsafe_allow_html=True)
        subtotal = PRICE * cart_qty
        total = subtotal + delivery
        st.markdown(f"**{local('Perfume subtotal', 'قيمة العطر')}:** AED {subtotal}")
        st.markdown(f"**{local('Delivery', 'التوصيل')}:** AED {delivery}")
        st.markdown(f"### {local('Total', 'الإجمالي')}: AED {total}")
        st.caption(local("Delivery fee is calculated for your selected area, per order.", "يتم احتساب رسوم التوصيل حسب المنطقة المختارة لكل طلب."))
        st.markdown(f"#### {local('Delivery details', 'بيانات التوصيل')}")
        with st.form("delivery_details"):
            customer = st.text_input(local("Full name", "الاسم الكامل"))
            phone = st.text_input(local("UAE mobile number", "رقم الهاتف الإماراتي"))
            address = st.text_area(local("Delivery address and area", "العنوان والمنطقة"))
            confirmed = st.form_submit_button(local("Review payment options", "عرض خيارات الدفع"), use_container_width=True)
        if confirmed:
            if not customer.strip() or not phone.strip() or not address.strip():
                st.error(local("Please complete all delivery fields.", "يرجى تعبئة جميع بيانات التوصيل."))
                st.session_state.checkout_ready = False
            else:
                st.session_state.checkout_ready = True
                st.session_state.order_details = (customer.strip(), phone.strip(), address.strip(), emirate, area, cart_qty, total)
        if st.session_state.get("checkout_ready"):
            details = st.session_state.get("order_details")
            if details and details[3] == emirate and details[4] == area and details[5] == cart_qty and details[6] == total:
                st.success(local("Order details reviewed. Payment is not yet confirmed.", "تمت مراجعة بيانات الطلب. الدفع غير مؤكد بعد."))
                st.markdown(f"**{local('Payable amount', 'المبلغ المطلوب')}: AED {total}**")
                # Only show a Ziina payment link if its exact amount has been configured and checked.
                try:
                    ziina_links = st.secrets.get("ziina_links", {})
                except Exception:
                    ziina_links = {}
                link = ziina_links.get(str(total), "") if ziina_links else ""
                if isinstance(link, str) and link.startswith("https://pay.ziina.com/"):
                    st.link_button(local("PAY WITH ZIINA", "ادفع عبر زينة"), link, use_container_width=True)
                    st.warning(local("Pay only if Ziina displays exactly AED " + str(total) + ". A payment link does not automatically confirm your order on this site.", "ادفع فقط إذا ظهر مبلغ " + str(total) + " درهماً في زينة. لا يؤكد رابط الدفع الطلب تلقائياً في الموقع."))
                else:
                    st.info(local("Ziina payments are not connected yet. The business owner must add a verified Ziina payment link for this exact total.", "الدفع عبر زينة غير متصل بعد. يجب إضافة رابط دفع موثّق لهذا المبلغ تحديداً."))
                st.markdown(f'<a class="order" href="https://ig.me/m/houseofver_" target="_blank" rel="noopener noreferrer">{local("CONTACT US ON INSTAGRAM", "تواصل معنا عبر إنستغرام")}</a>', unsafe_allow_html=True)
                st.caption(local("No order is placed and no personal details are sent by this form. Confirm the order with HOUSE OF VÈR on Instagram.", "لا يتم إرسال بياناتك أو تسجيل طلب تلقائياً من هذا النموذج. أكّد الطلب مع هاوس أوف ڤير عبر إنستغرام."))
            else:
                st.session_state.checkout_ready = False
        st.markdown(f'<div class="fine"></div><div class="copy">{local("Need help? Contact @houseofver_ on Instagram.", "للمساعدة تواصل معنا عبر إنستغرام @houseofver_")}</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">HOUSE OF VÈR · THE ESSENCE OF PRESENCE</div>', unsafe_allow_html=True)
