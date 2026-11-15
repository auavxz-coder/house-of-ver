import base64
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="HOUSE OF VÈR | The Essence of Presence", page_icon="✦", layout="wide", initial_sidebar_state="collapsed")
BASE = Path(__file__).parent

def image_uri(filename):
    p = BASE / filename
    if not p.exists():
        return None
    mime = "image/jpeg" if p.suffix.lower() in (".jpg", ".jpeg") else "image/png"
    return f"data:{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"

if "language" not in st.session_state:
    st.session_state.language = "English"
st.selectbox("Language / اللغة", ["English", "العربية"], key="language")
ar = st.session_state.language == "العربية"

def tr(en, arabic):
    return arabic if ar else en

art = image_uri("brand_art.png")
perfume = image_uri("perfume.jpg")
notes = image_uri("notes.jpg") or image_uri("notes.png")
direction = "rtl" if ar else "ltr"
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&family=Cormorant+Garamond:wght@400;500;600&family=DM+Sans:wght@400;500&display=swap');
:root{--ink:#493425;--gold:#9b702f;--cream:#fff6eb}
html,body,[class*="css"]{font-family:'DM Sans',sans-serif}
.stApp{background:#fff6eb;color:var(--ink)}
.block-container{max-width:1080px;padding:1.3rem 1.4rem 4rem}
header[data-testid="stHeader"]{background:transparent}
#MainMenu,footer{visibility:hidden}
div[data-testid="stSelectbox"]{max-width:190px;margin-left:auto}
div[data-testid="stSelectbox"] label{color:#8a6538}
.hero{position:relative;overflow:hidden;border:1px solid #b48b50;background:#fef0df;box-shadow:0 12px 36px #6d49231a}
.hero img{display:block;width:100%;height:340px;object-fit:cover;object-position:center 19%}
.hero-caption{text-align:center;margin:18px auto 10px;color:#9b702f;letter-spacing:.22em;font-size:12px}
.heading{font-family:'Cormorant Garamond','Amiri',serif;text-align:center;font-size:clamp(38px,5vw,64px);font-weight:500;color:#8c622b;line-height:1.12;margin:34px 0 10px}
.sub{text-align:center;color:#665244;font-size:clamp(15px,2vw,19px);line-height:1.7;margin:0 auto 24px;max-width:600px}
.product{display:flex;align-items:center;gap:42px;max-width:880px;margin:35px auto 10px}
.product-image{flex:0 0 45%;min-width:0}
.product-image img{width:100%;display:block;max-height:540px;object-fit:contain;border-radius:4px}
.product-info{flex:1;text-align:center}
.product-name{font-family:'Cormorant Garamond','Amiri',serif;font-size:clamp(36px,5vw,60px);color:#8c622b;line-height:1.1}
.price{font-family:'Cormorant Garamond',serif;font-size:36px;color:#8c622b;margin:14px 0 0}
.small{font-size:13px;color:#796751;line-height:1.7}
.cta{display:block;max-width:360px;margin:22px auto 12px;padding:17px 22px;background:#8d632e;color:#fffaf3!important;text-align:center;text-decoration:none!important;letter-spacing:.1em;font-weight:500;font-size:13px}
.cta:hover{background:#684720}
.backup{display:block;text-align:center;color:#8d632e!important;font-size:13px;margin-bottom:18px}
.rule{border:0;border-top:1px solid #d8bd94;max-width:740px;margin:48px auto 20px}
.notes-image{display:block;max-width:650px;width:100%;margin:20px auto;border-radius:3px}
.notes-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;max-width:900px;margin:24px auto}
.note{background:#fffaf4;border:1px solid #e2cfb1;text-align:center;padding:22px 12px;min-width:0}
.note strong{font-size:12px;letter-spacing:.2em;color:#986c30}
.note p{font-family:'Cormorant Garamond','Amiri',serif;font-size:clamp(19px,2.3vw,25px);line-height:1.35;margin:10px 0 0}
[dir="rtl"] .note p{font-family:'Amiri',serif}
@media(max-width:700px){
.block-container{padding:1rem .8rem 3rem}
.hero img{height:185px;object-position:center 16%}
.hero-caption{font-size:10px;letter-spacing:.13em}
.heading{font-size:39px;margin:24px 0 8px}
.product{display:block;margin:16px auto 0}
.product-image{max-width:340px;margin:auto}
.product-image img{max-height:380px}
.product-info{padding:0 10px}
.product-name{font-size:43px}
.price{font-size:32px}
.cta{max-width:none;width:100%;box-sizing:border-box}
.notes-grid{grid-template-columns:1fr;gap:10px}
.note{padding:15px}
.note p{font-size:23px}
.rule{margin:35px auto 18px}
.notes-image{max-height:420px;object-fit:cover}
}
</style>""", unsafe_allow_html=True)

if art:
    st.markdown(f'<div class="hero"><img src="{art}" alt="HOUSE OF VÈR gold cloud artwork"></div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="heading">HOUSE OF VÈR</div>', unsafe_allow_html=True)
st.markdown(f'<div class="hero-caption">{tr("THE ESSENCE OF PRESENCE", "جوهر الحضور")}</div>', unsafe_allow_html=True)

picture = f'<img src="{perfume}" alt="VÈR perfume bottle">' if perfume else ''
st.markdown(f"""
<div class="product" dir="{direction}">
 <div class="product-image">{picture}</div>
 <div class="product-info">
  <div class="product-name">VÈR</div>
  <div class="sub">{tr("EAU DE PARFUM", "عطر ڤير")}</div>
  <div class="price">AED 225</div>
  <p class="small">{tr("100 ml · Delivery across the UAE", "١٠٠ مل · التوصيل داخل الإمارات")}</p>
  <p class="small">{tr("A presence that lingers.", "حضور يترك أثره.")}</p>
  <a class="cta" href="https://ig.me/m/houseofver_" target="_blank" rel="noopener noreferrer">{tr("ORDER VIA INSTAGRAM ↗", "اطلب عبر إنستغرام ↗")}</a>
  <a class="backup" href="https://www.instagram.com/houseofver_/" target="_blank" rel="noopener noreferrer">@houseofver_</a>
 </div>
</div>
""", unsafe_allow_html=True)

st.markdown(f'<hr class="rule"><div class="heading">{tr("THE FRAGRANCE NOTES", "نوتات العطر")}</div><p class="sub">{tr("From a vibrant opening to a lasting, warm signature.", "من بداية نابضة إلى بصمة دافئة تدوم.")}</p>', unsafe_allow_html=True)
if notes:
    st.markdown(f'<img class="notes-image" src="{notes}" alt="Pink pepper, florals, woods, leather and amber fragrance notes">', unsafe_allow_html=True)
st.markdown(f"""
<div class="notes-grid" dir="{direction}">
 <div class="note"><strong>{tr("TOP NOTES", "النوتات العليا")}</strong><p>{tr("Pink Pepper · Warm Spice", "الفلفل الوردي · التوابل الدافئة")}</p></div>
 <div class="note"><strong>{tr("HEART NOTES", "قلب العطر")}</strong><p>{tr("Elegant Florals", "نفحات زهرية أنيقة")}</p></div>
 <div class="note"><strong>{tr("BASE NOTES", "النوتات الأساسية")}</strong><p>{tr("Rich Woods · Leather · Amber · Musk", "الأخشاب الغنية · الجلد · العنبر · المسك")}</p></div>
</div>
""", unsafe_allow_html=True)

st.markdown(f'<hr class="rule"><div class="heading">{tr("THE HOUSE", "عن الدار")}</div><p class="sub">{tr("HOUSE OF VÈR is built around the essence of presence — a fragrance made to be remembered.", "تتمحور هوية هاوس أوف ڤير حول جوهر الحضور، عطر يبقى في الذاكرة.")}</p>', unsafe_allow_html=True)
st.markdown(f'<hr class="rule"><div class="heading">{tr("UAE DELIVERY", "التوصيل داخل الإمارات")}</div><p class="sub">{tr("Orders are arranged through Instagram messages. Delivery timing and fees are confirmed before your order is finalized.", "تُنسق الطلبات عبر رسائل إنستغرام، ويتم تأكيد موعد التوصيل ورسومه قبل إتمام الطلب.")}</p><a class="cta" href="https://ig.me/m/houseofver_" target="_blank" rel="noopener noreferrer">{tr("ORDER VIA INSTAGRAM ↗", "اطلب عبر إنستغرام ↗")}</a><p class="small" style="text-align:center">{tr("No card payments are taken on this website.", "لا يتم تحصيل مدفوعات بالبطاقة عبر هذا الموقع.")}</p>', unsafe_allow_html=True)
