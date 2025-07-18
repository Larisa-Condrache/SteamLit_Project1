import streamlit as st
#streamlit run app.py
st.title("Steam Library Manager")

st.write("This is a Streamlit app to demostrate the basics of Streamlit.")
st.header("Welcome to the Streamlit library manager!")
st.subheader("Manage your Steam library with ease.")
st.caption("This app allows you to view and manage your Steam library using the Steamlib library.")

st.markdown("""
## Key Features of Streamlit:" 
"- *Interactive Widgets*: Create interactive elements like sliders, buttons, and text inputs to enhance user interaction.\n"
""")

st.divider()
st.html("<p>This is a simple HTML paragraph.</p>")