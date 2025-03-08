import streamlit as st

st.title('Content Extractor Website')

with st.form("my_form"):
    weburl = st.text_input("Enter your WebURL:")
    submit_button = st.form_submit_button("Submit")

if submit_button:
    st.write(weburl)