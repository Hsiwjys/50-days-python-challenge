# VowelCounter.py

import streamlit as st

def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)

def app():
    st.title("🔡 Vowel Counter App")
    st.write("Enter a sentence below, and I’ll count how many vowels are in each word.")

    sentence = st.text_input("Enter your sentence here:")

    if sentence:
        words = sentence.split()
        total_vowel_count = 0

        st.markdown("### 📋 Vowel Count per Word")
        for word in words:
            vowel_count = count_vowels(word)
            total_vowel_count += vowel_count
            st.write(f"**{word}** → vowels: {vowel_count}")

        st.markdown(f"---\n### 🔢 Total Vowels in Sentence: `{total_vowel_count}`")

if __name__ == "__main__":
    app()
