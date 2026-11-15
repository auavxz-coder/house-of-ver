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
.thank-star{font-size:72px;line-height:1;color:#c18b35}
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

def render_payment_thank_you(preview=False):
    """Display branded confirmation; live orders require verified payment first."""
    label = local("DESIGN PREVIEW — NOT A PAYMENT CONFIRMATION", "معاينة التصميم — ليست تأكيداً للدفع") if preview else local("PAYMENT CONFIRMED", "تم تأكيد الدفع")
    st.markdown(f'<div class="thank-preview">{html.escape(label)}</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="thank-card">
      <div class="thank-star">✳</div>
      <div class="thank-brand">HOUSE OF VÈR</div>
      <div class="thank-tagline">THE ESSENCE OF PRESENCE</div>
      <div class="thank-rule"></div>
      <div class="thank-script">Thank You</div>
      <div class="thank-offer">Get 5% off your next order<br>using code: <strong>UAE219</strong></div>
      <div class="thank-social">Follow Us on Instagram<br><a href="https://www.instagram.com/houseofver_/" target="_blank" rel="noopener noreferrer">@houseofver_</a></div>
      <div class="thank-clouds" aria-hidden="true"><span class="cloud cloud-one"></span><span class="cloud cloud-two"></span><span class="cloud cloud-three"></span></div>
    </div>
    """, unsafe_allow_html=True)
    st.caption(local("The discount code is displayed as provided; automatic discount redemption is not configured.", "يظهر رمز الخصم كما تم تقديمه، لكن تطبيق الخصم تلقائياً غير مفعّل."))

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
if ar:
    st.markdown('<style>.stApp .st-key-lang_ar button{border-bottom:1px solid #986821!important}</style>',unsafe_allow_html=True)
else:
    st.markdown('<style>.stApp .st-key-lang_en button{border-bottom:1px solid #986821!important}</style>',unsafe_allow_html=True)
nav = st.session_state.page

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
elif nav == "shop":
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
                st.markdown(f'<div class="checkout-notice">{html.escape(local("Order details reviewed. Payment is not yet confirmed.", "تمت مراجعة بيانات الطلب. الدفع غير مؤكد بعد."))}</div>', unsafe_allow_html=True)
                st.markdown(f"**{local('Payable amount', 'المبلغ المطلوب')}: AED {total}**")
                # Only show a Ziina payment link if its exact amount has been configured and checked.
                try:
                    ziina_links = st.secrets.get("ziina_links", {})
                except Exception:
                    ziina_links = {}
                link = ziina_links.get(str(total), "") if ziina_links else ""
                if isinstance(link, str) and link.startswith("https://pay.ziina.com/"):
                    st.link_button(local("PAY WITH ZIINA", "ادفع عبر زينة"), link, use_container_width=True)
                    st.markdown(f'<div class="checkout-notice">{html.escape(local("Pay only if Ziina displays exactly AED " + str(total) + ". A payment link does not automatically confirm your order on this site.", "ادفع فقط إذا ظهر مبلغ " + str(total) + " درهماً في زينة. لا يؤكد رابط الدفع الطلب تلقائياً في الموقع."))}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="checkout-notice">{html.escape(local("Ziina payments are not connected yet. The business owner must add a verified Ziina payment link for this exact total.", "الدفع عبر زينة غير متصل بعد. يجب إضافة رابط دفع موثّق لهذا المبلغ تحديداً."))}</div>', unsafe_allow_html=True)
                st.markdown(f'<a class="order" href="https://ig.me/m/houseofver_" target="_blank" rel="noopener noreferrer">{local("CONTACT US ON INSTAGRAM", "تواصل معنا عبر إنستغرام")}</a>', unsafe_allow_html=True)
                st.caption(local("No order is placed and no personal details are sent by this form. Confirm the order with HOUSE OF VÈR on Instagram.", "لا يتم إرسال بياناتك أو تسجيل طلب تلقائياً من هذا النموذج. أكّد الطلب مع هاوس أوف ڤير عبر إنستغرام."))
            else:
                st.session_state.checkout_ready = False
        st.markdown(f'<div class="fine"></div><div class="copy">{local("Need help? Contact @houseofver_ on Instagram.", "للمساعدة تواصل معنا عبر إنستغرام @houseofver_")}</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">HOUSE OF VÈR · THE ESSENCE OF PRESENCE</div>', unsafe_allow_html=True)
