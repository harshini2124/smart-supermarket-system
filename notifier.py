import smtplib
from email.message import EmailMessage
import streamlit as st

def notify_customer(product_name, days_left, discount, customer_email):
     
    sender_email = "harshini2127@gmail.com"      
    sender_password = "eyfr dpgn bemv hmub"     

    msg = EmailMessage()
    msg["Subject"] = "Product Expiry Alert & Offer"
    msg["From"] = sender_email
    msg["To"] = customer_email

    msg.set_content(
        f"""
Hello Customer,

The product "{product_name}" will expire in {days_left} days.

🎉 Special Offer: {discount}% OFF

Please purchase it soon.

Thank you,
Smart Product Expiry Management System
"""
    )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)

        st.success("📧 Email notification sent successfully!")

    except Exception as e:
        st.error(f"❌ Email failed: {e}")
