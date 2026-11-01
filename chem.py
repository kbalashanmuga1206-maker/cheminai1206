import streamlit as st

# Page settings
st.set_page_config(
    page_title="My First Website",
    page_icon="🌐",
    layout="centered"
)

# Website title
st.title("🌐 My First Website")

st.write("Welcome! This website is created using Python.")

# User input
name = st.text_input("Enter your name")

# Button
if st.button("Submit"):
    if name:
        st.success(f"Welcome, {name}!")
    else:
        st.warning("Please enter your name.")

# About section
st.header("About")
st.write("""
This is a simple Python web application.
It is created using Streamlit.
""")

# Contact section
st.header("Contact")
st.write("Email: example@gmail.com")

# Footer
st.divider()
st.caption("Created with Python ❤️")
