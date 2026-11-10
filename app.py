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
.hero { background:linear-gradient(110deg,#126b39,#36a765); padding:26px; border-radius:20px; color:white; margin-bottom:16px; }
.hero h1 { color:white; margin:0; }
.hero p { color:#f0fff4; margin-bottom:0; }
.ad-strip { overflow:hidden; white-space:nowrap; background:#fff4d6; border:2px solid #bd8731; border-radius:14px; padding:11px 0; margin:0 0 20px 0; color:#155b34; font-weight:800; }
.ad-strip span { display:inline-block; padding-left:100%; animation:adscroll 27s linear infinite; }
@keyframes adscroll { from { transform:translateX(0); } to { transform:translateX(-100%); } }
.search-hint { color:#176b3a; font-weight:800; margin:4px 0 8px 2px; }
.search-rotate { display:inline-flex; flex-direction:column; vertical-align:bottom; height:1.5em; overflow:hidden; color:#e83e8c; }
.search-rotate span { display:block; height:1.5em; line-height:1.5em; }
.food-photo-slot { width:154px; height:154px; margin:12px auto 18px; border-radius:50%; background:radial-gradient(circle,#fffaf0 0 58%,#f3d89b 59% 64%,#176b3a 65% 69%,#fff 70%); display:flex; align-items:center; justify-content:center; font-size:4rem; box-shadow:0 4px 14px rgba(0,0,0,.12); }
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
    {"name":"Vadapav","category":"Maharashtra","price":25,"description":"Mumbai-style spicy vadapav","emoji":"🥪"},
    {"name":"Misal Pav","category":"Maharashtra","price":70,"description":"Maharashtrian spicy misal","emoji":"🍲"},
    {"name":"Pav Bhaji","category":"Maharashtra","price":90,"description":"Buttery pav with bhaji","emoji":"🥘"},
    {"name":"Kanda Poha","category":"Maharashtra","price":35,"description":"Classic breakfast poha","emoji":"🍋"},
    {"name":"Sabudana Khichdi","category":"Maharashtra","price":60,"description":"Maharashtrian sabudana khichdi","emoji":"🍚"},
    {"name":"Dabeli","category":"Gujarati","price":35,"description":"Kutchi dabeli with masala","emoji":"🥯"},
    {"name":"Khaman Dhokla","category":"Gujarati","price":45,"description":"Soft steamed Gujarati dhokla","emoji":"🟨"},
    {"name":"Khandvi","category":"Gujarati","price":55,"description":"Gujarati gram-flour rolls","emoji":"🍥"},
    {"name":"Fafda","category":"Gujarati","price":50,"description":"Crispy Gujarati fafda","emoji":"🥨"},
    {"name":"Thepla","category":"Gujarati","price":40,"description":"Gujarati spiced flatbread","emoji":"🫓"},
    {"name":"Masala Dosa","category":"South Indian","price":90,"description":"Crispy dosa with potato masala","emoji":"🥞"},
    {"name":"Plain Dosa","category":"South Indian","price":70,"description":"Crispy South Indian dosa","emoji":"🥞"},
    {"name":"Idli Sambar","category":"South Indian","price":50,"description":"Soft idli with sambar","emoji":"🥣"},
    {"name":"Medu Vada","category":"South Indian","price":50,"description":"Crispy lentil vada","emoji":"🍩"},
    {"name":"Uttapam","category":"South Indian","price":80,"description":"Soft vegetable uttapam","emoji":"🥞"},
    {"name":"Lemon Rice","category":"South Indian","price":60,"description":"South Indian lemon rice","emoji":"🍋"},
    {"name":"Manchurian","category":"Chinese","price":99,"description":"Spicy street-style Manchurian","emoji":"🥡"},
    {"name":"Veg Noodles","category":"Chinese","price":89,"description":"Street-style veg noodles","emoji":"🍜"},
    {"name":"Fried Rice","category":"Chinese","price":90,"description":"Indo-Chinese fried rice","emoji":"🍚"},
    {"name":"Samosa","category":"Street Food","price":20,"description":"Crispy potato samosa","emoji":"🔺"},
    {"name":"Kachori","category":"Street Food","price":30,"description":"Crispy masala kachori","emoji":"🥟"},
    {"name":"Pani Puri","category":"Street Food","price":40,"description":"Tangy pani puri","emoji":"🥣"},
    {"name":"Bhel Puri","category":"Street Food","price":40,"description":"Mumbai-style bhel puri","emoji":"🥗"},
    {"name":"Sev Puri","category":"Street Food","price":45,"description":"Crispy sev puri chaat","emoji":"🥗"},
    {"name":"Chole Kulche","category":"Street Food","price":80,"description":"Spicy chole with kulche","emoji":"🫓"},
    {"name":"Aloo Tikki","category":"Street Food","price":40,"description":"Crispy potato tikki","emoji":"🥔"},
    {"name":"Veg Momos","category":"Street Food","price":70,"description":"Steamed vegetable momos","emoji":"🥟"},
    {"name":"Veg Pulao","category":"Meals","price":89,"description":"Aromatic vegetable pulao","emoji":"🍚"},
    {"name":"Veg Thali","category":"Meals","price":99,"description":"Everyday vegetarian thali","emoji":"🍱"},
    {"name":"Non-Veg Thali","category":"Meals","price":99,"description":"Sample non-veg thali price","emoji":"🍛"},
    {"name":"Pizza Combo","category":"Combos","price":99,"description":"Mini pizza combo offer","emoji":"🍕"},
    {"name":"Mojito","category":"Drinks","price":59,"description":"Refreshing mint cooler","emoji":"🥤"},
    {"name":"Fresh Lime Soda","category":"Drinks","price":35,"description":"Fresh lime soda","emoji":"🍋"},
    {"name":"Ice Cream","category":"Desserts","price":49,"description":"Creamy ice cream","emoji":"🍨"},
    {"name":"Gulab Jamun","category":"Desserts","price":30,"description":"Traditional sweet treat","emoji":"🍮"},
    {"name":"Jalebi","category":"Desserts","price":35,"description":"Crispy syrupy jalebi","emoji":"🍥"},
    {"name":"Paneer Masala","category":"Punjabi","price":95,"description":"Spicy paneer masala","emoji":"🍛"},
    {"name":"Palak Paneer","category":"Punjabi","price":99,"description":"Paneer in creamy spinach gravy","emoji":"🥬"},
    {"name":"Shahi Paneer","category":"Punjabi","price":99,"description":"Rich shahi-style paneer curry","emoji":"🍛"},
    {"name":"Kadai Paneer","category":"Punjabi","price":99,"description":"Paneer tossed with capsicum and spices","emoji":"🍲"},
    {"name":"Paneer Bhurji","category":"Punjabi","price":89,"description":"Spiced scrambled paneer","emoji":"🍳"},
    {"name":"Paneer Tikka","category":"Punjabi","price":99,"description":"Tandoori-style paneer bites","emoji":"🍢"},
    {"name":"Chole Bhature","category":"North Indian","price":90,"description":"Spiced chickpeas with bhature","emoji":"🫓"},
    {"name":"Rajma Chawal","category":"North Indian","price":90,"description":"Rajma served with rice","emoji":"🍚"},
    {"name":"Dal Khichdi","category":"North Indian","price":75,"description":"Comforting lentil and rice khichdi","emoji":"🍲"},
    {"name":"Aloo Paratha","category":"North Indian","price":60,"description":"Stuffed potato paratha","emoji":"🫓"},
    {"name":"Paneer Paratha","category":"North Indian","price":85,"description":"Stuffed paneer paratha","emoji":"🫓"},
    {"name":"Gobi Paratha","category":"North Indian","price":65,"description":"Stuffed cauliflower paratha","emoji":"🫓"},
    {"name":"Methi Paratha","category":"North Indian","price":55,"description":"Fenugreek paratha","emoji":"🫓"},
    {"name":"Mix Veg Paratha","category":"North Indian","price":75,"description":"Mixed vegetable stuffed paratha","emoji":"🫓"},
    {"name":"Plain Paratha","category":"North Indian","price":35,"description":"Layered plain paratha","emoji":"🫓"},
    {"name":"Veg Sandwich","category":"Sandwich","price":50,"description":"Fresh vegetable sandwich","emoji":"🥪"},
    {"name":"Cheese Sandwich","category":"Sandwich","price":70,"description":"Grilled cheese sandwich","emoji":"🥪"},
    {"name":"Bombay Sandwich","category":"Sandwich","price":65,"description":"Mumbai-style chutney sandwich","emoji":"🥪"},
    {"name":"Club Sandwich","category":"Sandwich","price":95,"description":"Layered café-style sandwich","emoji":"🥪"},
    {"name":"Paneer Sandwich","category":"Sandwich","price":85,"description":"Paneer-filled toasted sandwich","emoji":"🥪"},
    {"name":"Grilled Veg Sandwich","category":"Sandwich","price":70,"description":"Grilled vegetable sandwich","emoji":"🥪"},
    {"name":"Cheese Toast","category":"Sandwich","price":55,"description":"Crispy cheese toast","emoji":"🍞"},
    {"name":"Rava Dosa","category":"South Indian","price":85,"description":"Crispy semolina dosa","emoji":"🥞"},
    {"name":"Mysore Masala Dosa","category":"South Indian","price":99,"description":"Mysore chutney masala dosa","emoji":"🥞"},
    {"name":"Onion Dosa","category":"South Indian","price":85,"description":"Dosa topped with onion","emoji":"🥞"},
    {"name":"Paneer Dosa","category":"South Indian","price":99,"description":"Dosa filled with paneer","emoji":"🥞"},
    {"name":"Set Dosa","category":"South Indian","price":75,"description":"Soft set dosa with chutney","emoji":"🥞"},
    {"name":"Rava Idli","category":"South Indian","price":60,"description":"Steamed semolina idli","emoji":"🥣"},
    {"name":"Podi Idli","category":"South Indian","price":65,"description":"Idli tossed in podi masala","emoji":"🥣"},
    {"name":"Thatte Idli","category":"South Indian","price":65,"description":"Karnataka-style plate idli","emoji":"🥣"},
    {"name":"Appam","category":"Kerala","price":70,"description":"Soft Kerala-style appam","emoji":"🥞"},
    {"name":"Puttu Kadala","category":"Kerala","price":90,"description":"Steamed puttu with chickpea curry","emoji":"🍛"},
    {"name":"Pazham Pori","category":"Kerala","price":40,"description":"Kerala banana fritters","emoji":"🍌"},
    {"name":"Medu Vada Sambar","category":"South Indian","price":60,"description":"Medu vada served with sambar","emoji":"🍩"},
    {"name":"Pesarattu","category":"Andhra","price":80,"description":"Andhra-style green gram dosa","emoji":"🥞"},
    {"name":"Mirchi Bajji","category":"Andhra","price":35,"description":"Batter-fried chilli snack","emoji":"🌶️"},
    {"name":"Punugulu","category":"Andhra","price":45,"description":"Crispy Andhra fritters","emoji":"🍘"},
    {"name":"Ragda Pattice","category":"Maharashtra","price":60,"description":"Potato patties with ragda","emoji":"🥔"},
    {"name":"Kothimbir Vadi","category":"Maharashtra","price":45,"description":"Coriander gram-flour bites","emoji":"🍘"},
    {"name":"Thalipeeth","category":"Maharashtra","price":55,"description":"Multigrain Maharashtrian flatbread","emoji":"🫓"},
    {"name":"Bhakarwadi","category":"Maharashtra","price":35,"description":"Crispy spiced spiral snack","emoji":"🥨"},
    {"name":"Puran Poli","category":"Maharashtra","price":60,"description":"Sweet lentil-stuffed flatbread","emoji":"🫓"},
    {"name":"Zunka Bhakar","category":"Maharashtra","price":75,"description":"Traditional zunka with bhakri","emoji":"🍛"},
    {"name":"Appe / Paniyaram","category":"South Indian","price":60,"description":"Savory rice-lentil dumplings","emoji":"🥘"},
    {"name":"Handvo","category":"Gujarati","price":65,"description":"Gujarati savory lentil cake","emoji":"🍰"},
    {"name":"Sev Khamani","category":"Gujarati","price":50,"description":"Crumbled khaman with sev","emoji":"🟨"},
    {"name":"Lilva Kachori","category":"Gujarati","price":45,"description":"Gujarati green-pea kachori","emoji":"🥟"},
    {"name":"Khakhra","category":"Gujarati","price":35,"description":"Crispy Gujarati flatbread snack","emoji":"🫓"},
    {"name":"Dal Dhokli","category":"Gujarati","price":85,"description":"Wheat dumplings in lentil curry","emoji":"🍲"},
    {"name":"Gujarati Kadhi Khichdi","category":"Gujarati","price":90,"description":"Kadhi served with khichdi","emoji":"🍚"},
    {"name":"Rajasthani Pyaz Kachori","category":"Rajasthani","price":45,"description":"Onion-filled crispy kachori","emoji":"🥟"},
    {"name":"Dal Baati Churma","category":"Rajasthani","price":99,"description":"Rajasthani classic platter","emoji":"🍛"},
    {"name":"Mirchi Vada","category":"Rajasthani","price":40,"description":"Stuffed and fried chilli","emoji":"🌶️"},
    {"name":"Ghewar","category":"Rajasthani","price":65,"description":"Traditional Rajasthani sweet","emoji":"🍯"},
    {"name":"Pyaaz Paratha","category":"North Indian","price":65,"description":"Onion-stuffed paratha","emoji":"🫓"},
    {"name":"Bedmi Puri","category":"North Indian","price":70,"description":"Spiced lentil puri","emoji":"🫓"},
    {"name":"Aloo Puri","category":"North Indian","price":70,"description":"Potato curry with puri","emoji":"🍛"},
    {"name":"Papdi Chaat","category":"Chaat","price":50,"description":"Crispy papdi with chutneys","emoji":"🥗"},
    {"name":"Dahi Puri","category":"Chaat","price":50,"description":"Puris filled with yogurt and chutneys","emoji":"🥣"},
    {"name":"Dahi Bhalla","category":"Chaat","price":60,"description":"Lentil dumplings with yogurt","emoji":"🥣"},
    {"name":"Aloo Chaat","category":"Chaat","price":45,"description":"Tangy spiced potato chaat","emoji":"🥔"},
    {"name":"Basket Chaat","category":"Chaat","price":75,"description":"Crispy edible basket chaat","emoji":"🥗"},
    {"name":"Ram Ladoo","category":"Chaat","price":45,"description":"Delhi-style lentil fritters","emoji":"🍘"},
    {"name":"Palak Chaat","category":"Chaat","price":60,"description":"Crispy spinach chaat","emoji":"🥬"},
    {"name":"Chana Chaat","category":"Chaat","price":50,"description":"Tangy chickpea chaat","emoji":"🥗"},
    {"name":"Jhal Muri","category":"Bengali","price":40,"description":"Kolkata-style puffed rice snack","emoji":"🥗"},
    {"name":"Kathi Roll","category":"Kolkata","price":85,"description":"Street-style vegetable kathi roll","emoji":"🌯"},
    {"name":"Puchka","category":"Bengali","price":45,"description":"Bengali-style pani puri","emoji":"🥣"},
    {"name":"Ghugni Chaat","category":"Bengali","price":50,"description":"Yellow-pea curry snack","emoji":"🍲"},
    {"name":"Luchi Aloo Dum","category":"Bengali","price":85,"description":"Bengali luchi with potato curry","emoji":"🍛"},
    {"name":"Momos Fried","category":"Street Food","price":80,"description":"Crispy fried vegetable momos","emoji":"🥟"},
    {"name":"Chilli Potato","category":"Indo-Chinese","price":85,"description":"Crispy potatoes in chilli sauce","emoji":"🥔"},
    {"name":"Spring Roll","category":"Indo-Chinese","price":70,"description":"Crispy vegetable spring rolls","emoji":"🌯"},
    {"name":"Hakka Noodles","category":"Indo-Chinese","price":90,"description":"Street-style Hakka noodles","emoji":"🍜"},
    {"name":"Schezwan Fried Rice","category":"Indo-Chinese","price":99,"description":"Spicy Schezwan fried rice","emoji":"🍚"},
    {"name":"Chilli Paneer","category":"Indo-Chinese","price":99,"description":"Paneer tossed in chilli sauce","emoji":"🍲"},
    {"name":"Bread Pakora","category":"Street Food","price":30,"description":"Crispy stuffed bread pakora","emoji":"🍞"},
    {"name":"Onion Pakora","category":"Street Food","price":35,"description":"Crispy onion fritters","emoji":"🧅"},
    {"name":"Paneer Pakora","category":"Street Food","price":65,"description":"Paneer fritters","emoji":"🧀"},
    {"name":"Aloo Bonda","category":"Street Food","price":30,"description":"South Indian potato bonda","emoji":"🥔"},
    {"name":"Vada Pav Cheese","category":"Maharashtra","price":40,"description":"Cheese-loaded vada pav","emoji":"🥪"},
    {"name":"Dahi Vada","category":"Street Food","price":55,"description":"Lentil vada with yogurt","emoji":"🥣"},
    {"name":"Kulfi","category":"Desserts","price":40,"description":"Traditional Indian kulfi","emoji":"🍦"},
    {"name":"Rabri","category":"Desserts","price":60,"description":"Thickened sweetened milk","emoji":"🍮"},
    {"name":"Rasgulla","category":"Bengali","price":35,"description":"Soft Bengali cottage-cheese sweet","emoji":"🍡"},
    {"name":"Sandesh","category":"Bengali","price":45,"description":"Bengali milk-based sweet","emoji":"🍬"},
    {"name":"Malpua","category":"Rajasthani","price":50,"description":"Sweet fried pancake","emoji":"🥞"},
    {"name":"Kesar Lassi","category":"Drinks","price":60,"description":"Chilled saffron lassi","emoji":"🥛"},
    {"name":"Masala Chaas","category":"Drinks","price":30,"description":"Spiced buttermilk","emoji":"🥛"},
    {"name":"Sugarcane Juice","category":"Drinks","price":35,"description":"Fresh sugarcane juice","emoji":"🥤"},
    {"name":"Masala Chai","category":"Drinks","price":20,"description":"Indian spiced tea","emoji":"☕"},
    {"name":"Filter Coffee","category":"Drinks","price":30,"description":"South Indian filter coffee","emoji":"☕"},
    {"name":"Mango Lassi","category":"Drinks","price":60,"description":"Refreshing mango yogurt drink","emoji":"🥭"},
    {"name":"Pav Sandwich","category":"Sandwich","price":60,"description":"Mumbai-style stuffed pav sandwich","emoji":"🥪"},
    {"name":"Frankie Roll","category":"Street Food","price":75,"description":"Indian-style stuffed frankie roll","emoji":"🌯"},
    {"name":"Paneer Frankie","category":"Street Food","price":90,"description":"Paneer frankie roll","emoji":"🌯"},
    {"name":"Egg Roll","category":"Kolkata","price":75,"description":"Kolkata-style egg roll","emoji":"🌯"},
    {"name":"Chicken Frankie","category":"Street Food","price":99,"description":"Chicken-filled frankie roll","emoji":"🌯"},
    {"name":"Chicken Momos","category":"Street Food","price":99,"description":"Steamed chicken momos","emoji":"🥟"},
    {"name":"Egg Bhurji Pav","category":"Maharashtra","price":75,"description":"Spiced egg bhurji with pav","emoji":"🍳"},
    {"name":"Chicken Kathi Roll","category":"Kolkata","price":99,"description":"Chicken-filled kathi roll","emoji":"🌯"},
]

plans = {
    "Daily Thali (1 Day)": 120,
    "2-Day Thali Plan": 240,
    "Weekly Membership": 500,
    "Monthly Membership": 1800
}

# ---------- BRAND HEADER ----------
st.markdown("""
<div class="hero"><h1>🚌 FOOD BUS</h1><p>Good Food. Great Value. Easy Ordering.</p></div>
""", unsafe_allow_html=True)

st.sidebar.title("🚌 FOOD BUS")
page = st.sidebar.radio("Navigation", ["Home", "Food Menu", "My Cart", "Mess Membership", "My Orders"])

if page == "Home":
    st.markdown("""
    <div class="ad-strip"><span>🚌 FOOD BUS • Pocket-friendly Indian street food • Freshly prepared favourites • Dosa, Idli, Dhokla, Vadapav, Pizza, Burgers, Chaat & More • Daily Thali ₹120 • Weekly Membership ₹500 • Monthly Membership ₹1800 • FOOD BUS — Good Food, Great Value! 🚌</span></div>
    """, unsafe_allow_html=True)
    st.title("Welcome to FOOD BUS!")
    st.subheader("Your Food, Your Choice.")
    st.write("Explore popular Indian street food and affordable meal plans.")
    c1, c2 = st.columns(2)
    with c1:
        st.info("🍕 FOOD ORDERING")
        st.write("Pizza, burgers, regional Indian snacks, South Indian dishes, Chinese and more.")
        if st.button("Explore Food Menu", key="home_menu"):
            st.session_state.category = "All"
            st.rerun()
    with c2:
        st.info("🍱 MESS MEMBERSHIP")
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
    visible_terms = "".join(f"<span>{term}</span>" for term in search_terms)
    scroll_count = len(search_terms)
    st.markdown(f"""<style>.search-rotate {{ animation:foodscroll {scroll_count * 2}s steps({scroll_count}) infinite; }} @keyframes foodscroll {{ to {{ transform:translateY(-{scroll_count * 1.5}em); }} }}</style>""", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="search-hint">Search for
      <span class="search-rotate">{visible_terms}</span>
    </div>
    """, unsafe_allow_html=True)
    search = st.text_input("Search food", placeholder="Type a food name...", label_visibility="collapsed")
    categories = ["All"] + list(dict.fromkeys(item["category"] for item in menu))
    st.write("**Categories**")
    category_cols = st.columns(4)
    for i, category in enumerate(categories):
        with category_cols[i % 4]:
            if st.button(category, key="cat_" + category, use_container_width=True):
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
    cols = st.columns(3)
    for index, item in enumerate(filtered_menu):
        with cols[index % 3]:
            with st.container(border=True):
                st.markdown(f"<div class='food-photo-slot'>{item['emoji']}</div>", unsafe_allow_html=True)
                st.markdown(f"<h3 class='food-title'>{item['name']}</h3>", unsafe_allow_html=True)
                st.write(item["description"])
                st.markdown(f"<div class='food-price'>₹{item['price']}</div>", unsafe_allow_html=True)
                if st.button("Add to Cart", key="add_" + item["name"], use_container_width=True):
                    name = item["name"]
                    st.session_state.cart[name] = st.session_state.cart.get(name, 0) + 1
                    st.success("Added to cart!")
                    st.rerun()

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
                    st.write("Items:", order["items"])
                    st.write("Total: ₹", order["total"])
                else:
                    st.write("Plan:", order["plan"])
                    st.write("Price: ₹", order["price"])

st.divider()
st.caption("FOOD BUS | Food Ordering & Mess Membership")
st.caption("Demo Version 3 • Demo prices; actual food photos and persistent database are future updates")
