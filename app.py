import sqlite3
import streamlit as st
from expiry_checker import check_expiry
from ml_model import predict_discount
from notifier import notify_customer

st.set_page_config(
    page_title="Smart Product Expiry Management",
    page_icon="🛒",
    layout="centered"
)

st.title("🛒 Smart Product Expiry Management System")

# Inputs
barcode = st.text_input("📦 Enter Product Barcode:")
customer_email = st.text_input("📧 Enter Customer Email:")

if barcode:
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE barcode=?", (barcode,))
    product = cursor.fetchone()
    conn.close()

    if product:

        barcode, name, expiry_date, price, stock = product

        print(expiry_date)
        print("expiry date")        

        days_left, status = check_expiry(expiry_date)
        discount_level = predict_discount(days_left, stock)

        discount_map = {1: 10, 2: 20, 3: 40}
        discount = discount_map[int(discount_level)]

        # Display product details
        st.subheader(f"🛍️ Product: {name}")
        st.write(f"**Barcode:** {barcode}")
        st.write(f"**Expiry Date:** {expiry_date}")
        st.write(f"**Days Left:** {days_left}")
        st.write(f"**Status:** {status}")
        st.write(f"**Price:** ₹{price}")
        st.write(f"**Stock Available:** {stock}")

        if status == "URGENT":
            st.error(f"🔥 URGENT SALE: {discount}% OFF")
        elif status == "NEAR":
            st.warning(f"⚠️ Near Expiry: {discount}% OFF")
        else:
            st.success(f"✅ Safe Product: {discount}% OFF")

        # Send notification
        if st.button("📩 Send Notification Email"):
            if customer_email:
                notify_customer(name, days_left, discount, customer_email)
            else:
                st.warning("⚠️ Please enter customer email")

    else:
        st.error("❌ Product not found in database!")
