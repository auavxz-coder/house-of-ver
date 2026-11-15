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



import html

PRICE = 240
DELIVERY = 30
EMIRATES = ["Dubai", "Ras Al Khaimah", "Sharjah", "Ajman", "Abu Dhabi", "Umm Al Quwain", "Fujairah"]
WESTERN = ["المرفأ", "الرويس", "الظنة", "السلع", "غياثي", "بدع المطاوعة", "بينونة", "مدينة زايد", "بدع زايد", "مرابع الظفرة", "ليوا"]
ALAIN_30 = ["ناهل", "الساد"]
ALAIN_50 = ["سويحان", "رماح", "الخزنة", "أبو سمرة", "الختم", "الظاهرة", "العراد", "بوكريه", "الوقن", "القوع"]
OTHER_30 = ["وادي الحلو", "شوكة", "كدرا", "السيجي", "وادي اصفني", "وادي اصفي", "وادي ممدوح", "مزيرع", "مصفوت", "مكن", "صعير", "المنيعي", "الحويلات", "وادي العجيلي", "رافاق", "جيما"]
def delivery_options(emirate):
    if emirate == "Abu Dhabi":
        return ["Standard area / منطقة عادية"] + ["Western Region / المنطقة الغربية — " + x for x in WESTERN] + ["Al Ain / العين — " + x for x in ALAIN_30 + ALAIN_50]
    if emirate in ("Sharjah", "Ras Al Khaimah", "Fujairah", "Ajman", "Dubai"):
        return ["Standard area / منطقة عادية"] + ["Special area / منطقة خاصة — " + x for x in OTHER_30]
    return ["Standard area / منطقة عادية"]

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
</style>""", unsafe_allow_html=True)

if "cart_qty" not in st.session_state:
    st.session_state.cart_qty = 0
if "page" not in st.session_state:
    st.session_state.page = "shop"

nav = st.radio(local("Explore", "تصفح"), ["shop", "cart"], format_func=lambda v: (local("Perfume", "العطر") if v == "shop" else local("Cart & payment", "السلة والدفع") + f" ({st.session_state.cart_qty})"), horizontal=True, label_visibility="collapsed", index=0 if st.session_state.page == "shop" else 1)
st.session_state.page = nav

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
else:
    st.markdown(f'<div class="section-title">{local("YOUR SHOPPING BAG", "سلة التسوق")}</div>', unsafe_allow_html=True)
    if st.session_state.cart_qty == 0:
        st.info(local("Your bag is empty.", "سلتك فارغة."))
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
        st.info(local(timing_en, timing_ar))
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
