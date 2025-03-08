import streamlit as st
import validators
import requests
from bs4 import BeautifulSoup

st.title('Content Extractor Website')

with st.form("my_form"):
    weburl = st.text_input("Enter your WebURL:")
    submit_button = st.form_submit_button("Submit")

if submit_button:
    if validators.url(weburl) is True:
        st.write(weburl)
    else:
        st.write("Invalid URL")