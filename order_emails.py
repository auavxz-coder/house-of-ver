"""HOUSE OF VÈR order-received emails via the business Gmail SMTP account.
Only send after Supabase confirms that the order has been saved.
Email delivery is best-effort; never treat it as payment verification.
"""
import smtplib
import logging
import ssl
from email.message import EmailMessage
from email.utils import formataddr
import streamlit as st

BUSINESS_EMAIL = "hello.softlyinframe@gmail.com"
logger = logging.getLogger("house_of_ver.order_email")

def _send(recipient, subject, text, password):
    message = EmailMessage()
    message["From"] = formataddr(("HOUSE OF VÈR", BUSINESS_EMAIL))
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(text)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context(), timeout=15) as server:
        server.login(BUSINESS_EMAIL, password)
        server.send_message(message)

def send_order_received(order_id, customer_name, customer_email, phone, instagram,
                        address, emirate, area, quantity, subtotal, delivery, total):
    """Return customer/store delivery outcomes without exposing SMTP credentials."""
    password = str(st.secrets.get("GMAIL_APP_PASSWORD", "")).replace(" ", "").strip()
    if not password:
        logger.warning("Order email: missing Gmail app password configuration")
        return {"configured": False, "customer": False, "store": False, "reasons": {"setup": "missing_app_password"}}
    order = str(order_id)
    customer_text = (
        f"Dear {customer_name},\n\n"
        "Thank you for choosing HOUSE OF VÈR.\n"
        f"We have received your order request: {order}\n\n"
        f"VÈR Eau de Parfum · 100 ml × {quantity}\n"
        f"Perfume subtotal: AED {subtotal:.2f}\n"
        f"Delivery: AED {delivery:.2f}\n"
        f"Current order total: AED {total:.2f}\n\n"
        "ORDER RECEIVED — NOT YET CONFIRMED\n"
        "Payment has not been verified. Choose your payment method in the website. "
        "If you choose Ziina, upload your payment screenshot after paying. "
        "HOUSE OF VÈR will verify the actual payment before confirming your order. "
        "For cash on delivery, the additional AED 5 fee is shown at payment selection, "
        "and the store will contact you to confirm delivery.\n\n"
        "Please keep your order number. We may contact you through Instagram, email or phone.\n"
        "HOUSE OF VÈR · THE ESSENCE OF PRESENCE\n"
    )
    admin_text = (
        "NEW ORDER REQUEST — PAYMENT NOT VERIFIED\n\n"
        f"Order: {order}\nName: {customer_name}\nEmail: {customer_email}\n"
        f"Phone: {phone}\nInstagram: @{instagram.lstrip('@')}\n"
        f"Address: {address}\nEmirate: {emirate}\nArea: {area}\n"
        f"VÈR Eau de Parfum · 100 ml × {quantity}\n"
        f"Subtotal: AED {subtotal:.2f}\nDelivery: AED {delivery:.2f}\n"
        f"Initial total: AED {total:.2f}\n\n"
        "Open the private admin dashboard to verify payment and process this order.\n"
        "Do not mark paid based on this email or a screenshot alone.\n"
    )
    outcome = {"configured": True, "customer": False, "store": False, "reasons": {}}
    for kind, recipient, subject, body in (
        ("store", BUSINESS_EMAIL, f"New HOUSE OF VÈR order · {order}", admin_text),
        ("customer", customer_email, f"HOUSE OF VÈR · Order received · {order}", customer_text),
    ):
        try:
            _send(recipient, subject, body, password)
            outcome[kind] = True
            logger.info("Order email accepted by SMTP: type=%s", kind)
        except smtplib.SMTPAuthenticationError:
            outcome["reasons"][kind] = "authentication_rejected"
            logger.error("Order email failed: type=%s reason=authentication", kind)
        except smtplib.SMTPRecipientsRefused:
            outcome["reasons"][kind] = "recipient_rejected"
            logger.error("Order email failed: type=%s reason=recipient", kind)
        except smtplib.SMTPException:
            outcome["reasons"][kind] = "smtp_rejected"
            logger.error("Order email failed: type=%s reason=smtp", kind)
        except OSError:
            outcome["reasons"][kind] = "network_unavailable"
            logger.error("Order email failed: type=%s reason=network", kind)
    return outcome
