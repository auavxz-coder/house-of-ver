import base64
from pathlib import Path
import streamlit as st
from order_store import save_order, upload_payment_proof, choose_payment, payment_state, lookup_order_status
import customer_auth as auth

st.set_page_config(page_title='HOUSE OF VÈR | The Essence of Presence', page_icon='✦', layout='wide', initial_sidebar_state='collapsed')
BASE=Path(__file__).parent

def img_data(name):
    p=BASE/name
    mime='image/jpeg' if p.suffix.lower() in ('.jpg','.jpeg') else 'image/png'
    return f'data:{mime};base64,{base64.b64encode(p.read_bytes()).decode()}'

if 'lang' not in st.session_state: st.session_state.lang='English'
requested_lang = st.query_params.get("lang", "")
if requested_lang in ("en", "ar"):
    st.session_state.lang = "العربية" if requested_lang == "ar" else "English"
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
 'contact':('STAY IN TOUCH','تواصل معنا'),
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
    emirate_ar = {"Dubai": "دبي", "Ras Al Khaimah": "رأس الخيمة", "Sharjah": "الشارقة", "Ajman": "عجمان", "Abu Dhabi": "أبوظبي", "Umm Al Quwain": "أم القيوين", "Fujairah": "الفجيرة"}
    standard = [f"{emirate} emirate / إمارة {emirate_ar[emirate]}"] if emirate in emirate_ar else ["Standard area / منطقة عادية"]
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

st.markdown('<div style="text-align:center;padding:12px 8px 8px"><div style="font-family:Cormorant Garamond,serif;font-size:clamp(30px,6vw,68px);color:#986821;letter-spacing:.05em">HOUSE OF VÈR</div><div style="font-family:Cormorant Garamond,serif;letter-spacing:.16em;color:#9a722e;font-size:clamp(12px,2vw,19px)">THE ESSENCE OF PRESENCE</div></div>', unsafe_allow_html=True)
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

/* HOUSE OF VÈR language switch: text-only, selected option underlined */
.stApp .st-key-language_radio [role="radiogroup"]{justify-content:center!important;gap:4px!important;align-items:center!important}
.stApp .st-key-language_radio [data-baseweb="radio"] > div:first-child{display:none!important}
.stApp .st-key-language_radio label{background:transparent!important;border:0!important;padding:3px 9px!important;cursor:pointer!important}
.stApp .st-key-language_radio label p{color:#986821!important;font-family:'Cormorant Garamond','Amiri',serif!important;font-size:17px!important;letter-spacing:.03em!important;text-decoration:none!important}
.stApp .st-key-language_radio label:has(input:checked) p,
.stApp .st-key-language_radio label:has([aria-checked="true"]) p{
text-decoration:underline!important;text-decoration-color:#986821!important;text-underline-offset:6px!important;text-decoration-thickness:1px!important;font-weight:600!important
}
.stApp .st-key-language_radio label:hover p{color:#79521e!important}
@media(max-width:650px){.stApp .st-key-language_radio label{padding:3px 4px!important}.stApp .st-key-language_radio label p{font-size:14px!important}}

/* Streamlit popover panel is rendered in a portal: style globally */
div[data-baseweb="popover"],div[data-baseweb="popover"]>div,
div[data-baseweb="popover"] [data-testid="stPopoverBody"],
div[data-testid="stPopoverBody"]{
background:#fff5e9!important;background-color:#fff5e9!important;
color:#795626!important;border-color:#d3b58a!important;box-shadow:0 12px 28px #70502d24!important
}
div[data-baseweb="popover"] button,div[data-testid="stPopoverBody"] button{
background:#fff5e9!important;background-color:#fff5e9!important;
border:1px solid #c8a675!important;border-radius:2px!important;
color:#8d6226!important;box-shadow:none!important
}
div[data-baseweb="popover"] button p,div[data-baseweb="popover"] button span,
div[data-testid="stPopoverBody"] button p{color:#8d6226!important}
div[data-baseweb="popover"] button:hover,div[data-testid="stPopoverBody"] button:hover{background:#f5e5cf!important}
div[data-baseweb="popover"] button:focus,div[data-testid="stPopoverBody"] button:focus{
outline:1px solid #b88a40!important;box-shadow:none!important;border-color:#b88a40!important
}

.checkout-notice{background:#fff9f0!important;color:#62482d!important;border:1px solid #d3b184!important;border-left:4px solid #a8782c!important;padding:16px 18px!important;border-radius:4px!important;margin:14px 0!important;line-height:1.6!important;font-size:15px!important}
.stApp [data-testid="stTextInput"] input,.stApp [data-testid="stTextArea"] textarea,
.stApp [data-testid="stForm"] input,.stApp [data-testid="stForm"] textarea,
.stApp [data-baseweb="input"] input,.stApp [data-baseweb="textarea"] textarea{
background:#fffaf4!important;background-color:#fffaf4!important;color:#463121!important;
-webkit-text-fill-color:#463121!important;caret-color:#463121!important;
border-color:#c9ac83!important;box-shadow:none!important
}
.stApp [data-testid="stTextInput"] [data-baseweb="input"],
.stApp [data-testid="stTextArea"] [data-baseweb="textarea"],
.stApp [data-testid="stForm"] [data-baseweb="input"],
.stApp [data-testid="stForm"] [data-baseweb="textarea"]{
background:#fffaf4!important;background-color:#fffaf4!important;
border:1px solid #c9ac83!important;box-shadow:none!important
}
.stApp [data-testid="stFormSubmitButton"] button,
.stApp [data-testid="stFormSubmitButton"] button:focus,
.stApp [data-testid="stFormSubmitButton"] button:active{
background:#946d36!important;border:1px solid #946d36!important;outline:none!important;
box-shadow:none!important;color:#fffaf2!important
}
.stApp [data-testid="stFormSubmitButton"] button p{color:#fffaf2!important}

/* Native inputs and browser autofill: keep ivory even when browser is in dark mode */
.stApp input,.stApp textarea,.stApp [data-baseweb="input"],.stApp [data-baseweb="textarea"],
.stApp [data-testid="stTextInput"] div[data-baseweb="base-input"],
.stApp [data-testid="stTextArea"] div[data-baseweb="textarea"]{
background-color:#fffaf4!important;background:#fffaf4!important;color:#463121!important;
-webkit-text-fill-color:#463121!important;box-shadow:none!important;
}
.stApp input:-webkit-autofill,.stApp input:-webkit-autofill:hover,
.stApp input:-webkit-autofill:focus,.stApp textarea:-webkit-autofill,
.stApp textarea:-webkit-autofill:focus{
-webkit-box-shadow:0 0 0 1000px #fffaf4 inset!important;
box-shadow:0 0 0 1000px #fffaf4 inset!important;
-webkit-text-fill-color:#463121!important;caret-color:#463121!important;
}
.stApp input:focus,.stApp textarea:focus{outline:1px solid #b8893b!important;box-shadow:none!important}

/* Mobile-first checkout: prevent desktop selectbox rules from shrinking address fields */
@media(max-width:700px){
  html,body{overflow-x:hidden!important}
  .stApp .block-container{width:100%!important;max-width:100%!important;padding:1rem 16px 3rem!important;overflow-x:hidden!important}
  .stApp [data-testid="stSelectbox"]{width:100%!important;max-width:none!important;margin-left:0!important}
  .stApp [data-testid="stSelectbox"] [data-baseweb="select"]{width:100%!important;max-width:none!important}
  .stApp [data-testid="stSelectbox"] [data-baseweb="select"]>div{width:100%!important;min-width:0!important}
  .stApp [data-testid="stSelectbox"] label p{font-size:15px!important;letter-spacing:0!important}
  .stApp [data-testid="stForm"]{width:100%!important;min-width:0!important;padding:14px!important}
  .stApp [data-testid="stTextInput"],.stApp [data-testid="stTextArea"],.stApp [data-testid="stNumberInput"]{width:100%!important;min-width:0!important}
  .stApp [data-testid="stNumberInput"] input{min-width:0!important}
  .section-title{font-size:clamp(27px,7vw,36px)!important;line-height:1.15!important;overflow-wrap:break-word!important;margin:22px 0 14px!important}
  .copy{font-size:19px!important;line-height:1.55!important}
  .stApp [data-testid="stMarkdownContainer"]{overflow-wrap:break-word}
  .stApp [data-testid="stHorizontalBlock"]{gap:6px!important}
  .stApp [data-testid="stColumn"]{min-width:0!important}
  .stApp .checkout-notice{font-size:14px!important;padding:12px!important}
  .stApp .bottle{max-width:min(310px,90vw)!important}
  .stApp .footer{font-size:12px!important;letter-spacing:.05em!important}
}

.thank-preview{text-align:center;color:#89612d;font-size:12px;letter-spacing:.08em;margin:12px auto 18px}
.thank-card{position:relative;max-width:850px;margin:10px auto 35px;padding:42px 30px 48px;background:#fff1e0;color:#936821;border:6px double #a87931;text-align:center;overflow:hidden;box-shadow:0 12px 30px #68432214}
.thank-star{font-size:60px;line-height:1;color:#c18b35}
.thank-brand{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(36px,6vw,66px);letter-spacing:.035em}
.thank-tagline{font-family:'Cormorant Garamond',Georgia,serif;letter-spacing:.23em;font-size:clamp(11px,2vw,18px)}
.thank-rule{width:90px;border-top:1px solid #aa803f;margin:25px auto}
.thank-script{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;font-size:clamp(62px,10vw,112px);line-height:1.1;margin:20px 0}
.thank-offer{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(27px,4vw,43px);line-height:1.25}
.thank-social{font-family:'Cormorant Garamond',Georgia,serif;font-size:clamp(22px,3vw,31px);font-style:italic;margin-top:40px}
.thank-social a{color:#936821!important}
.thank-clouds{position:relative;height:115px;margin:24px -30px -48px;overflow:hidden;pointer-events:none;background:linear-gradient(0deg,#d8a85c30,transparent)}
.thank-clouds .cloud{position:absolute;bottom:-65px;height:115px;border:1px solid #d7a557;border-radius:50%;background:radial-gradient(ellipse at 45% 30%,#fffaf1 8%,#f5dbaf 65%,#d2a057 100%);box-shadow:0 -6px 0 #e9c99555,18px -12px 0 #f2d8a688,-15px -4px 0 #dbaf6a55}
.thank-clouds .cloud-one{width:46%;left:-5%;transform:rotate(-9deg)}
.thank-clouds .cloud-two{width:48%;left:29%;bottom:-48px}
.thank-clouds .cloud-three{width:47%;right:-7%;transform:rotate(10deg)}
.thank-card:before,.thank-card:after{content:"";position:absolute;width:145px;height:75px;top:90px;border-radius:55%;border:1px solid #e4bb7b;background:radial-gradient(ellipse,#fff7e7 15%,#edcf9d 75%,#d9ad6a);opacity:.65;pointer-events:none}
.thank-card:before{left:-70px}.thank-card:after{right:-70px}
@media(max-width:650px){.thank-card{padding:25px 12px 20px;border-width:4px}.thank-star{font-size:48px}.thank-social{margin-top:28px}.thank-clouds{height:70px;margin:10px -12px -20px}.thank-clouds .cloud{height:75px;bottom:-48px}}
</style>""", unsafe_allow_html=True)

def render_payment_thank_you(preview=False, proof_received=False, cod_received=False, instagram_received=False):
    """Show the relevant pending-confirmation notice before the thank-you card."""
    if proof_received:
        message = local(
            "Thank you! We received your payment screenshot. Your order is NOT confirmed yet. HOUSE OF VÈR will check the amount actually received in Ziina. Only after payment is verified will we contact you through Instagram, email, or phone to confirm your order. Please keep your order number.",
            "شكراً على طلبك! تم استلام صورة إثبات الدفع، لكن الطلب لم يتأكد بعد. سنتحقق أولاً من المبلغ المستلم في زينة، وبعد التحقق من الدفع سنتواصل عبر الإنستغرام أو البريد الإلكتروني أو الهاتف لتأكيد الطلب. يرجى الاحتفاظ برقم الطلب.")
    elif cod_received:
        message = local(
            "Thank you! We received your cash-on-delivery order. Your order is NOT confirmed yet. We will contact you through Instagram, email, or phone to confirm delivery. The full amount, including the AED 5 cash-on-delivery fee, is payable upon delivery.",
            "شكراً على طلبك! تم استلام طلب الدفع عند الاستلام، لكنه لم يتأكد بعد. سنتواصل عبر الإنستغرام أو البريد الإلكتروني أو الهاتف لتأكيد التوصيل. يُدفع المبلغ الكامل شاملاً ٥ دراهم رسوم الدفع عند الاستلام وقت التوصيل.")
    elif instagram_received:
        message = local(
            "Thank you! Your order request has been received but is NOT confirmed. Please contact HOUSE OF VÈR on Instagram to request bank transfer details. Once the transfer is received and verified, we will contact you by Instagram, email, or phone to confirm your order.",
            "شكراً على طلبك! تم استلام الطلب لكنه لم يتأكد بعد. يرجى التواصل معنا عبر الإنستغرام للحصول على تفاصيل التحويل. بعد التحقق من وصول المبلغ سنتواصل عبر الإنستغرام أو البريد الإلكتروني أو الهاتف لتأكيد الطلب.")
    else:
        message = local("DESIGN PREVIEW — NOT A PAYMENT CONFIRMATION", "معاينة التصميم — ليست تأكيداً للدفع")
    st.markdown(f'<div class="checkout-notice">{html.escape(message)}</div>', unsafe_allow_html=True)
    if proof_received:
        st.caption(local("A screenshot alone does not confirm successful payment.", "صورة الدفع بروحها ما تعتبر تأكيد لوصول المبلغ."))
    st.markdown("""
    <div class="thank-card">
      <div class="thank-star">✨</div>
      <div class="thank-brand">HOUSE OF VÈR</div>
      <div class="thank-tagline">THE ESSENCE OF PRESENCE</div>
      <div class="thank-rule"></div>
      <div class="thank-script">Thank You</div>
      <div class="thank-social">Follow Us on Instagram<br><a href="https://www.instagram.com/houseofver_/" target="_blank" rel="noopener noreferrer">@houseofver_</a></div>
      <div class="thank-clouds" aria-hidden="true"><span class="cloud cloud-one"></span><span class="cloud cloud-two"></span><span class="cloud cloud-three"></span></div>
    </div>
    """, unsafe_allow_html=True)


# Never show a real payment success message from a query parameter or button click.
# Connect Ziina server-side verification before activating the paid-order flow.

if "cart_qty" not in st.session_state:
    st.session_state.cart_qty = 0
if "page" not in st.session_state:
    st.session_state.page = "shop"

def go_to(destination):
    st.session_state.page = destination

nav_left, nav_lang, nav_right = st.columns([4.5, 1.8, 1.3], gap="small")
with nav_lang:
    en_style = "border-bottom:1px solid #986821;font-weight:600" if not ar else "border-bottom:1px solid transparent"
    ar_style = "border-bottom:1px solid #986821;font-weight:600" if ar else "border-bottom:1px solid transparent"
    st.markdown(
        f'<div style="display:flex;justify-content:center;align-items:center;gap:10px;padding-top:7px;white-space:nowrap">'
        f'<a href="?lang=en" target="_self" style="font-family:Georgia,serif;color:#986821;text-decoration:none;padding:3px 2px;{en_style}">EN</a>'
        f'<span style="color:#bca078">|</span>'
        f'<a href="?lang=ar" target="_self" style="font-family:Georgia,serif;color:#986821;text-decoration:none;padding:3px 2px;{ar_style}">عربي</a>'
        f'</div>', unsafe_allow_html=True
    )
with nav_right:
    with st.popover("☰  MENU" if not ar else "☰  القائمة", use_container_width=True):
        st.button(local("PERFUME", "العطر"), key="menu_perfume", use_container_width=True, on_click=go_to, args=("shop",))
        st.button(local("CART & PAYMENT", "السلة والدفع") + f" ({st.session_state.cart_qty})", key="menu_cart", use_container_width=True, on_click=go_to, args=("cart",))
        st.button(local("OUR STORY", "قصتنا"), key="menu_story", use_container_width=True, on_click=go_to, args=("story",))
        st.button(local("TRACK YOUR ORDER", "تتبع الطلب"), key="menu_tracking", use_container_width=True, on_click=go_to, args=("tracking",))
        st.button(local("MY ACCOUNT", "حسابي"), key="menu_account", use_container_width=True, on_click=go_to, args=("account",))
if ar:
    st.markdown('<style>.stApp .st-key-lang_ar button{border-bottom:1px solid #986821!important}</style>',unsafe_allow_html=True)
else:
    st.markdown('<style>.stApp .st-key-lang_en button{border-bottom:1px solid #986821!important}</style>',unsafe_allow_html=True)
nav = "thankyou_preview" if st.query_params.get("preview") == "thankyou" else st.session_state.page

if nav == "thankyou_preview":
    render_payment_thank_you(preview=True)
elif nav == "story":
    st.markdown("""<style>
    .story-wrap{max-width:800px;margin:35px auto 70px;padding:0 14px}
    .story-kicker{text-align:center;color:#a27b46;font-size:12px;letter-spacing:.24em}
    .story-heading{font-family:'Cormorant Garamond','Amiri',serif;font-size:clamp(42px,6vw,72px);font-weight:400;color:#92672c;text-align:center;margin:10px 0 24px}
    .story-rule{height:1px;background:#d5b88d;max-width:110px;margin:25px auto 48px}
    .story-section{margin:0 0 52px}
    .story-section h2{font-family:'Cormorant Garamond','Amiri',serif;color:#946d36;font-size:clamp(29px,4vw,42px);font-weight:500;margin:0 0 12px}
    .story-section p{font-family:'Cormorant Garamond','Amiri',serif;color:#493425;font-size:clamp(20px,2.4vw,26px);line-height:1.7;margin:0 0 16px}
    .story-rtl{text-align:right;direction:rtl}
    .story-rtl p,.story-rtl h2{font-family:'Amiri',serif}
    @media(max-width:650px){.story-wrap{margin:16px auto 50px;padding:0 6px}.story-section{margin-bottom:35px}.story-section p{font-size:21px}}
    </style>""", unsafe_allow_html=True)
    sections = [
        (("THE PHILOSOPHY", "الفلسفة"),
         ("HOUSE OF VÈR is guided by a simple belief: presence does not need to be loud to be unforgettable. The house celebrates understated elegance, individuality, and the quiet confidence that stays long after a moment has passed.",
          "تؤمن هاوس أوف ڤير بأن الحضور لا يحتاج إلى ضجيج حتى يبقى في الذاكرة. تحتفي الدار بالأناقة الهادئة والتفرّد والثقة التي تترك أثرها حتى بعد مرور اللحظة.")),
        (("THE ART OF FRAGRANCE", "فن العطر"),
         ("Fragrance is more than an accessory. It becomes part of how a person moves through the world — an intimate detail, a familiar feeling, and a memory waiting to be made.",
          "العطر أكثر من مجرد لمسة أخيرة، فهو جزء من حضور الإنسان في العالم، وتفصيل شخصي يحمل إحساساً مألوفاً وذكرى تنتظر أن تُصنع.")),
        (("VÈR — THE SIGNATURE", "ڤير — البصمة"),
         ("VÈR expresses the house's character through contrast: a lively opening of pink pepper and warm spice, an elegant floral heart, and a deep base of woods, leather, amber, and musk.",
          "يعبّر عطر ڤير عن شخصية الدار بتوازن بين التباين والانسجام؛ افتتاحية من الفلفل الوردي والتوابل الدافئة، وقلب زهري أنيق، وقاعدة عميقة من الأخشاب والجلد والعنبر والمسك.")),
        (("THE ESSENCE OF PRESENCE", "جوهر الحضور"),
         ("HOUSE OF VÈR is devoted to the impression that remains. Not simply a scent to wear, but a presence to remember.",
          "تحتفي هاوس أوف ڤير بالأثر الذي يبقى؛ ليس مجرد عطر يُرتدى، بل حضور لا يُنسى.")),
    ]
    story_class = "story-wrap story-rtl" if ar else "story-wrap"
    story_html = '<div class="' + story_class + '">'
    story_html += '<div class="story-kicker">HOUSE OF VÈR</div>'
    story_html += '<div class="story-heading">' + local("OUR STORY", "قصتنا") + '</div>'
    story_html += '<div class="story-rule"></div>'
    for headings, paragraphs in sections:
        story_html += '<section class="story-section"><h2>' + local(*headings) + '</h2><p>' + local(*paragraphs) + '</p></section>'
    story_html += '</div>'
    st.markdown(story_html, unsafe_allow_html=True)
    st.markdown(f'<a class="order" href="https://ig.me/m/houseofver_" target="_blank" rel="noopener noreferrer">{local("DISCOVER VÈR ON INSTAGRAM", "اكتشف ڤير عبر إنستغرام")}</a>', unsafe_allow_html=True)
elif nav == "account":
    st.markdown(f'<div class="section-title">{local("MY ACCOUNT", "حسابي")}</div>',unsafe_allow_html=True)
    st.markdown(
        '<div style="background:linear-gradient(115deg,#f3e2c9,#fff9f0 68%,#ead0a5);'
        'border:1px solid #d7b98b;border-radius:14px;padding:24px 28px;margin:14px 0 24px;'
        'text-align:center;box-shadow:0 8px 26px rgba(88,60,30,.06)">'
        '<div style="font-family:Georgia,serif;font-size:12px;letter-spacing:.22em;color:#a07840">'
        'HOUSE OF VÈR</div>'
        '<div style="font-family:Georgia,serif;font-size:clamp(24px,4vw,36px);'
        'color:#64452a;margin:13px 0">'
        +html.escape(local("YOUR PRIVATE WORLD OF VÈR","عالم ڤير الخاص بك"))+'</div>'
        '<div style="font-family:Georgia,serif;color:#80664a;font-size:16px;line-height:1.7">'
        +html.escape(local("A more personal way to shop, save your bag, and revisit your orders.", "تجربة تسوق خاصة تتيح حفظ السلة والعودة إلى طلباتك بسهولة."))+'</div></div>',
        unsafe_allow_html=True)
    st.caption(local("Accounts are optional. Guest checkout remains available.", "الحساب اختياري، ويمكن إكمال الطلب كضيف."))
    try:
        configured=bool(st.secrets.get("SUPABASE_PUBLISHABLE_KEY",""))
    except Exception:
        configured=False
    if not configured:
        st.warning(local("Customer accounts are not activated yet. Guest checkout is available.", "حسابات العملاء غير مفعلة بعد. الطلب كضيف متاح."))
    elif not st.session_state.get("customer_token"):
        tab=st.radio(local("Account action", "إجراء الحساب"),["login","signup","recover"],horizontal=True,
            format_func=lambda x:{"login":local("Sign in","تسجيل الدخول"),"signup":local("Create account","إنشاء حساب"),"recover":local("Reset password","استعادة كلمة المرور")}[x])
        with st.form("customer_auth_form"):
            email=st.text_input(local("Email", "البريد الإلكتروني"))
            password=st.text_input(local("Password", "كلمة المرور"),type="password") if tab!="recover" else ""
            submitted=st.form_submit_button(local("CONTINUE","متابعة"))
        if submitted:
            try:
                if tab=="recover":
                    auth.recover(email)
                    st.success(local("If this account exists, password recovery instructions will be emailed.", "إذا كان الحساب موجوداً، ستصل تعليمات استعادة كلمة المرور إلى البريد الإلكتروني."))
                elif tab=="signup":
                    if len(password)<10:
                        st.error(local("Use a password of at least 10 characters.", "استخدم كلمة مرور من ١٠ أحرف على الأقل."))
                    else:
                        auth.signup(email,password)
                        st.success(local("Check your email to confirm your account, then sign in.", "يرجى تأكيد الحساب عبر البريد الإلكتروني ثم تسجيل الدخول."))
                else:
                    session=auth.signin(email,password)
                    user=auth.current_user(session["access_token"])
                    st.session_state.customer_token=session["access_token"]
                    st.session_state.customer_id=user["id"]
                    st.session_state.customer_email=user["email"]
                    profile=auth.get_profile(session["access_token"])
                    st.session_state.customer_profile=profile
                    if profile.get("cart_qty") is not None:
                        st.session_state.cart_qty=int(profile["cart_qty"])
                    st.rerun()
            except (ValueError,RuntimeError,KeyError):
                st.error(local("Unable to complete account request. Check your details and account settings.", "تعذر إكمال العملية. يرجى مراجعة البيانات وإعدادات الحساب."))
    else:
        profile=st.session_state.get("customer_profile",{})
        display_name=(profile.get("full_name") or st.session_state.get("customer_email","")).strip()
        st.markdown("""
        <style>
        .ver-account-hero{background:linear-gradient(115deg,#f4e5cf,#fff9f0 65%,#ecd3aa);
          border:1px solid #d7b98b;border-radius:14px;padding:28px 30px;margin:16px 0 24px;
          box-shadow:0 8px 26px rgba(88,60,30,.07)}
        .ver-account-kicker{font-family:Georgia,serif;font-size:12px;letter-spacing:.19em;color:#9b743c}
        .ver-account-name{font-family:Georgia,serif;font-size:clamp(26px,5vw,39px);color:#624329;
          margin:12px 0 8px;overflow-wrap:anywhere}
        .ver-account-sub{font-size:14px;color:#846d54;overflow-wrap:anywhere}
        .ver-account-section{font-family:Georgia,serif;color:#76512c;letter-spacing:.08em;
          font-size:22px;margin:22px 0 6px}
        .ver-account-rule{height:1px;background:linear-gradient(90deg,#b78c4f,#e6d3b6,transparent);
          margin-bottom:18px}
        .ver-order-card{background:#fff9f0;border:1px solid #dfc9a8;border-left:3px solid #a47b42;
          border-radius:10px;padding:19px 20px;margin:12px 0}
        .ver-order-top{display:flex;flex-wrap:wrap;justify-content:space-between;gap:10px;align-items:center}
        .ver-order-id{font-family:Georgia,serif;font-size:17px;color:#583c27;overflow-wrap:anywhere}
        .ver-order-price{font-family:Georgia,serif;font-size:22px;color:#8c662e}
        .ver-order-meta{display:flex;flex-wrap:wrap;gap:9px;margin-top:14px}
        .ver-order-pill{background:#f4e6d2;border:1px solid #e1c69c;border-radius:20px;
          color:#705032;font-size:12px;padding:6px 12px}
        @media(max-width:640px){.ver-account-hero{padding:22px 18px}
          .ver-order-card{padding:15px}.ver-account-section{font-size:20px}}
        </style>
        """,unsafe_allow_html=True)
        st.markdown(
            '<div class="ver-account-hero"><div class="ver-account-kicker">HOUSE OF VÈR · '+html.escape(local("MEMBER ACCOUNT","حساب العميل"))+'</div>'
            '<div class="ver-account-name">'+html.escape(local("Welcome, ","مرحباً، ")+display_name)+'</div>'
            '<div class="ver-account-sub">'+html.escape(st.session_state.get("customer_email",""))+'</div></div>',
            unsafe_allow_html=True)
        st.markdown('<div class="ver-account-section">'+html.escape(local("PERSONAL DETAILS","البيانات الشخصية"))+'</div><div class="ver-account-rule"></div>',unsafe_allow_html=True)
        st.caption(local("Keep your delivery details up to date for a smoother checkout.", "احتفظ ببيانات التوصيل محدثة لتسهيل الطلبات القادمة."))
        with st.container(border=True):
            with st.form("customer_profile_form"):
                c1,c2=st.columns(2,gap="medium")
                with c1:
                    fullname=st.text_input(local("Full name","الاسم الكامل"),value=profile.get("full_name") or "",max_chars=120)
                    phone=st.text_input(local("Phone","رقم الهاتف"),value=profile.get("phone") or "",max_chars=30)
                with c2:
                    instagram=st.text_input(local("Instagram","الإنستغرام"),value=profile.get("instagram") or "",max_chars=60)
                    st.text_input(local("Account email","البريد الإلكتروني للحساب"),value=st.session_state.get("customer_email",""),disabled=True)
                address=st.text_area(local("Saved delivery address","عنوان التوصيل المحفوظ"),value=profile.get("address") or "",max_chars=500)
                save=st.form_submit_button(local("SAVE CHANGES","حفظ التغييرات"),use_container_width=True)
        if save:
            try:
                auth.save_profile(st.session_state.customer_token,st.session_state.customer_id,
                    full_name=fullname,phone=phone,instagram=instagram,address=address)
                st.session_state.customer_profile=auth.get_profile(st.session_state.customer_token)
                st.success(local("Details saved.","تم حفظ البيانات."))
                st.rerun()
            except Exception:
                st.error(local("Could not save details.","تعذر حفظ البيانات."))
        try:
            orders=auth.my_orders(st.session_state.customer_token)
            fulfillment_labels={
                "new":local("Order received","تم استلام الطلب"),
                "preparing":local("Preparing","قيد التجهيز"),
                "shipped":local("Shipped","تم الشحن"),
                "delivered":local("Delivered","تم التوصيل"),
                "cancelled":local("Cancelled","ملغي")}
            payment_labels={
                "awaiting_verification":local("Awaiting payment selection","بانتظار اختيار الدفع"),
                "ziina_pending":local("Ziina verification pending","بانتظار التحقق من زينة"),
                "cod_pending":local("Cash on delivery","الدفع عند الاستلام"),
                "paid_verified":local("Payment verified","تم التحقق من الدفع"),
                "instagram_pending":local("Transfer pending","التحويل قيد الانتظار"),
                "failed":local("Payment not verified","لم يتم تأكيد الدفع"),
                "refunded":local("Refunded","تم الاسترجاع")}
            st.markdown('<div class="ver-account-section">'+html.escape(local("ACCOUNT OVERVIEW","نظرة عامة على الحساب"))+'</div><div class="ver-account-rule"></div>',unsafe_allow_html=True)
            total_orders=len(orders)
            active_orders=sum(o.get("fulfillment_status") not in ("delivered","cancelled") for o in orders)
            last_order=orders[0].get("order_id") if orders else None
            m1,m2,m3=st.columns(3,gap="small")
            m1.metric(local("TOTAL ORDERS","إجمالي الطلبات"),total_orders)
            m2.metric(local("ACTIVE ORDERS","الطلبات الجارية"),active_orders)
            m3.metric(local("SAVED BAG","السلة المحفوظة"),int(st.session_state.get("cart_qty",0)))
            if last_order:
                st.caption(local("Latest order: ","آخر طلب: ")+str(last_order))
            st.markdown('<div class="ver-account-section">'+html.escape(local("MY ORDERS","طلباتي"))+'</div><div class="ver-account-rule"></div>',unsafe_allow_html=True)
            if not orders:
                st.caption(local("No account-linked orders yet. Guest orders are not automatically linked.", "لا توجد طلبات مرتبطة بالحساب بعد. الطلبات السابقة كضيف لا ترتبط تلقائياً."))
            for order in orders:
                oid=html.escape(str(order.get("order_id","")))
                total=html.escape(str(order.get("total","—")))
                fulfillment=html.escape(fulfillment_labels.get(order.get("fulfillment_status"),local("Contact us for status","يرجى التواصل لمعرفة الحالة")))
                payment=html.escape(payment_labels.get(order.get("payment_status"),local("Payment status unavailable","حالة الدفع غير متاحة")))
                st.markdown(
                    '<div class="ver-order-card">'
                    '<div style="display:flex;align-items:center;gap:17px;flex-wrap:wrap">'
                    '<img src="'+perfume+'" alt="VÈR Eau de Parfum 100 ml" '
                    'style="width:105px;height:125px;object-fit:cover;border-radius:7px;'
                    'border:1px solid #dfc9a8;flex-shrink:0">'
                    '<div style="flex:1;min-width:180px">'
                    '<div class="ver-account-kicker">'+html.escape(local("ORDER NUMBER","رقم الطلب"))+'</div>'
                    '<div class="ver-order-id">'+oid+'</div>'
                    '<div style="font-family:Georgia,serif;color:#775736;margin-top:9px">'
                    +html.escape(local("VÈR Eau de Parfum · 100 ml","عطر ڤير · ١٠٠ مل"))+'</div>'
                    '<div class="ver-order-price" style="margin-top:8px">AED '+total+'</div>'
                    '</div></div>'
                    '<div class="ver-order-meta"><span class="ver-order-pill">'+fulfillment+'</span>'
                    '<span class="ver-order-pill">'+payment+'</span></div></div>',
                    unsafe_allow_html=True)
                with st.expander(local("VIEW ORDER DETAILS","عرض تفاصيل الطلب")+" · "+str(order.get("order_id",""))):
                    try:
                        details=auth.my_order_details(st.session_state.customer_token,str(order.get("order_id","")))
                        if not details or not isinstance(details,dict):
                            st.warning(local("Details are unavailable for this order.","تفاصيل هذا الطلب غير متاحة."))
                        else:
                            def money(value):
                                try:
                                    return f"{float(value):,.2f}".rstrip("0").rstrip(".")
                                except (TypeError,ValueError):
                                    return "—"
                            def detail_row(label,value,emphasis=False):
                                color="#785327" if emphasis else "#66513d"
                                weight="700" if emphasis else "400"
                                st.markdown(
                                    '<div style="display:flex;justify-content:space-between;gap:16px;'
                                    'align-items:baseline;border-bottom:1px solid #ead9c3;padding:11px 3px;'
                                    'font-family:Georgia,serif;color:'+color+';font-weight:'+weight+'">'
                                    '<span>'+html.escape(label)+'</span><span style="text-align:right">'
                                    +html.escape(str(value))+'</span></div>',unsafe_allow_html=True)
                            st.markdown('<div style="font-family:Georgia,serif;font-size:21px;color:#8e692f;'
                                'padding:12px 0 5px">'+html.escape(local("ORDER SUMMARY","ملخص الطلب"))+'</div>',unsafe_allow_html=True)
                            detail_row(local("Product","المنتج"),local("VÈR Eau de Parfum · 100 ml","عطر ڤير · ١٠٠ مل"))
                            detail_row(local("Quantity","الكمية"),details.get("quantity","—"))
                            detail_row(local("Perfume subtotal","مجموع العطر"),"AED "+money(details.get("subtotal")))
                            detail_row(local("Delivery","التوصيل"),"AED "+money(details.get("delivery_fee")))
                            try:
                                adjustment=round(float(details["total"])-float(details["subtotal"])-float(details["delivery_fee"]),2)
                            except (TypeError,ValueError,KeyError):
                                adjustment=None
                            if adjustment is not None and abs(adjustment)>0.001:
                                adjustment_label=(local("Cash on delivery fee","رسوم الدفع عند الاستلام")
                                    if abs(adjustment-5)<0.001 else local("Additional charge / adjustment","رسوم إضافية / تعديل"))
                                detail_row(adjustment_label,("AED "+money(adjustment)))
                            detail_row(local("Total","الإجمالي"),"AED "+money(details.get("total")),True)
                            st.markdown('<div style="font-family:Georgia,serif;font-size:19px;color:#8e692f;'
                                'padding:23px 0 5px">'+html.escape(local("DELIVERY & STATUS","التوصيل وحالة الطلب"))+'</div>',unsafe_allow_html=True)
                            detail_row(local("Emirate","الإمارة"),details.get("emirate") or "—")
                            detail_row(local("Area","المنطقة"),details.get("area") or "—")
                            detail_row(local("Payment status","حالة الدفع"),payment_labels.get(details.get("payment_status"),local("Contact the store","يرجى التواصل مع المتجر")))
                            detail_row(local("Order status","حالة الطلب"),fulfillment_labels.get(details.get("fulfillment_status"),local("Contact the store","يرجى التواصل مع المتجر")))
                            st.markdown('<div style="font-family:Georgia,serif;font-size:19px;color:#8e692f;'
                                'padding:23px 0 10px">'+html.escape(local("ORDER JOURNEY","مراحل الطلب"))+'</div>',unsafe_allow_html=True)
                            stage=details.get("fulfillment_status","new")
                            journey=[("new",local("Received","تم الاستلام")),
                                     ("preparing",local("Preparing","قيد التجهيز")),
                                     ("shipped",local("Shipped","تم الشحن")),
                                     ("delivered",local("Delivered","تم التوصيل"))]
                            if stage=="cancelled":
                                st.warning(local("This order has been cancelled.","تم إلغاء هذا الطلب."))
                            elif stage in dict(journey):
                                current=[x[0] for x in journey].index(stage)
                                parts=[]
                                for idx,(code,label) in enumerate(journey):
                                    active=idx<=current
                                    circle="#99703a" if active else "#e5d7c3"
                                    text_color="#664725" if active else "#978572"
                                    symbol="✓" if idx<current else "●" if idx==current else str(idx+1)
                                    parts.append(
                                        '<div style="flex:1;min-width:65px;text-align:center">'
                                        '<div style="width:31px;height:31px;margin:0 auto 9px;border-radius:50%;'
                                        'background:'+circle+';color:'+("#fffaf2" if active else "#806a50")+';'
                                        'display:flex;align-items:center;justify-content:center;font-size:14px">'
                                        +symbol+'</div><div style="font-size:12px;color:'+text_color+';'
                                        'font-family:Georgia,serif;line-height:1.4">'+html.escape(label)+'</div></div>')
                                st.markdown('<div style="display:flex;gap:7px;padding:17px 8px;'
                                    'background:#fff8ed;border:1px solid #dfc9a8;border-radius:9px;'
                                    'margin:8px 0 15px">'+''.join(parts)+'</div>',unsafe_allow_html=True)
                            else:
                                st.info(local("Contact HOUSE OF VÈR for the current order stage.","يرجى التواصل مع HOUSE OF VÈR لمعرفة مرحلة الطلب."))
                            st.caption(local("Payment verification and order updates are handled by HOUSE OF VÈR.","التحقق من الدفع وتحديث الطلبات يتم من قبل HOUSE OF VÈR."))
                    except Exception:
                        st.warning(local("Order details are not enabled yet. The store must run the secure order-details SQL setup.","تفاصيل الطلب غير مفعّلة بعد. يجب تشغيل إعداد SQL الآمن لتفاصيل الطلبات."))
        except Exception:
            st.warning(local("Order history is temporarily unavailable.","سجل الطلبات غير متاح حالياً."))
        st.markdown('<div class="ver-account-section">'+html.escape(local("ACCOUNT SETTINGS","إعدادات الحساب"))+'</div><div class="ver-account-rule"></div>',unsafe_allow_html=True)
        if st.button(local("SIGN OUT","تسجيل الخروج"),key="customer_signout"):
            for key in ("customer_token","customer_id","customer_email","customer_profile","last_synced_cart"):
                st.session_state.pop(key,None)
            st.rerun()

elif nav == "tracking":
    st.markdown(f'<div class="section-title">{local("TRACK YOUR ORDER", "تتبع الطلب")}</div>',unsafe_allow_html=True)
    st.markdown(
        '<div style="background:linear-gradient(115deg,#f4e5cf,#fff9f0 68%,#ead0a5);'
        'border:1px solid #d7b98b;border-radius:12px;padding:23px 26px;margin:15px 0 24px;'
        'color:#65462b;box-shadow:0 8px 25px rgba(88,60,30,.06)">'
        '<div style="font-family:Georgia,serif;letter-spacing:.15em;font-size:12px;color:#9b743c;margin-bottom:12px">'
        +html.escape(local("GUEST ORDER TRACKING","تتبع طلبات الضيوف"))+'</div>'
        '<div style="font-family:Georgia,serif;font-size:clamp(19px,3vw,25px);line-height:1.5">'
        +html.escape(local("Continued as a guest? Track your HOUSE OF VÈR order here.", "أكملت الطلب كضيف؟ تابع حالة طلبك من HOUSE OF VÈR هنا."))+'</div>'
        '<div style="font-size:14px;line-height:1.6;margin-top:12px">'
        +html.escape(local("Enter your order number, email and phone number used at checkout. Signed-in customers can view their orders in My Account.", "أدخل رقم الطلب والبريد الإلكتروني ورقم الهاتف المستخدم عند الطلب. يمكن لأصحاب الحسابات متابعة طلباتهم من صفحة حسابي."))+'</div></div>',
        unsafe_allow_html=True)
    with st.form("track_order_form"):
        track_id=st.text_input(local("Order number", "رقم الطلب"),placeholder="VER-XXXXXXXXXXXX",max_chars=20)
        track_email=st.text_input(local("Email used for the order", "البريد الإلكتروني المستخدم في الطلب"),max_chars=254)
        track_phone=st.text_input(local("Phone number used for the order", "رقم الهاتف المستخدم في الطلب"),max_chars=30)
        track_submit=st.form_submit_button(local("CHECK ORDER STATUS", "عرض حالة الطلب"),use_container_width=True)
    if track_submit:
        import time
        last=st.session_state.get("last_tracking_check",0.0)
        if time.monotonic()-last < 10:
            st.warning(local("Please wait before trying again.", "يرجى الانتظار قليلاً قبل المحاولة مجدداً."))
        else:
            st.session_state.last_tracking_check=time.monotonic()
            try:
                found=lookup_order_status(track_id,track_email,track_phone)
                if not found:
                    st.warning(local("No matching order was found. Check the details or contact us on Instagram.", "لم يتم العثور على طلب مطابق. يرجى مراجعة البيانات أو التواصل معنا عبر الإنستغرام."))
                else:
                    fulfillment = found.get("fulfillment_status","new")
                    payment = found.get("payment_status","awaiting_verification")
                    steps = [
                        (local("Order received", "تم استلام الطلب"),local("Your order request has been saved.", "تم تسجيل طلبك في النظام.")),
                        (local("Preparing", "قيد التجهيز"),local("Your perfume is being prepared.", "طلبك قيد التجهيز.")),
                        (local("Shipped", "تم الشحن"),local("Your order is on its way.", "طلبك في الطريق.")),
                        (local("Delivered", "تم التوصيل"),local("Your order has been delivered.", "تم توصيل الطلب."))
                    ]
                    positions={"new":0,"preparing":1,"shipped":2,"delivered":3}
                    payment_labels={
                        "awaiting_verification":local("Awaiting payment selection", "بانتظار اختيار الدفع"),
                        "ziina_pending":local("Ziina payment awaiting verification", "دفع زينة بانتظار التحقق"),
                        "cod_pending":local("Cash on delivery — payment due on delivery", "الدفع عند الاستلام — المبلغ مستحق عند التوصيل"),
                        "paid_verified":local("Payment verified", "تم التحقق من الدفع"),
                        "instagram_pending":local("Instagram transfer awaiting verification", "التحويل عبر الإنستغرام بانتظار التحقق"),
                        "failed":local("Payment could not be verified", "تعذر التحقق من الدفع"),
                        "refunded":local("Refunded", "تم استرجاع المبلغ")
                    }
                    st.markdown(f'<div class="checkout-notice" style="text-align:center"><strong>{html.escape(found["order_id"])}</strong></div>',unsafe_allow_html=True)
                    st.markdown("#### "+local("Payment", "الدفع"))
                    st.markdown('<div style="padding:13px 17px;border:1px solid #d6b98c;border-radius:7px;background:#fff8ef;color:#65482c">'+html.escape(payment_labels.get(payment,local("Contact the store for payment status", "يرجى التواصل مع المتجر لمعرفة حالة الدفع")))+'</div>',unsafe_allow_html=True)
                    st.markdown("#### "+local("Order journey", "مراحل الطلب"))
                    if fulfillment=="cancelled":
                        st.error(local("This order was cancelled. Please contact HOUSE OF VÈR for assistance.", "تم إلغاء هذا الطلب. يرجى التواصل مع HOUSE OF VÈR للمساعدة."))
                    elif fulfillment in positions:
                        current=positions[fulfillment]
                        for idx,(label,description) in enumerate(steps):
                            reached=idx<=current
                            marker="✓" if idx<current else "●" if idx==current else "○"
                            bg="#f4e6d0" if reached else "#fff9f0"
                            border="#aa7b38" if reached else "#dfcfb8"
                            color="#644522" if reached else "#8c806f"
                            st.markdown(
                                '<div style="display:flex;align-items:flex-start;gap:13px;'
                                'border:1px solid '+border+';border-radius:8px;'
                                'background:'+bg+';padding:13px 16px;margin:8px 0;color:'+color+'">'
                                '<span style="font-size:23px;min-width:25px" aria-hidden="true">'+marker+'</span>'
                                '<div><div style="font-weight:700;font-size:17px">'+html.escape(label)+'</div>'
                                '<div style="font-size:14px;margin-top:3px">'+html.escape(description if reached else local("Not reached yet", "لم تصل هذه المرحلة بعد"))+'</div></div></div>',
                                unsafe_allow_html=True)
                    else:
                        st.info(local("Please contact HOUSE OF VÈR for an update.", "يرجى التواصل مع HOUSE OF VÈR لمعرفة حالة الطلب."))
                    st.caption(local("Statuses are updated manually by HOUSE OF VÈR. Payment proof does not confirm payment.", "يتم تحديث الحالات يدوياً من قبل HOUSE OF VÈR. صورة إثبات الدفع لا تعني تأكيد وصول المبلغ."))
            except Exception:
                st.error(local("Order tracking is temporarily unavailable. Please try again later.", "خدمة التتبع غير متاحة حالياً. يرجى المحاولة لاحقاً."))
elif nav == "shop":
    st.markdown(f'<div class="bottle"><img src="{perfume}" alt="VÈR perfume bottle"></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="price">AED {PRICE}</div><div class="muted">{local("VÈR Eau de Parfum · 100 ml", "عطر ڤير · ١٠٠ مل")}</div>', unsafe_allow_html=True)
    qty = st.number_input(local("Quantity", "الكمية"), min_value=1, max_value=20, value=1, step=1)
    if st.button(local("ADD TO CART", "أضف إلى السلة"), type="primary", use_container_width=True):
        st.session_state.cart_qty = min(20, st.session_state.cart_qty + int(qty))
        if st.session_state.get("customer_token"):
            try:
                auth.save_profile(st.session_state.customer_token,st.session_state.customer_id,cart_qty=st.session_state.cart_qty)
            except Exception:
                st.warning(local("Cart could not sync to your account.", "تعذرت مزامنة السلة مع الحساب."))
        st.session_state.page = "cart"
        st.rerun()
    st.markdown(
        '<div style="background:#fff8ef;color:#65482c;border:1px solid #d6b98c;'
        'border-left:3px solid #a67b3c;border-radius:5px;padding:17px 18px;'
        'line-height:1.65;font-size:16px;margin:16px 0">'
        + html.escape(local("Prefer to order via Instagram and pay by bank transfer? Contact us on Instagram to arrange your order and receive transfer details.", "للطلب عبر الإنستغرام والدفع بتحويل بنكي، يرجى التواصل معنا لترتيب الطلب والحصول على تفاصيل التحويل."))
        + '</div>', unsafe_allow_html=True)
    st.markdown("""<style>
    [data-testid="stLinkButton"] a[href*="ig.me/m/houseofver_"] {
      background:#946d36!important;color:#fff8ef!important;
      border:1px solid #946d36!important;border-radius:5px!important;
      font-family:Georgia,serif!important;letter-spacing:.025em!important;
      min-height:48px!important;box-shadow:none!important;
    }
    [data-testid="stLinkButton"] a[href*="ig.me/m/houseofver_"]:hover {
      background:#7d592b!important;color:#ffffff!important;
    }
    </style>""", unsafe_allow_html=True)
    st.link_button(local("ORDER VIA INSTAGRAM — BANK TRANSFER", "اطلبي عبر الإنستغرام — تحويل بنكي"), "https://ig.me/m/houseofver_", use_container_width=True)
    st.markdown(f'<div class="fine"></div><div class="section-title">{t("about_title")}</div><div class="copy">{t("about")}</div>', unsafe_allow_html=True)
    st.markdown("### " + local("DISCOVER THE SCENT", "اكتشف نوتات العطر"))
    st.caption(local("A balanced composition that unfolds in three layers.", "تركيبة متوازنة تتكشف عبر ثلاث طبقات."))
    selected_note = st.radio(local("Fragrance layers", "طبقات العطر"),
        ["top", "heart", "base"], horizontal=True, key="scent_layer",
        format_func=lambda x: {"top":local("TOP NOTES", "المقدمة"),"heart":local("HEART NOTES", "القلب"),"base":local("BASE NOTES", "القاعدة")}[x])
    scent_copy = {
        "top":local("Pink pepper and warm spice open VÈR with a lively, inviting warmth.", "يفتتح الفلفل الوردي والتوابل الدافئة عطر ڤير بإحساس حيوي ودافئ."),
        "heart":local("Elegant floral notes create a soft, refined heart.", "تمنح النفحات الزهرية الأنيقة قلب العطر طابعاً ناعماً وراقياً."),
        "base":local("Rich woods, leather, amber and musk leave a deep, lasting impression.", "تترك الأخشاب الغنية والجلد والعنبر والمسك أثراً عميقاً ومميزاً.")
    }
    scent_titles = {
        "top":local("Pink Pepper · Warm Spice", "الفلفل الوردي · التوابل الدافئة"),
        "heart":local("Elegant Florals", "نفحات زهرية أنيقة"),
        "base":local("Woods · Leather · Amber · Musk", "الأخشاب · الجلد · العنبر · المسك")
    }
    # Each fragrance layer has its own editorial photo once the assets are uploaded.
    scent_files = {"top": "scent_top.png", "heart": "scent_heart.png", "base": "scent_base.png"}
    selected_file = scent_files[selected_note]
    photo_src = img_data(selected_file) if (BASE / selected_file).exists() else (img_data("notes.jpg.png") if notes_image else perfume)
    st.markdown(
        '<div style="border:1px solid #d5b98e;background:#fff8ef;border-radius:9px;'
        'padding:16px;margin:14px 0 24px;box-shadow:0 8px 28px #75552b12">'
        '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,250px),1fr));'
        'gap:22px;align-items:center">'
        '<img src="' + photo_src + '" alt="' + html.escape(scent_titles[selected_note],quote=True) +
        '" style="display:block;width:100%;height:auto;aspect-ratio:3/2;object-fit:cover;border-radius:7px">'
        '<div style="padding:12px;text-align:center">'
        '<div style="font-family:Georgia,serif;color:#a17a44;letter-spacing:.16em;font-size:12px;margin-bottom:16px">'
        + html.escape(selected_note.upper() + " NOTES") + '</div>'
        '<div style="font-family:Georgia,serif;color:#67452d;font-size:clamp(20px,4vw,29px);margin-bottom:18px">'
        + html.escape(scent_titles[selected_note]) + '</div>'
        '<div style="font-family:Georgia,serif;color:#71553d;font-size:clamp(16px,2.5vw,21px);line-height:1.7">'
        + html.escape(scent_copy[selected_note]) + '</div></div></div></div>',
        unsafe_allow_html=True)

elif nav == "payment":
    st.markdown("## " + local("PAYMENT", "الدفع"))
    oid = st.session_state.get("saved_order_id")
    base_total = st.session_state.get("order_base_total")
    if not oid or not base_total:
        st.warning(local("Submit an order first.", "يرجى إرسال الطلب أولاً."))
    else:
        st.write(local("Order number", "رقم الطلب") + ": " + oid)
        try:
            saved_payment = payment_state(oid)
            status = saved_payment["payment_status"]
        except Exception:
            st.error(local("Unable to load payment status. Please try again.", "تعذر تحميل حالة الدفع. يرجى المحاولة مرة أخرى."))
            st.stop()
        if status == "awaiting_verification":
            method = st.radio(local("Choose payment method", "اختر طريقة الدفع"), ["ziina", "cod"],
                format_func=lambda x: local("Ziina online payment", "زينة - دفع إلكتروني") if x == "ziina" else local("Cash on delivery (+ AED 5)", "الدفع عند الاستلام (+٥ دراهم)"))
            payable = base_total + (5 if method == "cod" else 0)
            st.markdown("### " + local("Total", "الإجمالي") + ": AED " + str(payable))
            st.caption(local("After confirmation, your payment method cannot be changed for this order.", "بعد التأكيد لا يمكن تغيير طريقة الدفع لنفس الطلب."))
            if st.button(local("CONFIRM PAYMENT METHOD", "تأكيد طريقة الدفع"), use_container_width=True):
                try:
                    choose_payment(oid, method, base_total)
                    st.rerun()
                except ValueError as exc:
                    st.error(local("Payment method could not be selected: ", "تعذر اختيار طريقة الدفع: ") + str(exc))
                except Exception as exc:
                    import urllib.error
                    if isinstance(exc, urllib.error.HTTPError):
                        st.error(local("Payment setup error (HTTP ", "خطأ في حفظ الدفع (HTTP ") + str(exc.code) + "). " + local("Please contact the store.", "يرجى التواصل مع المتجر."))
                    else:
                        st.error(local("Could not reach the payment database. Please retry.", "تعذر الاتصال بقاعدة بيانات الدفع. يرجى المحاولة مرة أخرى."))
        elif status == "cod_pending":
            st.markdown("### " + local("Cash on delivery", "الدفع عند الاستلام") + " — AED " + str(saved_payment["total"]))
            render_payment_thank_you(proof_received=False, cod_received=True)
            st.write(local("Order number", "رقم الطلب") + ": " + oid)
        elif status == "instagram_pending":
            st.info(local("Existing Instagram transfer order. Contact us to complete it.", "هذا طلب تحويل سابق عبر الإنستغرام. يرجى التواصل معنا لاستكماله."))
            st.link_button(local("CONTACT ON INSTAGRAM", "التواصل عبر الإنستغرام"), "https://ig.me/m/houseofver_", use_container_width=True)
        elif status == "ziina_pending":
            st.markdown("### " + local("Ziina payment", "الدفع عبر زينة") + " — AED " + str(saved_payment["total"]))
            if st.session_state.get("proof_uploaded_for") == oid:
                render_payment_thank_you(proof_received=True)
                st.write(local("Order number", "رقم الطلب") + ": " + oid)
            else:
                links = {270:"https://pay.ziina.com/Sulaiman97/XGrEI3duJ?source=app",290:"https://pay.ziina.com/Sulaiman97/kjDR_i_KW?source=app"}
                if base_total in links:
                    st.link_button(local("STEP 1 — OPEN ZIINA PAYMENT LINK", "الخطوة ١ — فتح رابط الدفع في زينة"), links[base_total], use_container_width=True)
                    st.caption(local("Check the recipient and exact amount before paying. After visiting Ziina, return to this page.", "يرجى التأكد من المستلم والمبلغ الصحيح قبل الدفع، ثم العودة إلى هذه الصفحة."))
                    if st.session_state.get("ziina_returned_order") != oid:
                        if st.button(local("I OPENED ZIINA AND RETURNED", "فتحت رابط زينة ورجعت للموقع"), use_container_width=True):
                            st.session_state.ziina_returned_order = oid
                            st.rerun()
                        st.info(local("Step 2 — After opening Ziina, return here and select the button above to enable the screenshot upload.", "الخطوة ٢ — بعد فتح رابط زينة، يرجى العودة والضغط على الزر أعلاه لإظهار رفع الصورة."))
                    else:
                        st.markdown("#### " + local("STEP 2 — UPLOAD PAYMENT SCREENSHOT", "الخطوة ٢ — رفع صورة إثبات الدفع"))
                        with st.form("payment_proof_form"):
                            proof = st.file_uploader(local("Payment screenshot (required)", "صورة الدفع (إجبارية)"), type=["png","jpg","jpeg"])
                            submitted = st.form_submit_button(local("SUBMIT PAYMENT PROOF", "إرسال إثبات الدفع"))
                        if submitted:
                            try:
                                upload_payment_proof(oid, proof)
                                st.session_state.proof_uploaded_for = oid
                                st.rerun()
                            except ValueError as exc:
                                st.error(str(exc))
                            except Exception:
                                st.error(local("Could not upload screenshot. Please retry.", "تعذر رفع الصورة. يرجى المحاولة مرة أخرى."))
                else:
                    st.warning(local("Contact us on Instagram for the correct payment link.", "يرجى التواصل معنا عبر إنستغرام للحصول على رابط الدفع الصحيح."))
        else:
            st.info(local("This order is already being processed. Contact the store for assistance.", "هذا الطلب قيد المعالجة. يرجى التواصل معنا للمساعدة."))

else:
    st.markdown(f'<div class="section-title">{local("YOUR SHOPPING BAG", "سلة التسوق")}</div>', unsafe_allow_html=True)
    if st.session_state.cart_qty == 0:
        st.markdown(f'<div style="background:#fff9ef!important;color:#60482e!important;border:1px solid #d7b98d;border-left:4px solid #a8782c;border-radius:6px;padding:18px 20px;margin:12px 0 16px;font-size:17px">{local("Your bag is empty.", "سلتك فارغة.")}</div>', unsafe_allow_html=True)
        if st.button(local("Shop VÈR", "تسوق ڤير"), use_container_width=True):
            st.session_state.page = "shop"
            st.rerun()
    else:
        st.markdown(
            '<div style="max-width:260px;margin:8px auto 22px;'
            'border:1px solid #d6b98c;border-radius:8px;overflow:hidden;'
            'background:#fff8ef;box-shadow:0 6px 24px rgba(100,72,45,.07)">'
            f'<img src="{perfume}" alt="VÈR Eau de Parfum 100 ml" '
            'style="width:100%;height:auto;display:block;object-fit:contain">'
            '</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div style="text-align:center;color:#8f692f;font-family:Georgia,serif;'
            f'font-size:21px;margin-bottom:18px">{local("VÈR Eau de Parfum · 100 ml", "عطر ڤير · ١٠٠ مل")}</div>',
            unsafe_allow_html=True)
        cart_qty = st.number_input(local("VÈR Eau de Parfum · 100 ml — Quantity", "عطر ڤير · ١٠٠ مل — الكمية"), min_value=0, max_value=20, step=1, key="cart_qty")
        if st.session_state.get("customer_token") and st.session_state.get("last_synced_cart") != cart_qty:
            try:
                auth.save_profile(st.session_state.customer_token,st.session_state.customer_id,cart_qty=cart_qty)
                st.session_state.last_synced_cart=cart_qty
            except Exception:
                st.warning(local("Cart could not sync to your account.", "تعذرت مزامنة السلة مع الحساب."))
        if cart_qty == 0:
            st.session_state.page = "shop"
            st.rerun()
        if not st.session_state.get("customer_token"):
            st.markdown(
                '<div style="background:#fff8ef;color:#64482f;border:1px solid #d7b98d;'
                'border-radius:9px;padding:20px;margin:18px 0">'
                '<div style="font-family:Georgia,serif;font-size:22px;color:#8d672f;margin-bottom:8px">'
                +html.escape(local("HOW WOULD YOU LIKE TO CHECK OUT?","كيف تفضل إكمال الطلب؟"))+'</div>'
                '<div style="font-size:15px;line-height:1.6">'
                +html.escape(local("Sign in to save your details and orders, or continue without an account.", "سجّل الدخول لحفظ بياناتك وطلباتك، أو أكمل الطلب من دون حساب."))+
                '</div></div>',unsafe_allow_html=True)
            login_col,guest_col=st.columns(2,gap="small")
            with login_col:
                if st.button(local("SIGN IN / CREATE ACCOUNT","تسجيل الدخول / إنشاء حساب"),key="cart_login",use_container_width=True):
                    st.session_state.page="account"
                    st.rerun()
            with guest_col:
                if st.button(local("CONTINUE AS GUEST","المتابعة كضيف"),key="cart_guest",use_container_width=True):
                    st.session_state.guest_checkout=True
                    st.rerun()
            if not st.session_state.get("guest_checkout"):
                st.caption(local("Select an option above to continue to delivery details.", "اختر إحدى الطريقتين للمتابعة إلى بيانات التوصيل."))
                st.stop()
            st.caption(local("Guest checkout — your order will not be saved to a customer account.", "الطلب كضيف — لن يُحفظ الطلب في حساب عميل."))
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
            saved_profile=st.session_state.get("customer_profile",{}) if st.session_state.get("customer_token") else {}
            customer = st.text_input(local("Full name", "الاسم الكامل"), value=saved_profile.get("full_name") or "", max_chars=120)
            phone = st.text_input(local("UAE mobile number", "رقم الهاتف الإماراتي"), value=saved_profile.get("phone") or "", max_chars=30)
            email = st.text_input(local("Email address", "البريد الإلكتروني"), value=st.session_state.get("customer_email",""), max_chars=254)
            instagram = st.text_input(local("Instagram username (required)", "حساب إنستغرام (إجباري)"), value=saved_profile.get("instagram") or "", max_chars=60)
            address = st.text_area(local("Delivery address and area", "العنوان والمنطقة"), value=saved_profile.get("address") or "", max_chars=500)
            st.caption(local("IMPORTANT: The full name on your order must match the name on your Ziina payment account. We use it to match payments manually.", "مهم: يجب أن يطابق الاسم في الطلب الاسم المسجل في حساب زينة المستخدم للدفع حتى نتمكن من مطابقة الدفعة يدوياً."))
            confirmed = st.form_submit_button(local("SUBMIT ORDER REQUEST", "إرسال الطلب"), use_container_width=True)
        fingerprint = (customer.strip(), phone.strip(), email.strip(), instagram.strip(), address.strip(), emirate, area, cart_qty, total)
        if confirmed and st.session_state.get("saved_order_fingerprint") != fingerprint:
            try:
                with st.spinner(local("Saving order...", "جارٍ تسجيل الطلب...")):
                    oid = save_order(customer, phone, email, instagram, address, emirate, area, cart_qty, PRICE, delivery, customer_token=st.session_state.get("customer_token"))
                st.session_state.saved_order_fingerprint = fingerprint
                st.session_state.saved_order_id = oid
            except ValueError as exc:
                st.error(str(exc))
            except Exception:
                st.error(local("Could not save your order. Please try again or contact us on Instagram.", "تعذر تسجيل الطلب. يرجى المحاولة مجدداً أو التواصل عبر إنستغرام."))
        if st.session_state.get("saved_order_fingerprint") == fingerprint:
            st.session_state.order_base_total = total
            st.session_state.page = "payment"
            st.rerun()
        else:
            st.caption(local("After submitting, choose your payment method.", "عقب إرسال الطلب اختر طريقة الدفع."))

        st.markdown(f'<div class="fine"></div><div class="copy">{local("Need help? Contact @houseofver_ on Instagram.", "للمساعدة تواصل معنا عبر إنستغرام @houseofver_")}</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">HOUSE OF VÈR · THE ESSENCE OF PRESENCE</div>', unsafe_allow_html=True)
