import streamlit as st
from datetime import datetime

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(page_title="FOOD BUS", page_icon="🍔", layout="wide")

# ---------------- CUSTOM DESIGN ----------------
st.markdown("""
<style>
.stApp { background: #e8f5e9; }
.block-container { padding-top: 1.5rem; max-width: 1200px; }
h1, h2, h3 { color: #176b3a; }
.food-title { color: #e83e8c !important; font-weight: 800; }
.food-price { color: #111111; font-weight: 800; font-size: 1.15rem; }
div.stButton > button {
    background: #168342; color: white; border: 0; border-radius: 12px;
    font-weight: 700; min-height: 2.6rem;
}
div.stButton > button:hover { background: #0e6330; color: white; border: 0; }
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: white; border-radius: 16px; border: 1px solid #d8eadb;
    padding: 10px;
}
div[data-testid="stTextInput"] input { border-radius: 12px; }
.hero {
    background: linear-gradient(110deg, #126b39, #36a765);
    padding: 28px; border-radius: 20px; color: white; margin-bottom: 18px;
}
.hero h1 { color: white; margin: 0; }
.hero p { color: #f0fff4; margin-bottom: 0; }
.search-hint { color: #176b3a; font-weight: 700; margin: 2px 0 6px 2px; }
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION DATA ----------------
if "cart" not in st.session_state:
    st.session_state.cart = {}
if "orders" not in st.session_state:
    st.session_state.orders = []
if "memberships" not in st.session_state:
    st.session_state.memberships = []
if "category" not in st.session_state:
    st.session_state.category = "All"

# ---------------- FOOD MENU ----------------
menu = [
    {"name": "Veg Pizza", "category": "Pizza", "price": 99, "description": "Delicious vegetable pizza", "emoji": "🍕"},
    {"name": "Cheese Pizza", "category": "Pizza", "price": 149, "description": "Cheese loaded pizza", "emoji": "🍕"},
    {"name": "Mayo Pizza", "category": "Pizza", "price": 139, "description": "Creamy mayo pizza", "emoji": "🍕"},
    {"name": "Corn Pizza", "category": "Pizza", "price": 129, "description": "Sweet corn and cheese pizza", "emoji": "🍕"},
    {"name": "Paneer Pizza", "category": "Pizza", "price": 159, "description": "Paneer topped pizza", "emoji": "🍕"},
    {"name": "Veg Burger", "category": "Burger", "price": 59, "description": "Fresh veg burger", "emoji": "🍔"},
    {"name": "Cheese Burger", "category": "Burger", "price": 89, "description": "Cheese burger", "emoji": "🍔"},
    {"name": "Non-Veg Burger", "category": "Burger", "price": 119, "description": "Classic non-veg burger", "emoji": "🍔"},
    {"name": "Vadapav", "category": "Vadapav", "price": 25, "description": "Mumbai-style vadapav", "emoji": "🥪"},
    {"name": "Manchurian", "category": "Chinese", "price": 99, "description": "Spicy Manchurian", "emoji": "🥡"},
    {"name": "Veg Noodles", "category": "Chinese", "price": 89, "description": "Street-style veg noodles", "emoji": "🍜"},
    {"name": "Pizza Combo", "category": "Combos", "price": 199, "description": "Pizza with a refreshing drink", "emoji": "🍕"},
    {"name": "Mojito", "category": "Drinks", "price": 59, "description": "Refreshing mint cooler", "emoji": "🥤"},
    {"name": "Ice Cream", "category": "Desserts", "price": 49, "description": "Creamy ice cream", "emoji": "🍨"},
    {"name": "Veg Pulao", "category": "Meals", "price": 89, "description": "Aromatic vegetable pulao", "emoji": "🍚"},
    {"name": "Veg Thali", "category": "Meals", "price": 89, "description": "Complete vegetarian thali", "emoji": "🍱"},
    {"name": "Non-Veg Thali", "category": "Meals", "price": 159, "description": "Special non-veg thali", "emoji": "🍛"},
]

plans = {
    "2 Days Premium": 299,
    "3 Days Premium": 399,
    "Weekly Membership": 799,
    "Monthly Membership": 2499
}

# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
  <h1>🚌 FOOD BUS</h1>
  <p>Good Food. Great Value. Easy Ordering.</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.title("🚌 FOOD BUS")
page = st.sidebar.radio(
    "Navigation",
    ["Home", "Food Menu", "My Cart", "Mess Membership", "My Orders"]
)

# ---------------- HOME PAGE ----------------
if page == "Home":
    st.title("Welcome to FOOD BUS!")
    st.subheader("Your Food, Your Choice.")
    st.write("Order your favourite food at affordable prices or choose a mess membership plan.")
    c1, c2 = st.columns(2)
    with c1:
        st.info("🍕 FOOD ORDERING")
        st.write("Pizza, burgers, Chinese, meals, drinks and more.")
        if st.button("Explore Food Menu", key="home_menu"):
            st.session_state["go_menu"] = True
            st.rerun()
    with c2:
        st.info("🍱 MESS MEMBERSHIP")
        st.write("Choose from 2-day, 3-day, weekly and monthly plans.")
    st.divider()
    st.subheader("Popular Categories")
    cols = st.columns(4)
    for col, label in zip(cols, ["Pizza", "Burger", "Chinese", "Meals"]):
        with col:
            st.markdown(f"**{label}**")
    st.caption("Affordable food options • Easy ordering • Flexible membership plans")

# ---------------- FOOD MENU PAGE ----------------
elif page == "Food Menu":
    st.title("Explore Our Food Menu")
    st.markdown("""
    <div class="search-hint">
      <span>Search for </span>
      <span class="search-rotate">
        <span>Pizza</span><span>Burger</span><span>Ice Cream</span><span>Vadapav</span>
        <span>Manchurian</span><span>Noodles</span><span>Pizza Combo</span><span>Mojito</span>
        <span>Mayo Pizza</span><span>Corn Pizza</span><span>Paneer Pizza</span><span>Veg Burger</span>
        <span>Non-Veg Burger</span><span>Pulao</span><span>Veg Thali</span><span>Non-Veg Thali</span>
      </span>
    </div>
    <style>
    .search-rotate { display:inline-flex; flex-direction:column; vertical-align:bottom;
      height:1.5em; overflow:hidden; color:#e83e8c; }
    .search-rotate span { height:1.5em; line-height:1.5em; animation: foodscroll 32s steps(16) infinite; }
    @keyframes foodscroll { to { transform:translateY(-24em); } }
    </style>
    """, unsafe_allow_html=True)
    search = st.text_input("Search food", placeholder="Type a food name...", label_visibility="collapsed")
    categories = ["All", "Pizza", "Burger", "Vadapav", "Chinese", "Combos", "Drinks", "Meals", "Desserts"]
    st.write("**Categories**")
    category_cols = st.columns(5)
    for i, category in enumerate(categories):
        with category_cols[i % 5]:
            if st.button(category, key="cat_" + category, use_container_width=True):
                st.session_state.category = category
    selected_category = st.session_state.category
    if selected_category != "All":
        st.caption("Showing: " + selected_category)
    filtered_menu = [
        item for item in menu
        if (selected_category == "All" or item["category"] == selected_category)
        and (search.strip().lower() in item["name"].lower() or search.strip().lower() in item["category"].lower())
    ]
    if not filtered_menu:
        st.warning("No food items found. Try another search.")
    cols = st.columns(3)
    for index, item in enumerate(filtered_menu):
        with cols[index % 3]:
            with st.container(border=True):
                st.markdown(f"<div style='font-size:3rem;text-align:center'>{item['emoji']}</div>", unsafe_allow_html=True)
                st.markdown(f"<h3 class='food-title' style='text-align:center'>{item['name']}</h3>", unsafe_allow_html=True)
                st.write(item["description"])
                st.markdown(f"<div class='food-price'>₹{item['price']}</div>", unsafe_allow_html=True)
                if st.button("Add to Cart", key="add_" + item["name"], use_container_width=True):
                    name = item["name"]
                    st.session_state.cart[name] = st.session_state.cart.get(name, 0) + 1
                    st.success("Added to cart!")
                    st.rerun()

# ---------------- CART PAGE ----------------
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

# ---------------- MESS MEMBERSHIP PAGE ----------------
elif page == "Mess Membership":
    st.title("Mess Membership Plans")
    st.write("Choose a membership according to your stay and needs.")
    for plan_name, price in plans.items():
        with st.container(border=True):
            c1, c2 = st.columns([3, 1])
            with c1:
                st.subheader(plan_name)
                st.write("Flexible food membership plan")
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

# ---------------- MY ORDERS PAGE ----------------
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

# ---------------- FOOTER ----------------
st.divider()
st.caption("FOOD BUS | Food Ordering & Mess Membership")
st.caption("Demo Version 2 • Product photos and database integration are next")
