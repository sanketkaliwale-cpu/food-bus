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
.search-rotate span { display:block; height:1.5em; line-height:1.5em; animation:foodscroll 54s steps(27) infinite; }
@keyframes foodscroll { to { transform:translateY(-40.5em); } }
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
    st.markdown(f"""
    <div class="search-hint">Search for
      <span class="search-rotate">{visible_terms}</span>
    </div>
    """, unsafe_allow_html=True)
    search = st.text_input("Search food", placeholder="Type a food name...", label_visibility="collapsed")
    categories = ["All", "Pizza", "Burger", "Maharashtra", "Gujarati", "South Indian", "Chinese", "Street Food", "Combos", "Drinks", "Meals", "Desserts"]
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
