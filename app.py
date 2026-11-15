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
col1,col2=st.columns([4,1])
with col2:
    st.selectbox('Language / اللغة', ['English','العربية'],key='lang',label_visibility='visible')
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


st.markdown(f'<div class="brand-shell" style="min-height:0;padding:0;border:none;background:transparent"><img src="{art}" alt="HOUSE OF VÈR" style="display:block;width:100%;height:auto;border:double 5px #b8893b"></div>', unsafe_allow_html=True)
st.markdown(f'<div class="bottle"><img src="{perfume}" alt="VÈR perfume bottle" /></div>',unsafe_allow_html=True)
st.markdown(f'<div class="price">AED 225</div><div class="muted">{t("size")}</div>',unsafe_allow_html=True)
st.markdown(f'<a class="order" href="https://ig.me/m/houseofver_" target="_blank" rel="noopener noreferrer">{t("order")} ↗</a><a class="secondary" href="https://www.instagram.com/houseofver_/" target="_blank" rel="noopener noreferrer">{t("profile")}</a>',unsafe_allow_html=True)
st.markdown(f'<div class="fine"></div><div class="section-title">{t("about_title")}</div><div class="copy {'rtl' if ar else ''}">{t("about")}</div>',unsafe_allow_html=True)
st.markdown(f'<div class="fine"></div><div class="section-title">{t("delivery_title")}</div><div class="copy {'rtl' if ar else ''}">{t("delivery")}</div>',unsafe_allow_html=True)
st.markdown(f'<div class="fine"></div><div class="section-title">{t("contact")}</div><a class="order" href="https://ig.me/m/houseofver_" target="_blank" rel="noopener noreferrer">{t("order")} ↗</a><a class="secondary" href="https://www.instagram.com/houseofver_/" target="_blank" rel="noopener noreferrer">@houseofver_</a><p class="muted">{t("notice")}</p><div class="footer">HOUSE OF VÈR · THE ESSENCE OF PRESENCE</div>',unsafe_allow_html=True)
