# Filename: ListMaximum.py

import streamlit as st

def find_largest_number(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

def app():
    st.title("🔢 List Maximum Finder")
    st.write("Enter a list of numbers (separated by spaces) to find the largest number without using `max()`.")

    user_input = st.text_input("Enter numbers separated by spaces:")
    
    if st.button("Find Maximum"):
        try:
            number_list = [float(n) for n in user_input.strip().split()]
            result = find_largest_number(number_list)
            if result is not None:
                st.success(f"✅ The largest number is: {result}")
            else:
                st.warning("⚠️ The list is empty.")
        except ValueError:
            st.error("❌ Please enter valid numbers separated by spaces.")
