# Filename: WordReverser.py

import streamlit as st

def reverse_words(sentence):
    words = sentence.strip().split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

def app():
    st.title("🔁 Word Reverser App")
    st.write("Enter a sentence and this app will reverse each word individually.")

    sentence = st.text_input("📝 Enter your sentence:")

    if sentence:
        result = reverse_words(sentence)
        st.success(f"🔄 Reversed Words: {result}")
