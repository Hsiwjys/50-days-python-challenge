# Filename: SimpleCipher.py

import streamlit as st

def shift_by_one(text):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - base + 1) % 26 + base)
            result += shifted
        else:
            result += char
    return result

def app():
    st.title("🔐 Simple Cipher (Caesar +1)")
    st.write("This tool shifts each letter in your input by **+1** in the alphabet.")

    input_text = st.text_input("🔤 Enter a word or sentence:")

    if input_text:
        cipher_text = shift_by_one(input_text)
        st.success(f"🔑 Ciphered Text: {cipher_text}")
