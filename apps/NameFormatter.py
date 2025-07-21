# Filename: NameFormatter.py

import streamlit as st

def format_name(full_name):
    parts = full_name.strip().split()
    if len(parts) < 2:
        return "Please enter at least first and last name."

    first_name = parts[0]
    last_name = parts[-1]
    middle_names = parts[1:-1]

    formats = {
        "First Last": f"{first_name} {last_name}",
        "Last, First": f"{last_name}, {first_name}",
        "Initials": f"{''.join([p[0].upper() for p in parts])}",
        "First M. Last": f"{first_name} {' '.join(m[0] + '.' for m in middle_names)} {last_name}" if middle_names else f"{first_name} {last_name}",
    }

    return formats

def app():
    st.title("🧑‍💼 Name Formatter App")
    full_name = st.text_input("Enter your full name:")

    if full_name:
        results = format_name(full_name)

        if isinstance(results, str):
            st.error(results)
        else:
            st.subheader("📋 Name Formats")
            for label, name_format in results.items():
                st.markdown(f"**{label}**: {name_format}")
