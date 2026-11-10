import streamlit as st
from datetime import datetime

# ---------------- PAGE SETTINGS ----------------

st.image("food_bus_logo.png", width=250)
    
)

# ---------------- SESSION DATA ----------------

if "cart" not in st.session_state:
    st.session_state.cart = {}

if "orders" not in st.session_state:
    st.session_state.orders = []

if "memberships" not in st.session_state:
    st.session_state.memberships = []

# ---------------- FOOD MENU ----------------

menu = [
    {"name": "Veg Pizza", "category": "Pizza", "price": 99,
     "description": "Delicious vegetable pizza"},
    {"name": "Cheese Pizza", "category": "Pizza", "price": 149,
     "description": "Cheese loaded pizza"},
    {"name": "Veg Burger", "category": "Burger", "price": 59,
     "description": "Fresh veg burger"},
    {"name": "Cheese Burger", "category": "Burger", "price": 89,
     "description": "Cheese burger"},
    {"name": "Veg Meal", "category": "Meals", "price": 89,
     "description": "Complete vegetarian meal"},
    {"name": "Special Thali", "category": "Meals", "price": 129,
     "description": "Special Indian thali"},
    {"name": "Cold Coffee", "category": "Drinks", "price": 49,
     "description": "Chilled cold coffee"},
    {"name": "Fresh Juice", "category": "Drinks", "price": 39,
     "description": "Fresh juice"}
]

# ---------------- MEMBERSHIP PLANS ----------------

plans = {
    "2 Days Premium": 299,
    "3 Days Premium": 399,
    "Weekly Membership": 799,
    "Monthly Membership": 2499
}

# ---------------- COMMON HEADER ----------------

st.title("FOOD BUS")
st.caption("Good Food. Great Value. Easy Ordering.")

st.sidebar.title("FOOD BUS")
page = st.sidebar.radio(
    "Navigation",
    ["Home", "Food Menu", "My Cart",
     "Mess Membership", "My Orders"]
)

# ---------------- HOME PAGE ----------------

if page == "Home":

    st.title("Welcome to FOOD BUS!")

    st.subheader("Your Food, Your Choice.")

    st.write(
        "Order your favourite food at affordable prices "
        "or choose a mess membership plan."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info("FOOD ORDERING")
        st.write("Pizza, Burgers, Meals and Drinks.")
        
    with col2:
        st.info("MESS MEMBERSHIP")
        st.write("2 Days, 3 Days, Weekly and Monthly Plans.")

    st.divider()

    st.subheader("Why FOOD BUS?")
    st.write("Affordable food options")
    st.write("Easy food ordering")
    st.write("Flexible mess membership plans")
    st.write("Simple cart and order management")

# ---------------- FOOD MENU PAGE ----------------

elif page == "Food Menu":

    st.title("Our Food Menu")

    search = st.text_input("Search your favourite food")

    categories = ["All", "Pizza", "Burger", "Meals", "Drinks"]

    selected_category = st.selectbox(
        "Select Category",
        categories
    )

    filtered_menu = []

    for item in menu:
        category_match = (
            selected_category == "All"
            or item["category"] == selected_category
        )

        search_match = (
            search.lower() in item["name"].lower()
        )

        if category_match and search_match:
            filtered_menu.append(item)

    if not filtered_menu:
        st.warning("No food items found.")

    for item in filtered_menu:

        with st.container(border=True):

            col1, col2 = st.columns([3, 1])

            with col1:
                st.subheader(item["name"])
                st.write(item["description"])
                st.write("Category:", item["category"])
                st.write("Price: ₹", item["price"])

            with col2:
                if st.button(
                    "Add to Cart",
                    key="add_" + item["name"]
                ):
                    name = item["name"]

                    st.session_state.cart[name] = (
                        st.session_state.cart.get(name, 0) + 1
                    )

                    st.success("Added to cart!")

# ---------------- CART PAGE ----------------

elif page == "My Cart":

    st.title("My Cart")

    cart = st.session_state.cart

    if not cart:

        st.info("Your cart is empty.")

    else:

        total = 0

        for name, quantity in list(cart.items()):

            item = next(
                (x for x in menu if x["name"] == name),
                None
            )

            if item is None:
                continue

            price = item["price"]
            subtotal = price * quantity
            total += subtotal

            with st.container(border=True):

                col1, col2, col3 = st.columns([3, 1, 1])

                with col1:
                    st.write("**" + name + "**")
                    st.write("₹", price, "each")

                with col2:
                    st.write("Quantity:", quantity)

                with col3:
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
                    "type": "Food Order",
                    "customer": customer_name,
                    "items": dict(st.session_state.cart),
                    "total": total,
                    "date": datetime.now().strftime(
                        "%d-%m-%Y %I:%M %p"
                    )
                }

                st.session_state.orders.append(order)
                st.session_state.cart = {}

                st.success("Demo order placed successfully!")
                st.info("No real payment or delivery has been processed.")

# ---------------- MESS MEMBERSHIP PAGE ----------------

elif page == "Mess Membership":

    st.title("Mess Membership Plans")

    st.write(
        "Choose a membership according to your stay and needs."
    )

    for plan_name, price in plans.items():

        with st.container(border=True):

            col1, col2 = st.columns([3, 1])

            with col1:
                st.subheader(plan_name)
                st.write("Flexible food membership plan")

            with col2:
                st.subheader("₹" + str(price))

    st.divider()

    st.subheader("Select Your Membership")

    selected_plan = st.selectbox(
        "Choose Plan",
        list(plans.keys())
    )

    member_name = st.text_input("Member Name")
    member_phone = st.text_input("Member Phone Number")

    if st.button("Choose Membership"):

        if not member_name or not member_phone:
            st.warning("Please enter your name and phone number.")

        elif not member_phone.isdigit() or len(member_phone) != 10:
            st.warning("Please enter a valid 10-digit phone number.")

        else:
            membership = {
                "type": "Mess Membership",
                "customer": member_name,
                "plan": selected_plan,
                "price": plans[selected_plan],
                "date": datetime.now().strftime(
                    "%d-%m-%Y %I:%M %p"
                )
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

        for index, order in enumerate(
            reversed(st.session_state.orders), start=1
        ):

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
st.caption("Demo Version 1")
