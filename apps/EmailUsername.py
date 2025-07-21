# EmailUsername.py (Streamlit version)

import streamlit as st

def extract_username(email):
    if "@" in email:
        return email.split("@")[0]
    else:
        return "❌ Invalid email address!"

def app():
    st.title("📧 Email Username Extractor")
    st.write("Enter an email address to extract the username (part before `@`).")

    email = st.text_input("Enter your email address")

    if email:
        username = extract_username(email)
        st.success(f"Username: `{username}`")
