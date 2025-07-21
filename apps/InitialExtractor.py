# Filename: InitialExtractor.py

import streamlit as st

def extract_initials(full_name):
    words = full_name.strip().split()
    initials = [word[0].upper() for word in words if word]
    return ''.join(initials)

def app():
    st.title("🔡 Initial Extractor")
    st.write("Enter a full name and extract the initials (e.g., John Doe → JD)")

    full_name = st.text_input("✍️ Enter your full name:")

    if full_name:
        result = extract_initials(full_name)
        st.success(f"✅ Initials: {result}")
