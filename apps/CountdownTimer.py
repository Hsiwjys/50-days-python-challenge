# Filename: CountdownTimer.py

import streamlit as st
import time

def app():
    st.title("⏳ Countdown Timer")
    st.write("Enter a number and watch the countdown to 0.")

    n = st.number_input("🔢 Enter starting number (n):", min_value=0, step=1)

    if st.button("Start Countdown"):
        countdown_placeholder = st.empty()
        for i in range(int(n), -1, -1):
            countdown_placeholder.markdown(f"# ⏱️ {i}")
            time.sleep(1)
        st.success("🎉 Countdown complete!")
