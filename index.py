import streamlit as st
import validators
import requests
from bs4 import BeautifulSoup
from datetime import datetime

st.title('Content Extractor Website')

with st.form("my_form"):
    weburl = st.text_input("Enter your WebURL:")
    submit_button = st.form_submit_button("Submit")

if submit_button:
    if validators.url(weburl) is True:
        response = requests.get(weburl)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        st.download_button(label="Download",data="text",file_name=datetime.now().strftime("%Y-%m-%d-%H:%M:%S")+".txt")
    else:
        st.write("Invalid URL")