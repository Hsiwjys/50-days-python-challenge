import streamlit as st

def app():
    st.set_page_config(page_title="📊 Grade Average Checker", layout="centered")
    st.title("📘 Grade Average Checker")

    # Number of subjects
    n = st.number_input("Enter number of test scores:", min_value=1, step=1)

    # Input scores
    scores = []
    for i in range(n):
        score = st.number_input(
            f"Enter score {i+1}:", min_value=0.0, max_value=100.0, key=f"score_{i}"
        )
        scores.append(score)

    # Button to calculate average
    if st.button("Calculate Average"):
        if len(scores) > 0:
            average = sum(scores) / n
            result = "✅ Pass" if average >= 40 else "❌ Fail"
            st.subheader(f"📈 Average Score: `{average:.2f}`")
            if average >= 40:
                st.success(result)
            else:
                st.error(result)
