import streamlit as st
from datetime import datetime

st.set_page_config(page_title="FOOD BUS", page_icon="🚌", layout="wide")

# ---------- FOOD BUS LOOK & FEEL ----------
st.markdown("""
<style>
.stApp { background: #e8f5e9; }
.block-container { max-width: 1200px; padding-top: 1.4rem; }
h1, h2, h3 { color: #176b3a; }
.food-title { color: #e83e8c !important; font-weight: 800; text-align: center; }
.food-price { color: #111; font-weight: 800; font-size: 1.15rem; }
div.stButton > button { background:#168342; color:white; border:0; border-radius:12px; font-weight:700; min-height:2.55rem; }
div.stButton > button:hover { background:#0e6330; color:white; border:0; }
div[data-testid="stVerticalBlockBorderWrapper"] {
 background:#fff; border-radius:18px; border:3px solid #d8b36a; padding:14px;
 box-shadow:0 3px 12px rgba(30,80,45,.07);
}
div[data-testid="stTextInput"] input { border-radius:12px; }
.hero {
  position:relative;
  display:flex;
  flex-direction:column;
  align-items:center;
  justify-content:center;
  box-sizing:border-box;
  width:100%;
  min-height:168px;
  overflow:visible;
  background:linear-gradient(110deg,#0f5b32 0%,#21834a 55%,#36a765 100%);
  padding:34px 22px 30px;
  border:3px double #e7c779;
  outline:1px solid rgba(255,255,255,.55);
  outline-offset:-9px;
  border-radius:20px;
  color:white;
  margin:0 0 18px 0;
  box-shadow:0 5px 18px rgba(13,75,40,.16);
}
.hero::before, .hero::after {
  position:absolute;
  color:#f5d98f;
  font-size:23px;
  line-height:1;
  pointer-events:none;
}
.hero::before { content:"❖  ✦  ❖"; top:12px; left:20px; letter-spacing:5px; }
.hero::after { content:"❖  ✦  ❖"; bottom:12px; right:20px; letter-spacing:5px; }
.hero h1 {
  color:#fff !important;
  display:block;
  width:100%;
  max-width:100%;
  box-sizing:border-box;
  margin:8px 0 6px 0 !important;
  padding:0 4px;
  font-size:clamp(1.9rem,4vw,3rem) !important;
  line-height:1.15 !important;
  font-weight:900 !important;
  letter-spacing:1.5px;
  white-space:normal !important;
  overflow:visible !important;
  overflow-wrap:normal;
  text-align:center;
  text-shadow:0 2px 3px rgba(0,0,0,.18);
}
.hero p {
  color:#f7f2df !important;
  margin:0 0 8px 0 !important;
  text-align:center;
  font-size:1rem;
  letter-spacing:.3px;
}
@media (max-width: 480px) {
  .hero { min-height:132px; padding:25px 14px; border-radius:16px; }
  .hero::before { top:9px; left:12px; font-size:17px; }
  .hero::after { bottom:9px; right:12px; font-size:17px; }
  .hero h1 { font-size:clamp(1.8rem,9vw,2.5rem) !important; letter-spacing:1px; }
  .hero p { font-size:.85rem; }
}
.ad-strip { overflow:hidden; white-space:nowrap; background:#fff4d6; border:2px solid #bd8731; border-radius:14px; padding:11px 0; margin:0 0 20px 0; color:#155b34; font-weight:800; }
.ad-strip span { display:inline-block; padding-left:100%; animation:adscroll 27s linear infinite; }
@keyframes adscroll { from { transform:translateX(0); } to { transform:translateX(-100%); } }
.search-hint { color:#176b3a; font-weight:800; margin:4px 0 8px 2px; }
.search-rotate { display:inline-flex; flex-direction:column; vertical-align:bottom; height:1.5em; overflow:hidden; color:#e83e8c; }
.search-rotate span { display:block; height:1.5em; line-height:1.5em; }
.food-photo-slot { width:154px; height:154px; margin:12px auto 18px; border-radius:50%; background:radial-gradient(circle,#fffaf0 0 58%,#f3d89b 59% 64%,#176b3a 65% 69%,#fff 70%); display:flex; align-items:center; justify-content:center; font-size:4rem; box-shadow:0 4px 14px rgba(0,0,0,.12); }
/* Compact, horizontally scrollable food categories */
.st-key-category_filter { margin:4px 0 14px 0; }
.st-key-category_filter [data-testid="stHorizontalBlock"] {
  display:flex !important;
  flex-wrap:nowrap !important;
  gap:7px !important;
  overflow-x:auto !important;
  overflow-y:hidden !important;
  padding:3px 2px 9px 2px !important;
  scrollbar-width:thin;
}
.st-key-category_filter [data-testid="column"] {
  flex:0 0 auto !important;
  width:auto !important;
  min-width:max-content !important;
}
.st-key-category_filter div.stButton > button {
  min-height:36px !important;
  padding:5px 13px !important;
  border-radius:18px !important;
  white-space:nowrap !important;
  font-size:13px !important;
}
/* Single-line Zomato-inspired category rail */
.st-key-menu_category_radio { width:100%; margin:6px 0 16px !important; }
.st-key-menu_category_radio [role="radiogroup"] {
  display:flex !important;
  flex-wrap:nowrap !important;
  align-items:center !important;
  justify-content:flex-start !important;
  gap:8px !important;
  width:100% !important;
  overflow-x:auto !important;
  overflow-y:hidden !important;
  white-space:nowrap !important;
  padding:5px 2px 12px !important;
  scrollbar-width:thin;
}
.st-key-menu_category_radio [role="radiogroup"] > label {
  flex:0 0 auto !important;
  width:auto !important;
  min-width:max-content !important;
  white-space:nowrap !important;
  display:flex !important;
  align-items:center !important;
  padding:7px 15px !important;
  margin:0 !important;
  border:1px solid #d8e3dc !important;
  border-radius:22px !important;
  background:#fff !important;
  color:#26352c !important;
  font-size:13px !important;
  line-height:1.2 !important;
}
.st-key-menu_category_radio [role="radiogroup"] > label p {
  white-space:nowrap !important;
  margin:0 !important;
}
.st-key-menu_category_radio [role="radiogroup"] > label:has(input:checked) {
  background:#176b3a !important;
  border-color:#176b3a !important;
  color:#fff !important;
}
.st-key-menu_category_radio [role="radiogroup"] > label:has(input:checked) p {
  color:#fff !important;
}
/* Tighter food cards and image slots */
.st-key-food_grid div[data-testid="stVerticalBlockBorderWrapper"] {
  padding:9px !important;
  border-width:2px !important;
}
.st-key-food_grid .food-photo-slot {
  width:112px;
  height:112px;
  margin:5px auto 10px;
  font-size:3rem;
}
.st-key-food_grid .food-title { font-size:1.05rem; margin:4px 0 !important; }
.st-key-food_grid .food-price { font-size:1rem; }
.st-key-food_grid div.stButton > button { min-height:2.2rem; padding:5px 8px; }
@media (max-width: 768px) {
  .st-key-food_grid [data-testid="stHorizontalBlock"] {
    display:grid !important;
    grid-template-columns:repeat(2,minmax(0,1fr)) !important;
    gap:9px !important;
  }
  .st-key-food_grid [data-testid="column"] { width:auto !important; min-width:0 !important; }
  .st-key-food_grid .food-photo-slot { width:92px; height:92px; font-size:2.5rem; }
  .st-key-food_grid .food-title { font-size:.95rem; }
  .st-key-food_grid div[data-testid="stVerticalBlockBorderWrapper"] { padding:7px !important; }
}

@media (max-width: 768px) {
  section[data-testid="stSidebar"] { display: none !important; }
  div[data-testid="stRadio"] {
    position: fixed !important;
    left: 0 !important;
    right: 0 !important;
    bottom: 0 !important;
    z-index: 999999 !important;
    background: #ffffff !important;
    padding: 9px 5px calc(9px + env(safe-area-inset-bottom)) 5px !important;
    border-top: 2px solid #d8b36a !important;
    box-shadow: 0 -3px 14px rgba(0,0,0,.12) !important;
  }
  div[data-testid="stRadio"] > label { display: none !important; }
  div[data-testid="stRadio"] div[role="radiogroup"] {
    display: flex !important;
    flex-wrap: nowrap !important;
    justify-content: space-around !important;
    gap: 2px !important;
  }
  div[data-testid="stRadio"] div[role="radiogroup"] label {
    flex: 1 1 20% !important;
    justify-content: center !important;
    padding: 5px 1px !important;
    font-size: 10px !important;
    text-align: center !important;
  }
  div[data-testid="stRadio"] div[role="radiogroup"] label p {
    font-size: 10px !important;
    white-space: normal !important;
    line-height: 1.15 !important;
  }
  .block-container { padding-bottom: 100px !important; }
}

/* Clean, spacious navigation tabs */
div[data-testid="stRadio"] {
  background: #ffffff !important;
  border: 1px solid #c9ddcf !important;
  border-radius: 16px !important;
  padding: 9px !important;
  box-shadow: 0 3px 12px rgba(22, 80, 48, .08) !important;
  margin: 8px 0 18px 0 !important;
}
div[data-testid="stRadio"] > label { display: none !important; }
div[data-testid="stRadio"] div[role="radiogroup"] {
  display: flex !important;
  flex-wrap: nowrap !important;
  justify-content: space-between !important;
  gap: 8px !important;
}
div[data-testid="stRadio"] div[role="radiogroup"] label {
  flex: 1 1 20% !important;
  justify-content: center !important;
  text-align: center !important;
  min-height: 46px !important;
  padding: 10px 8px !important;
  margin: 0 !important;
  border: 1px solid #d7e6db !important;
  border-radius: 11px !important;
  background: #f6faf7 !important;
  color: #245b3b !important;
  font-size: 14px !important;
  font-weight: 700 !important;
}
div[data-testid="stRadio"] div[role="radiogroup"] label p {
  font-size: 14px !important;
  line-height: 1.2 !important;
  white-space: normal !important;
  color: inherit !important;
  font-weight: 700 !important;
}
div[data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) {
  background: #176b3a !important;
  border-color: #176b3a !important;
  color: #ffffff !important;
}
div[data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) p {
  color: #ffffff !important;
}
@media (max-width: 768px) {
  div[data-testid="stRadio"] {
    position: fixed !important;
    left: 0 !important;
    right: 0 !important;
    bottom: 0 !important;
    z-index: 999999 !important;
    border-radius: 15px 15px 0 0 !important;
    margin: 0 !important;
    padding: 8px 5px calc(8px + env(safe-area-inset-bottom)) 5px !important;
  }
  div[data-testid="stRadio"] div[role="radiogroup"] { gap: 5px !important; }
  div[data-testid="stRadio"] div[role="radiogroup"] label {
    min-height: 52px !important;
    padding: 9px 3px !important;
    font-size: 12px !important;
  }
  div[data-testid="stRadio"] div[role="radiogroup"] label p {
    font-size: 12px !important;
    line-height: 1.15 !important;
  }
  .block-container { padding-bottom: 105px !important; }
}

/* FOOD BUS compact menu rows and category chips */
.st-key-food_grid .food-photo-slot { width:76px !important; height:76px !important; margin:4px auto !important; font-size:2.1rem !important; }
.st-key-food_grid .food-title { font-size:1rem !important; font-weight:700; margin:0 0 3px !important; }
.st-key-food_grid .food-price { font-size:1rem !important; font-weight:700; margin:3px 0; }
.st-key-food_grid .food-availability { color:#18864b; font-size:11px; font-weight:650; }
.st-key-food_grid div.stButton > button { min-height:30px !important; width:auto !important; padding:3px 16px !important; font-size:12px !important; border-radius:7px !important; }
.st-key-category_filter [data-testid="stHorizontalBlock"] { display:flex !important; flex-wrap:nowrap !important; gap:6px !important; overflow-x:auto !important; padding:2px 2px 8px !important; }
.st-key-category_filter [data-testid="column"] { flex:0 0 auto !important; width:auto !important; min-width:max-content !important; }
.st-key-category_filter div.stButton > button { min-height:31px !important; padding:4px 11px !important; border-radius:16px !important; white-space:nowrap !important; font-size:12px !important; }

/* FINAL OVERRIDE: category names stay on one line and scroll horizontally */
div[data-testid="stRadio"].st-key-menu_category_radio {
  width:100% !important;
  max-width:100% !important;
  min-width:0 !important;
  overflow:hidden !important;
  padding:4px 0 8px !important;
  margin:4px 0 14px !important;
  background:transparent !important;
  border:0 !important;
  box-shadow:none !important;
}
div[data-testid="stRadio"].st-key-menu_category_radio div[role="radiogroup"] {
  display:flex !important;
  flex-direction:row !important;
  flex-wrap:nowrap !important;
  justify-content:flex-start !important;
  align-items:center !important;
  gap:8px !important;
  width:100% !important;
  max-width:100% !important;
  overflow-x:auto !important;
  overflow-y:hidden !important;
  white-space:nowrap !important;
  scrollbar-width:thin !important;
}
div[data-testid="stRadio"].st-key-menu_category_radio div[role="radiogroup"] > label {
  display:flex !important;
  flex:0 0 auto !important;
  width:max-content !important;
  min-width:max-content !important;
  max-width:none !important;
  min-height:36px !important;
  white-space:nowrap !important;
  flex-wrap:nowrap !important;
  padding:7px 14px !important;
  margin:0 !important;
  border-radius:20px !important;
}
div[data-testid="stRadio"].st-key-menu_category_radio div[role="radiogroup"] > label p {
  display:inline-block !important;
  width:max-content !important;
  min-width:max-content !important;
  white-space:nowrap !important;
  overflow:visible !important;
  word-break:keep-all !important;
  overflow-wrap:normal !important;
  line-height:1.2 !important;
}

/* CATEGORY CHIPS: override global radio/navigation styles with full-width labels */
.st-key-menu_category_radio div[data-testid="stRadio"] {
  width:100% !important;
  max-width:100% !important;
  min-width:0 !important;
  overflow:hidden !important;
  background:transparent !important;
  border:0 !important;
  box-shadow:none !important;
  padding:4px 0 10px !important;
  margin:4px 0 14px !important;
}
.st-key-menu_category_radio div[data-testid="stRadio"] div[role="radiogroup"] {
  display:flex !important;
  flex-direction:row !important;
  flex-wrap:nowrap !important;
  justify-content:flex-start !important;
  align-items:center !important;
  gap:9px !important;
  width:100% !important;
  min-width:0 !important;
  overflow-x:auto !important;
  overflow-y:hidden !important;
  white-space:nowrap !important;
  padding:4px 2px 10px !important;
}
.st-key-menu_category_radio div[data-testid="stRadio"] div[role="radiogroup"] > label {
  display:inline-flex !important;
  flex:0 0 auto !important;
  flex-grow:0 !important;
  flex-shrink:0 !important;
  width:auto !important;
  min-width:max-content !important;
  max-width:none !important;
  white-space:nowrap !important;
  word-break:normal !important;
  overflow-wrap:normal !important;
  align-items:center !important;
  justify-content:center !important;
  padding:8px 15px !important;
  margin:0 !important;
}
.st-key-menu_category_radio div[data-testid="stRadio"] div[role="radiogroup"] > label p,
.st-key-menu_category_radio div[data-testid="stRadio"] div[role="radiogroup"] > label span {
  display:inline !important;
  flex:0 0 auto !important;
  width:auto !important;
  min-width:max-content !important;
  white-space:nowrap !important;
  word-break:keep-all !important;
  overflow-wrap:normal !important;
}

/* Force category chip BUTTON TEXT itself to remain horizontal */
.st-key-category_filter {
  width:100% !important;
  max-width:100% !important;
  overflow-x:auto !important;
  overflow-y:hidden !important;
  padding:4px 0 12px !important;
}
.st-key-category_filter [data-testid="stHorizontalBlock"] {
  display:flex !important;
  flex-direction:row !important;
  flex-wrap:nowrap !important;
  justify-content:flex-start !important;
  align-items:center !important;
  gap:8px !important;
  width:max-content !important;
  min-width:100% !important;
}
.st-key-category_filter [data-testid="column"] {
  flex:0 0 auto !important;
  width:max-content !important;
  min-width:max-content !important;
}
.st-key-category_filter [data-testid="stButton"] {
  width:max-content !important;
  min-width:max-content !important;
}
.st-key-category_filter [data-testid="stButton"] button {
  display:inline-flex !important;
  width:max-content !important;
  min-width:max-content !important;
  max-width:none !important;
  white-space:nowrap !important;
  word-break:normal !important;
  overflow-wrap:normal !important;
  writing-mode:horizontal-tb !important;
  padding:7px 15px !important;
  min-height:36px !important;
  border-radius:20px !important;
}
.st-key-category_filter [data-testid="stButton"] button p,
.st-key-category_filter [data-testid="stButton"] button span {
  display:inline !important;
  width:max-content !important;
  min-width:max-content !important;
  white-space:nowrap !important;
  word-break:keep-all !important;
  overflow-wrap:normal !important;
  writing-mode:horizontal-tb !important;
}

/* Hand-drawn Madhubani-inspired FOOD BUS banner */
.madhubani-hero { position:relative !important; display:flex !important; align-items:center !important; justify-content:center !important; min-height:250px !important; padding:16px 10px !important; overflow:hidden !important; background:radial-gradient(ellipse at center,#267a4a 0%,#155333 75%) !important; border-radius:18px !important; }
.folk-banner { position:absolute !important; inset:0 !important; width:100% !important; height:100% !important; pointer-events:none !important; }
.hero-copy { position:relative !important; z-index:2 !important; text-align:center !important; padding:13px 28px !important; border:1px solid rgba(246,215,123,.8) !important; border-radius:14px !important; background:rgba(18,72,43,.88) !important; box-shadow:0 4px 18px rgba(0,0,0,.22) !important; }
.hero-copy h1 { color:#fff4d2 !important; font-size:clamp(1.8rem,4vw,3rem) !important; line-height:1.1 !important; margin:0 0 6px !important; letter-spacing:1.5px !important; }
.hero-copy p { color:#f6dca0 !important; margin:0 !important; font-size:clamp(.78rem,1.5vw,1rem) !important; }
@media (max-width:700px) { .madhubani-hero { min-height:170px !important; } .folk-banner { opacity:.72 !important; } .hero-copy { padding:10px 15px !important; } }
</style>
""", unsafe_allow_html=True)

# ---------- SESSION DATA ----------
for key, default in {
    "cart": {}, "orders": [], "memberships": [], "category": "All"
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# Demo menu prices in rupees. These are editable sample prices.
menu = [
    {"name":"Veg Pizza","category":"Pizza","price":99,"description":"Vegetable-loaded pizza","emoji":"🍕"},
    {"name":"Cheese Pizza","category":"Pizza","price":99,"description":"Cheesy pizza slice","emoji":"🍕"},
    {"name":"Mayo Pizza","category":"Pizza","price":99,"description":"Creamy mayo pizza","emoji":"🍕"},
    {"name":"Corn Pizza","category":"Pizza","price":99,"description":"Sweet corn pizza","emoji":"🍕"},
    {"name":"Paneer Pizza","category":"Pizza","price":99,"description":"Paneer topping pizza","emoji":"🍕"},
    {"name":"Veg Burger","category":"Burger","price":59,"description":"Fresh vegetable burger","emoji":"🍔"},
    {"name":"Cheese Burger","category":"Burger","price":89,"description":"Cheese-filled burger","emoji":"🍔"},
    {"name":"Non-Veg Burger","category":"Burger","price":99,"description":"Classic non-veg burger","emoji":"🍔"},
    {"name":"Vadapav","category":"Snacks & Namkeen","price":25,"description":"Mumbai-style spicy vadapav","emoji":"🥪"},
    {"name":"Misal Pav","category":"Snacks & Namkeen","price":70,"description":"Maharashtrian spicy misal","emoji":"🍲"},
    {"name":"Pav Bhaji","category":"Snacks & Namkeen","price":90,"description":"Buttery pav with bhaji","emoji":"🥘"},
    {"name":"Kanda Poha","category":"Snacks & Namkeen","price":35,"description":"Classic breakfast poha","emoji":"🍋"},
    {"name":"Sabudana Khichdi","category":"Meals","price":60,"description":"Maharashtrian sabudana khichdi","emoji":"🍚"},
    {"name":"Dabeli","category":"Snacks & Namkeen","price":35,"description":"Kutchi dabeli with masala","emoji":"🥯"},
    {"name":"Khaman Dhokla","category":"Snacks & Namkeen","price":45,"description":"Soft steamed Gujarati dhokla","emoji":"🟨"},
    {"name":"Khandvi","category":"Snacks & Namkeen","price":55,"description":"Gujarati gram-flour rolls","emoji":"🍥"},
    {"name":"Fafda","category":"Snacks & Namkeen","price":50,"description":"Crispy Gujarati fafda","emoji":"🥨"},
    {"name":"Thepla","category":"Paratha","price":40,"description":"Gujarati spiced flatbread","emoji":"🫓"},
    {"name":"Masala Dosa","category":"Dosa & Idli","price":90,"description":"Crispy dosa with potato masala","emoji":"🥞"},
    {"name":"Plain Dosa","category":"Dosa & Idli","price":70,"description":"Crispy South Indian dosa","emoji":"🥞"},
    {"name":"Idli Sambar","category":"Dosa & Idli","price":50,"description":"Soft idli with sambar","emoji":"🥣"},
    {"name":"Medu Vada","category":"Dosa & Idli","price":50,"description":"Crispy lentil vada","emoji":"🍩"},
    {"name":"Uttapam","category":"Dosa & Idli","price":80,"description":"Soft vegetable uttapam","emoji":"🥞"},
    {"name":"Lemon Rice","category":"Meals","price":60,"description":"South Indian lemon rice","emoji":"🍋"},
    {"name":"Manchurian","category":"Chinese","price":99,"description":"Spicy street-style Manchurian","emoji":"🥡"},
    {"name":"Veg Noodles","category":"Chinese","price":89,"description":"Street-style veg noodles","emoji":"🍜"},
    {"name":"Fried Rice","category":"Chinese","price":90,"description":"Indo-Chinese fried rice","emoji":"🍚"},
    {"name":"Samosa","category":"Snacks & Namkeen","price":20,"description":"Crispy potato samosa","emoji":"🔺"},
    {"name":"Kachori","category":"Snacks & Namkeen","price":30,"description":"Crispy masala kachori","emoji":"🥟"},
    {"name":"Pani Puri","category":"Chaat","price":40,"description":"Tangy pani puri","emoji":"🥣"},
    {"name":"Bhel Puri","category":"Chaat","price":40,"description":"Mumbai-style bhel puri","emoji":"🥗"},
    {"name":"Sev Puri","category":"Chaat","price":45,"description":"Crispy sev puri chaat","emoji":"🥗"},
    {"name":"Chole Kulche","category":"Meals","price":80,"description":"Spicy chole with kulche","emoji":"🫓"},
    {"name":"Aloo Tikki","category":"Chaat","price":40,"description":"Crispy potato tikki","emoji":"🥔"},
    {"name":"Veg Momos","category":"Chinese","price":70,"description":"Steamed vegetable momos","emoji":"🥟"},
    {"name":"Veg Pulao","category":"Meals","price":89,"description":"Aromatic vegetable pulao","emoji":"🍚"},
    {"name":"Veg Thali","category":"Meals","price":99,"description":"Everyday vegetarian thali","emoji":"🍱"},
    {"name":"Non-Veg Thali","category":"Meals","price":99,"description":"Sample non-veg thali price","emoji":"🍛"},
    {"name":"Pizza Combo","category":"Pizza","price":99,"description":"Mini pizza combo offer","emoji":"🍕"},
    {"name":"Mojito","category":"Drinks","price":59,"description":"Refreshing mint cooler","emoji":"🥤"},
    {"name":"Fresh Lime Soda","category":"Drinks","price":35,"description":"Fresh lime soda","emoji":"🍋"},
    {"name":"Ice Cream","category":"Desserts","price":49,"description":"Creamy ice cream","emoji":"🍨"},
    {"name":"Gulab Jamun","category":"Desserts","price":30,"description":"Traditional sweet treat","emoji":"🍮"},
    {"name":"Jalebi","category":"Desserts","price":35,"description":"Crispy syrupy jalebi","emoji":"🍥"},
    {"name":"Paneer Masala","category":"Snacks & Namkeen","price":95,"description":"Spicy paneer masala","emoji":"🍛"},
    {"name":"Palak Paneer","category":"Snacks & Namkeen","price":99,"description":"Paneer in creamy spinach gravy","emoji":"🥬"},
    {"name":"Shahi Paneer","category":"Snacks & Namkeen","price":99,"description":"Rich shahi-style paneer curry","emoji":"🍛"},
    {"name":"Kadai Paneer","category":"Snacks & Namkeen","price":99,"description":"Paneer tossed with capsicum and spices","emoji":"🍲"},
    {"name":"Paneer Bhurji","category":"Snacks & Namkeen","price":89,"description":"Spiced scrambled paneer","emoji":"🍳"},
    {"name":"Paneer Tikka","category":"Snacks & Namkeen","price":99,"description":"Tandoori-style paneer bites","emoji":"🍢"},
    {"name":"Chole Bhature","category":"Meals","price":90,"description":"Spiced chickpeas with bhature","emoji":"🫓"},
    {"name":"Rajma Chawal","category":"Meals","price":90,"description":"Rajma served with rice","emoji":"🍚"},
    {"name":"Dal Khichdi","category":"Meals","price":75,"description":"Comforting lentil and rice khichdi","emoji":"🍲"},
    {"name":"Aloo Paratha","category":"Paratha","price":60,"description":"Stuffed potato paratha","emoji":"🫓"},
    {"name":"Paneer Paratha","category":"Paratha","price":85,"description":"Stuffed paneer paratha","emoji":"🫓"},
    {"name":"Gobi Paratha","category":"Paratha","price":65,"description":"Stuffed cauliflower paratha","emoji":"🫓"},
    {"name":"Methi Paratha","category":"Paratha","price":55,"description":"Fenugreek paratha","emoji":"🫓"},
    {"name":"Mix Veg Paratha","category":"Paratha","price":75,"description":"Mixed vegetable stuffed paratha","emoji":"🫓"},
    {"name":"Plain Paratha","category":"Paratha","price":35,"description":"Layered plain paratha","emoji":"🫓"},
    {"name":"Veg Sandwich","category":"Sandwiches","price":50,"description":"Fresh vegetable sandwich","emoji":"🥪"},
    {"name":"Cheese Sandwich","category":"Sandwiches","price":70,"description":"Grilled cheese sandwich","emoji":"🥪"},
    {"name":"Bombay Sandwich","category":"Sandwiches","price":65,"description":"Mumbai-style chutney sandwich","emoji":"🥪"},
    {"name":"Club Sandwich","category":"Sandwiches","price":95,"description":"Layered café-style sandwich","emoji":"🥪"},
    {"name":"Paneer Sandwich","category":"Sandwiches","price":85,"description":"Paneer-filled toasted sandwich","emoji":"🥪"},
    {"name":"Grilled Veg Sandwich","category":"Sandwiches","price":70,"description":"Grilled vegetable sandwich","emoji":"🥪"},
    {"name":"Cheese Toast","category":"Sandwiches","price":55,"description":"Crispy cheese toast","emoji":"🍞"},
    {"name":"Rava Dosa","category":"Dosa & Idli","price":85,"description":"Crispy semolina dosa","emoji":"🥞"},
    {"name":"Mysore Masala Dosa","category":"Dosa & Idli","price":99,"description":"Mysore chutney masala dosa","emoji":"🥞"},
    {"name":"Onion Dosa","category":"Dosa & Idli","price":85,"description":"Dosa topped with onion","emoji":"🥞"},
    {"name":"Paneer Dosa","category":"Dosa & Idli","price":99,"description":"Dosa filled with paneer","emoji":"🥞"},
    {"name":"Set Dosa","category":"Dosa & Idli","price":75,"description":"Soft set dosa with chutney","emoji":"🥞"},
    {"name":"Rava Idli","category":"Dosa & Idli","price":60,"description":"Steamed semolina idli","emoji":"🥣"},
    {"name":"Podi Idli","category":"Dosa & Idli","price":65,"description":"Idli tossed in podi masala","emoji":"🥣"},
    {"name":"Thatte Idli","category":"Dosa & Idli","price":65,"description":"Karnataka-style plate idli","emoji":"🥣"},
    {"name":"Appam","category":"Dosa & Idli","price":70,"description":"Soft Kerala-style appam","emoji":"🥞"},
    {"name":"Puttu Kadala","category":"Dosa & Idli","price":90,"description":"Steamed puttu with chickpea curry","emoji":"🍛"},
    {"name":"Pazham Pori","category":"Snacks & Namkeen","price":40,"description":"Kerala banana fritters","emoji":"🍌"},
    {"name":"Medu Vada Sambar","category":"Dosa & Idli","price":60,"description":"Medu vada served with sambar","emoji":"🍩"},
    {"name":"Pesarattu","category":"Dosa & Idli","price":80,"description":"Andhra-style green gram dosa","emoji":"🥞"},
    {"name":"Mirchi Bajji","category":"Snacks & Namkeen","price":35,"description":"Batter-fried chilli snack","emoji":"🌶️"},
    {"name":"Punugulu","category":"Dosa & Idli","price":45,"description":"Crispy Andhra fritters","emoji":"🍘"},
    {"name":"Ragda Pattice","category":"Chaat","price":60,"description":"Potato patties with ragda","emoji":"🥔"},
    {"name":"Kothimbir Vadi","category":"Snacks & Namkeen","price":45,"description":"Coriander gram-flour bites","emoji":"🍘"},
    {"name":"Thalipeeth","category":"Paratha","price":55,"description":"Multigrain Maharashtrian flatbread","emoji":"🫓"},
    {"name":"Bhakarwadi","category":"Snacks & Namkeen","price":35,"description":"Crispy spiced spiral snack","emoji":"🥨"},
    {"name":"Puran Poli","category":"Snacks & Namkeen","price":60,"description":"Sweet lentil-stuffed flatbread","emoji":"🫓"},
    {"name":"Zunka Bhakar","category":"Snacks & Namkeen","price":75,"description":"Traditional zunka with bhakri","emoji":"🍛"},
    {"name":"Appe / Paniyaram","category":"Dosa & Idli","price":60,"description":"Savory rice-lentil dumplings","emoji":"🥘"},
    {"name":"Handvo","category":"Snacks & Namkeen","price":65,"description":"Gujarati savory lentil cake","emoji":"🍰"},
    {"name":"Sev Khamani","category":"Snacks & Namkeen","price":50,"description":"Crumbled khaman with sev","emoji":"🟨"},
    {"name":"Lilva Kachori","category":"Snacks & Namkeen","price":45,"description":"Gujarati green-pea kachori","emoji":"🥟"},
    {"name":"Khakhra","category":"Snacks & Namkeen","price":35,"description":"Crispy Gujarati flatbread snack","emoji":"🫓"},
    {"name":"Dal Dhokli","category":"Snacks & Namkeen","price":85,"description":"Wheat dumplings in lentil curry","emoji":"🍲"},
    {"name":"Gujarati Kadhi Khichdi","category":"Meals","price":90,"description":"Kadhi served with khichdi","emoji":"🍚"},
    {"name":"Rajasthani Pyaz Kachori","category":"Snacks & Namkeen","price":45,"description":"Onion-filled crispy kachori","emoji":"🥟"},
    {"name":"Dal Baati Churma","category":"Meals","price":99,"description":"Rajasthani classic platter","emoji":"🍛"},
    {"name":"Mirchi Vada","category":"Snacks & Namkeen","price":40,"description":"Stuffed and fried chilli","emoji":"🌶️"},
    {"name":"Ghewar","category":"Desserts","price":65,"description":"Traditional Rajasthani sweet","emoji":"🍯"},
    {"name":"Pyaaz Paratha","category":"Paratha","price":65,"description":"Onion-stuffed paratha","emoji":"🫓"},
    {"name":"Bedmi Puri","category":"Meals","price":70,"description":"Spiced lentil puri","emoji":"🫓"},
    {"name":"Aloo Puri","category":"Meals","price":70,"description":"Potato curry with puri","emoji":"🍛"},
    {"name":"Papdi Chaat","category":"Chaat","price":50,"description":"Crispy papdi with chutneys","emoji":"🥗"},
    {"name":"Dahi Puri","category":"Chaat","price":50,"description":"Puris filled with yogurt and chutneys","emoji":"🥣"},
    {"name":"Dahi Bhalla","category":"Chaat","price":60,"description":"Lentil dumplings with yogurt","emoji":"🥣"},
    {"name":"Aloo Chaat","category":"Chaat","price":45,"description":"Tangy spiced potato chaat","emoji":"🥔"},
    {"name":"Basket Chaat","category":"Chaat","price":75,"description":"Crispy edible basket chaat","emoji":"🥗"},
    {"name":"Ram Ladoo","category":"Chaat","price":45,"description":"Delhi-style lentil fritters","emoji":"🍘"},
    {"name":"Palak Chaat","category":"Chaat","price":60,"description":"Crispy spinach chaat","emoji":"🥬"},
    {"name":"Chana Chaat","category":"Chaat","price":50,"description":"Tangy chickpea chaat","emoji":"🥗"},
    {"name":"Jhal Muri","category":"Snacks & Namkeen","price":40,"description":"Kolkata-style puffed rice snack","emoji":"🥗"},
    {"name":"Kathi Roll","category":"Rolls","price":85,"description":"Street-style vegetable kathi roll","emoji":"🌯"},
    {"name":"Puchka","category":"Chaat","price":45,"description":"Bengali-style pani puri","emoji":"🥣"},
    {"name":"Ghugni Chaat","category":"Chaat","price":50,"description":"Yellow-pea curry snack","emoji":"🍲"},
    {"name":"Luchi Aloo Dum","category":"Snacks & Namkeen","price":85,"description":"Bengali luchi with potato curry","emoji":"🍛"},
    {"name":"Momos Fried","category":"Chinese","price":80,"description":"Crispy fried vegetable momos","emoji":"🥟"},
    {"name":"Chilli Potato","category":"Chinese","price":85,"description":"Crispy potatoes in chilli sauce","emoji":"🥔"},
    {"name":"Spring Roll","category":"Chinese","price":70,"description":"Crispy vegetable spring rolls","emoji":"🌯"},
    {"name":"Hakka Noodles","category":"Chinese","price":90,"description":"Street-style Hakka noodles","emoji":"🍜"},
    {"name":"Schezwan Fried Rice","category":"Chinese","price":99,"description":"Spicy Schezwan fried rice","emoji":"🍚"},
    {"name":"Chilli Paneer","category":"Chinese","price":99,"description":"Paneer tossed in chilli sauce","emoji":"🍲"},
    {"name":"Bread Pakora","category":"Snacks & Namkeen","price":30,"description":"Crispy stuffed bread pakora","emoji":"🍞"},
    {"name":"Onion Pakora","category":"Snacks & Namkeen","price":35,"description":"Crispy onion fritters","emoji":"🧅"},
    {"name":"Paneer Pakora","category":"Snacks & Namkeen","price":65,"description":"Paneer fritters","emoji":"🧀"},
    {"name":"Aloo Bonda","category":"Snacks & Namkeen","price":30,"description":"South Indian potato bonda","emoji":"🥔"},
    {"name":"Vada Pav Cheese","category":"Snacks & Namkeen","price":40,"description":"Cheese-loaded vada pav","emoji":"🥪"},
    {"name":"Dahi Vada","category":"Snacks & Namkeen","price":55,"description":"Lentil vada with yogurt","emoji":"🥣"},
    {"name":"Kulfi","category":"Desserts","price":40,"description":"Traditional Indian kulfi","emoji":"🍦"},
    {"name":"Rabri","category":"Desserts","price":60,"description":"Thickened sweetened milk","emoji":"🍮"},
    {"name":"Rasgulla","category":"Desserts","price":35,"description":"Soft Bengali cottage-cheese sweet","emoji":"🍡"},
    {"name":"Sandesh","category":"Desserts","price":45,"description":"Bengali milk-based sweet","emoji":"🍬"},
    {"name":"Malpua","category":"Desserts","price":50,"description":"Sweet fried pancake","emoji":"🥞"},
    {"name":"Kesar Lassi","category":"Drinks","price":60,"description":"Chilled saffron lassi","emoji":"🥛"},
    {"name":"Masala Chaas","category":"Drinks","price":30,"description":"Spiced buttermilk","emoji":"🥛"},
    {"name":"Sugarcane Juice","category":"Drinks","price":35,"description":"Fresh sugarcane juice","emoji":"🥤"},
    {"name":"Masala Chai","category":"Drinks","price":20,"description":"Indian spiced tea","emoji":"☕"},
    {"name":"Filter Coffee","category":"Drinks","price":30,"description":"South Indian filter coffee","emoji":"☕"},
    {"name":"Mango Lassi","category":"Drinks","price":60,"description":"Refreshing mango yogurt drink","emoji":"🥭"},
    {"name":"Pav Sandwich","category":"Sandwiches","price":60,"description":"Mumbai-style stuffed pav sandwich","emoji":"🥪"},
    {"name":"Frankie Roll","category":"Rolls","price":75,"description":"Indian-style stuffed frankie roll","emoji":"🌯"},
    {"name":"Paneer Frankie","category":"Rolls","price":90,"description":"Paneer frankie roll","emoji":"🌯"},
    {"name":"Egg Roll","category":"Rolls","price":75,"description":"Kolkata-style egg roll","emoji":"🌯"},
    {"name":"Chicken Frankie","category":"Rolls","price":99,"description":"Chicken-filled frankie roll","emoji":"🌯"},
    {"name":"Chicken Momos","category":"Chinese","price":99,"description":"Steamed chicken momos","emoji":"🥟"},
    {"name":"Egg Bhurji Pav","category":"Snacks & Namkeen","price":75,"description":"Spiced egg bhurji with pav","emoji":"🍳"},
    {"name":"Chicken Kathi Roll","category":"Rolls","price":99,"description":"Chicken-filled kathi roll","emoji":"🌯"},
    {"name":"Margherita Pizza","category":"Pizza","price":99,"description":"Classic tomato and cheese pizza","emoji":"🍕"},
    {"name":"Farmhouse Pizza","category":"Pizza","price":99,"description":"Mixed vegetable pizza","emoji":"🍕"},
    {"name":"Cheese Burst Pizza","category":"Pizza","price":99,"description":"Cheese-filled crust pizza","emoji":"🍕"},
    {"name":"Peri Peri Pizza","category":"Pizza","price":99,"description":"Spicy peri peri pizza","emoji":"🍕"},
    {"name":"Aloo Tikki Burger","category":"Burger","price":59,"description":"Crispy potato patty burger","emoji":"🍔"},
    {"name":"Paneer Burger","category":"Burger","price":89,"description":"Spiced paneer burger","emoji":"🍔"},
    {"name":"Double Patty Burger","category":"Burger","price":99,"description":"Double patty burger","emoji":"🍔"},
    {"name":"Peri Peri Burger","category":"Burger","price":89,"description":"Spicy peri peri burger","emoji":"🍔"},
    {"name":"Masala Sandwich","category":"Sandwiches","price":45,"description":"Spiced vegetable sandwich","emoji":"🥪"},
    {"name":"Corn Cheese Sandwich","category":"Sandwiches","price":75,"description":"Corn and cheese sandwich","emoji":"🥪"},
    {"name":"Chutney Sandwich","category":"Sandwiches","price":40,"description":"Green chutney sandwich","emoji":"🥪"},
    {"name":"Cheese Garlic Sandwich","category":"Sandwiches","price":75,"description":"Garlic cheese sandwich","emoji":"🥪"},
    {"name":"Ghee Roast Dosa","category":"Dosa & Idli","price":95,"description":"Crispy ghee roast dosa","emoji":"🥞"},
    {"name":"Cheese Masala Dosa","category":"Dosa & Idli","price":99,"description":"Dosa with cheese masala","emoji":"🥞"},
    {"name":"Mini Idli Sambar","category":"Dosa & Idli","price":55,"description":"Mini idlis with sambar","emoji":"🥣"},
    {"name":"Onion Uttapam","category":"Dosa & Idli","price":85,"description":"Uttapam topped with onion","emoji":"🥞"},
    {"name":"Lachha Paratha","category":"Paratha","price":55,"description":"Flaky layered paratha","emoji":"🫓"},
    {"name":"Onion Paratha","category":"Paratha","price":60,"description":"Stuffed onion paratha","emoji":"🫓"},
    {"name":"Aloo Cheese Paratha","category":"Paratha","price":85,"description":"Potato cheese paratha","emoji":"🫓"},
    {"name":"Cheese Paratha","category":"Paratha","price":85,"description":"Cheese-stuffed paratha","emoji":"🫓"},
    {"name":"Schezwan Noodles","category":"Chinese","price":95,"description":"Spicy Schezwan noodles","emoji":"🍜"},
    {"name":"Chilli Garlic Noodles","category":"Chinese","price":95,"description":"Chilli garlic noodles","emoji":"🍜"},
    {"name":"Veg Manchurian Dry","category":"Chinese","price":90,"description":"Dry vegetable Manchurian","emoji":"🥡"},
    {"name":"Veg Manchurian Gravy","category":"Chinese","price":95,"description":"Manchurian in gravy","emoji":"🥡"},
    {"name":"Paneer Chilli Dry","category":"Chinese","price":99,"description":"Dry chilli paneer","emoji":"🍲"},
    {"name":"Dahi Papdi Chaat","category":"Chaat","price":55,"description":"Papdi with yogurt and chutneys","emoji":"🥗"},
    {"name":"Samosa Chaat","category":"Chaat","price":55,"description":"Samosa with chole and chutneys","emoji":"🥗"},
    {"name":"Masala Papad","category":"Chaat","price":35,"description":"Crispy papad with toppings","emoji":"🥗"},
    {"name":"Potato Wafers","category":"Snacks & Namkeen","price":30,"description":"Crispy salted potato wafers","emoji":"🥔"},
    {"name":"Masala Wafers","category":"Snacks & Namkeen","price":35,"description":"Spicy potato wafers","emoji":"🥔"},
    {"name":"Banana Chips","category":"Snacks & Namkeen","price":40,"description":"Crispy banana chips","emoji":"🍌"},
    {"name":"Plain Sev","category":"Snacks & Namkeen","price":30,"description":"Crunchy gram flour sev","emoji":"🥨"},
    {"name":"Tikha Sev","category":"Snacks & Namkeen","price":35,"description":"Spicy sev","emoji":"🥨"},
    {"name":"Chivda","category":"Snacks & Namkeen","price":35,"description":"Poha chivda mixture","emoji":"🥜"},
    {"name":"Farsan Mix","category":"Snacks & Namkeen","price":40,"description":"Savory farsan mixture","emoji":"🥨"},
    {"name":"Masala Papdi","category":"Snacks & Namkeen","price":35,"description":"Spiced crispy papdi","emoji":"🥨"},
    {"name":"Gathiya","category":"Snacks & Namkeen","price":40,"description":"Crunchy gathiya","emoji":"🥨"},
    {"name":"Chakli","category":"Snacks & Namkeen","price":40,"description":"Crispy spiral snack","emoji":"🥨"},
    {"name":"Moong Dal Namkeen","category":"Snacks & Namkeen","price":35,"description":"Crunchy moong dal","emoji":"🥜"},
    {"name":"Son Papdi","category":"Desserts","price":40,"description":"Flaky traditional sweet","emoji":"🍬"},
    {"name":"Kaju Katli","category":"Desserts","price":70,"description":"Cashew sweet","emoji":"🍬"},
    {"name":"Motichoor Ladoo","category":"Desserts","price":35,"description":"Boondi ladoo","emoji":"🍡"},
    {"name":"Besan Ladoo","category":"Desserts","price":35,"description":"Gram flour ladoo","emoji":"🍡"},
    {"name":"Jalebi Rabri","category":"Desserts","price":70,"description":"Jalebi with rabri","emoji":"🍮"},
    {"name":"Kulfi Falooda","category":"Desserts","price":80,"description":"Kulfi with falooda","emoji":"🍨"},
    {"name":"Cold Coffee","category":"Drinks","price":60,"description":"Chilled coffee","emoji":"🥤"},
    {"name":"Masala Chaas","category":"Drinks","price":30,"description":"Spiced buttermilk","emoji":"🥛"},
    {"name":"Sugarcane Juice","category":"Drinks","price":35,"description":"Fresh sugarcane juice","emoji":"🥤"},
]

plans = {
    "Daily Thali (1 Day)": 120,
    "2-Day Thali Plan": 240,
    "Weekly Membership": 500,
    "Monthly Membership": 1800
}

# ---------- BRAND HEADER ----------
st.markdown("""
<div class="hero madhubani-hero">
<svg class="folk-banner" viewBox="0 0 1200 250" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Indian Madhubani-inspired folk art featuring Taj Mahal, elephants, peacocks and floral motifs">
<defs>
 <pattern id="dotsA" width="12" height="12" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="1.7" fill="#f6d77b"/><circle cx="9" cy="9" r="1.4" fill="#e97854"/></pattern>
 <pattern id="stripesA" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M0 0L10 10M-3 3L3 -3M7 13L13 7" stroke="#f4d27a" stroke-width="1.4"/></pattern>
</defs>
<rect x="7" y="7" width="1186" height="236" rx="17" fill="none" stroke="#f6d77b" stroke-width="5"/>
<rect x="17" y="17" width="1166" height="216" rx="12" fill="none" stroke="#f6d77b" stroke-width="1.8" stroke-dasharray="3 6"/>
<!-- ornamental floral corners -->
<g stroke="#f6d77b" stroke-width="3" stroke-linejoin="round" fill="#d85b49">
 <path d="M38 50Q65 24 91 50Q65 76 38 50ZM91 50Q117 24 143 50Q117 76 91 50ZM65 76Q65 42 91 27Q117 42 117 76" />
 <path d="M1109 50Q1135 24 1161 50Q1135 76 1109 50ZM1057 50Q1083 24 1109 50Q1083 76 1057 50ZM1083 76Q1083 42 1109 27Q1135 42 1135 76"/>
 <path d="M38 200Q65 174 91 200Q65 226 38 200ZM91 200Q117 174 143 200Q117 226 91 200Z M1057 200Q1083 174 1109 200Q1083 226 1057 200ZM1109 200Q1135 174 1161 200Q1135 226 1109 200Z"/>
</g>
<!-- elephant procession -->
<g stroke="#f6d77b" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">
 <g transform="translate(145 0)">
  <path d="M20 164Q22 121 64 115Q105 111 125 145L143 151Q153 163 140 177L127 179L125 207H111L108 179H54L50 207H36L34 177Q17 176 20 164Z" fill="#e6a64d"/>
  <path d="M121 146Q149 131 154 155Q157 171 143 177M142 165Q129 173 134 187" fill="none"/>
  <path d="M44 124Q72 92 105 124L95 143H53Z" fill="#c64f43"/><path d="M53 125L74 106L95 125M74 106V91" fill="none"/>
  <path d="M57 147Q75 132 94 147Q75 163 57 147Z" fill="url(#dotsA)"/><circle cx="111" cy="143" r="3.8" fill="#173f2b" stroke="none"/>
  <path d="M33 161Q48 150 59 161M65 178L65 191M88 178L88 191" fill="none"/>
 </g>
 <g transform="translate(900 0) scale(.92 1)">
  <path d="M20 164Q22 121 64 115Q105 111 125 145L143 151Q153 163 140 177L127 179L125 207H111L108 179H54L50 207H36L34 177Q17 176 20 164Z" fill="#e6a64d"/>
  <path d="M121 146Q149 131 154 155Q157 171 143 177M142 165Q129 173 134 187" fill="none"/>
  <path d="M44 124Q72 92 105 124L95 143H53Z" fill="#c64f43"/><path d="M53 125L74 106L95 125M74 106V91" fill="none"/>
  <path d="M57 147Q75 132 94 147Q75 163 57 147Z" fill="url(#dotsA)"/><circle cx="111" cy="143" r="3.8" fill="#173f2b" stroke="none"/>
  <path d="M33 161Q48 150 59 161M65 178L65 191M88 178L88 191" fill="none"/>
 </g>
</g>
<!-- peacocks -->
<g stroke="#f6d77b" stroke-width="2.8" stroke-linejoin="round">
 <path d="M300 184Q272 148 288 117Q309 128 312 157Q319 119 342 112Q354 148 329 178Q352 154 370 162Q364 194 329 199Z" fill="#278b69"/>
 <path d="M299 169Q295 144 306 137Q317 147 312 169M324 171Q325 144 339 137Q347 151 332 174M342 183Q350 166 360 170" fill="none"/>
 <path d="M316 184Q305 159 320 145Q337 159 329 184L324 205H313Z" fill="#2b9c83"/>
 <circle cx="323" cy="151" r="3" fill="#f4d27a" stroke="none"/><path d="M317 143L320 135L324 143M323 147L335 143" fill="none"/>
 <path d="M900 184Q872 148 888 117Q909 128 912 157Q919 119 942 112Q954 148 929 178Q952 154 970 162Q964 194 929 199Z" fill="#278b69"/>
 <path d="M899 169Q895 144 906 137Q917 147 912 169M924 171Q925 144 939 137Q947 151 932 174M942 183Q950 166 960 170" fill="none"/>
 <path d="M916 184Q905 159 920 145Q937 159 929 184L924 205H913Z" fill="#2b9c83"/>
 <circle cx="923" cy="151" r="3" fill="#f4d27a" stroke="none"/><path d="M917 143L920 135L924 143M923 147L935 143" fill="none"/>
</g>
<!-- Taj Mahal -->
<g transform="translate(0 1)" stroke="#f6d77b" stroke-width="3" stroke-linejoin="round">
 <path d="M478 183V125L510 99L542 125V183ZM658 183V125L690 99L722 125V183Z" fill="#e9dfc5"/>
 <path d="M514 183V105Q600 18 686 105V183Z" fill="#f4e8ca"/>
 <path d="M570 183V132Q600 91 630 132V183Z" fill="#c85a48"/>
 <path d="M540 183V139Q555 117 570 139V183M630 183V139Q645 117 660 139V183" fill="#d36a50"/>
 <path d="M600 38V20M591 27H609M600 20L594 12L600 4L606 12Z" fill="#e6a64d"/>
 <path d="M510 99V80M500 87H520M690 99V80M680 87H700M478 125V108M468 115H488M722 125V108M712 115H732" fill="none"/>
 <path d="M475 183H725M490 193H710" fill="none"/>
 <path d="M586 183V153Q600 132 614 153V183" fill="#f6d77b"/>
 <path d="M555 105Q600 65 645 105M575 112Q600 91 625 112" fill="none"/>
</g>
<!-- floral vines and dots -->
<g fill="none" stroke="#f6d77b" stroke-width="2.4">
 <path d="M170 44Q220 15 270 44T370 44M830 44Q880 15 930 44T1030 44"/>
 <path d="M170 215Q220 185 270 215T370 215M830 215Q880 185 930 215T1030 215"/>
 <path d="M185 44q-12 -18 -24 0q12 18 24 0M245 44q-12 -18 -24 0q12 18 24 0M305 44q-12 -18 -24 0q12 18 24 0M865 44q-12 -18 -24 0q12 18 24 0M925 44q-12 -18 -24 0q12 18 24 0M985 44q-12 -18 -24 0q12 18 24 0"/>
 <path d="M185 215q-12 -18 -24 0q12 18 24 0M245 215q-12 -18 -24 0q12 18 24 0M305 215q-12 -18 -24 0q12 18 24 0M865 215q-12 -18 -24 0q12 18 24 0M925 215q-12 -18 -24 0q12 18 24 0M985 215q-12 -18 -24 0q12 18 24 0"/>
</g>
<g fill="#f6d77b"><circle cx="405" cy="54" r="4"/><circle cx="430" cy="74" r="3"/><circle cx="795" cy="54" r="4"/><circle cx="770" cy="74" r="3"/><circle cx="405" cy="195" r="4"/><circle cx="795" cy="195" r="4"/></g>
</svg>
<div class="hero-copy"><h1>🚌 FOOD BUS</h1><p>Good Food. Great Value. Easy Ordering.</p></div>
</div>
""", unsafe_allow_html=True)

st.sidebar.title("🚌 FOOD BUS")
page = st.radio(
    "Navigation",
    ["Home", "Food Menu", "My Cart", "Mess Membership", "My Orders"],
    horizontal=True,
    label_visibility="collapsed",
    key="main_navigation"
)
# Navigation labels are plain text for a cleaner, professional look

if page == "Home":
    st.markdown("""
    <div class="ad-strip"><span>🚌 FOOD BUS • Pocket-friendly Indian street food • Freshly prepared favourites • Dosa, Idli, Dhokla, Vadapav, Pizza, Burgers, Chaat & More • Daily Thali ₹120 • Weekly Membership ₹500 • Monthly Membership ₹1800 • FOOD BUS — Good Food, Great Value! 🚌</span></div>
    """, unsafe_allow_html=True)
    st.title("Welcome to FOOD BUS!")
    st.subheader("Your Food, Your Choice.")
    st.write("Explore popular Indian street food and affordable meal plans.")
    c1, c2 = st.columns(2)
    with c1:
        st.info("FOOD ORDERING")
        st.write("Pizza, burgers, regional Indian snacks, South Indian dishes, Chinese and more.")
        if st.button("Explore Food Menu", key="home_menu"):
            st.session_state.category = "All"
            st.rerun()
    with c2:
        st.info("MESS MEMBERSHIP")
        st.write("Daily thali, weekly and monthly membership options.")
    st.divider()
    st.subheader("Popular Indian Food Regions")
    region_cols = st.columns(4)
    for col, label in zip(region_cols, ["Maharashtra", "Gujarati", "South Indian", "Street Food"]):
        with col:
            st.markdown(f"**{label}**")
    st.caption("Affordable food options • Easy ordering • Flexible membership plans")

elif page == "Food Menu":
    st.title("Explore Our Food Menu")
    search_terms = [item["name"] for item in menu]
    scroll_count = len(search_terms)
    visible_terms = "".join(f"<span>{term}</span>" for term in search_terms)
    st.markdown(f"""<style>
    .search-rotate {{ display:block; height:1.55em; overflow:hidden; color:#e83e8c; font-weight:800; }}
    .search-rotate-inner {{ display:block; animation:foodscroll {scroll_count * 2}s steps({scroll_count}) infinite; }}
    .search-rotate-inner span {{ display:block; height:1.55em; line-height:1.55em; }}
    @keyframes foodscroll {{ to {{ transform:translateY(-{scroll_count * 1.55}em); }} }}
    </style>""", unsafe_allow_html=True)
    st.markdown(f"""<div class="search-hint">Search suggestions — try:</div><div class="search-rotate"><div class="search-rotate-inner">{visible_terms}<span>{search_terms[0]}</span></div></div>""", unsafe_allow_html=True)
    search = st.text_input("Search food", placeholder="Search by food name...", label_visibility="collapsed")
    categories = ["All", "Pizza", "Burger", "Sandwiches", "Rolls", "Paratha", "Dosa & Idli", "Chinese", "Chaat", "Snacks & Namkeen", "Meals", "Desserts", "Drinks"]
    st.write("**Categories**")
    with st.container(key="category_filter"):
        category_cols = st.columns(len(categories))
        for i, category in enumerate(categories):
            with category_cols[i]:
                if st.button(category, key="category_chip_" + str(i), use_container_width=False):
                    st.session_state.category = category
    selected_category = st.session_state.category
    if selected_category != "All":
        st.caption("Showing: " + selected_category)
    query = search.strip().lower()
    filtered_menu = [
        item for item in menu
        if (selected_category == "All" or item["category"] == selected_category)
        and (not query or query in item["name"].lower() or query in item["category"].lower())
    ]
    if not filtered_menu:
        st.warning("No food items found. Try another search.")
    with st.container(key="food_grid"):
        for index, item in enumerate(filtered_menu):
            with st.container(border=True):
                info_col, photo_col = st.columns([5, 1.55], vertical_alignment="center")
                with info_col:
                    st.markdown(f"<div class='food-title'>{item['name']}</div>", unsafe_allow_html=True)
                    st.caption(item["description"])
                    st.markdown(f"<div class='food-price'>₹{item['price']}</div>", unsafe_allow_html=True)
                    st.markdown("<span class='food-availability'>● On the menu</span>", unsafe_allow_html=True)
                    if st.button("ADD", key="add_" + str(index) + "_" + item["name"]):
                        name = item["name"]
                        st.session_state.cart[name] = st.session_state.cart.get(name, 0) + 1
                        st.success("Added to cart!")
                        st.rerun()
                with photo_col:
                    st.markdown(f"<div class='food-photo-slot'>{item['emoji']}</div>", unsafe_allow_html=True)
    
elif page == "My Cart":
    st.title("My Cart")
    cart = st.session_state.cart
    if not cart:
        st.info("Your cart is empty.")
    else:
        total = 0
        for name, quantity in list(cart.items()):
            item = next((x for x in menu if x["name"] == name), None)
            if item is None:
                continue
            subtotal = item["price"] * quantity
            total += subtotal
            with st.container(border=True):
                c1, c2, c3 = st.columns([3, 1, 1])
                with c1:
                    st.write("**" + name + "**")
                    st.write("₹", item["price"], "each")
                with c2:
                    st.write("Quantity:", quantity)
                with c3:
                    if st.button("Remove", key="remove_" + name):
                        del st.session_state.cart[name]
                        st.rerun()
                st.write("Subtotal: ₹", subtotal)
        st.divider()
        st.subheader("Total Amount: ₹" + str(total))
        st.subheader("Delivery Details")
        customer_name = st.text_input("Customer Name")
        phone = st.text_input("Phone Number")
        address = st.text_area("Delivery Address")
        if st.button("Place Demo Order"):
            if not customer_name or not phone or not address:
                st.warning("Please fill all delivery details.")
            elif not phone.isdigit() or len(phone) != 10:
                st.warning("Please enter a valid 10-digit phone number.")
            else:
                order = {
                    "type": "Food Order", "customer": customer_name,
                    "items": dict(st.session_state.cart), "total": total,
                    "date": datetime.now().strftime("%d-%m-%Y %I:%M %p")
                }
                st.session_state.orders.append(order)
                st.session_state.cart = {}
                st.success("Demo order placed successfully!")
                st.info("No real payment or delivery has been processed.")
                st.rerun()

elif page == "Mess Membership":
    st.title("Mess Membership Plans")
    st.write("Choose a membership according to your stay and needs.")
    for plan_name, price in plans.items():
        with st.container(border=True):
            c1, c2 = st.columns([3, 1])
            with c1:
                st.subheader(plan_name)
                st.write("Affordable food membership plan")
            with c2:
                st.subheader("₹" + str(price))
    st.divider()
    st.subheader("Select Your Membership")
    selected_plan = st.selectbox("Choose Plan", list(plans.keys()))
    member_name = st.text_input("Member Name")
    member_phone = st.text_input("Member Phone Number")
    if st.button("Choose Membership"):
        if not member_name or not member_phone:
            st.warning("Please enter your name and phone number.")
        elif not member_phone.isdigit() or len(member_phone) != 10:
            st.warning("Please enter a valid 10-digit phone number.")
        else:
            membership = {
                "type": "Mess Membership", "customer": member_name,
                "plan": selected_plan, "price": plans[selected_plan],
                "date": datetime.now().strftime("%d-%m-%Y %I:%M %p")
            }
            st.session_state.memberships.append(membership)
            st.session_state.orders.append(membership)
            st.success("Demo membership selected successfully!")
            st.info("This is a demo selection, not a paid subscription.")

elif page == "My Orders":
    st.title("My Orders")
    if not st.session_state.orders:
        st.info("No orders yet.")
    else:
        for index, order in enumerate(reversed(st.session_state.orders), start=1):
            with st.container(border=True):
                st.subheader("Order / Membership #" + str(index))
                st.write("Type:", order["type"])
                st.write("Customer:", order["customer"])
                st.write("Date:", order["date"])
                if order["type"] == "Food Order":
                    st.markdown("**Ordered Items**")
                    items = order.get("items", {})
                    if isinstance(items, dict) and items:
                        for item_name, quantity in items.items():
                            item_label = "item" if quantity == 1 else "items"
                            st.write(f"{item_name} — Quantity: {quantity} {item_label}")
                    else:
                        st.write("No item details available.")
                    st.markdown(f"**Total Amount: ₹{order['total']}**")
                else:
                    st.write("Membership Plan:", order["plan"])
                    st.write("Membership Price: ₹", order["price"])

st.divider()
st.caption("FOOD BUS | Food Ordering & Mess Membership")
st.caption("Demo Version 3 • Demo prices; actual food photos and persistent database are future updates")
