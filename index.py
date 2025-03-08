import streamlit as st
import pandas as pd
import numpy as np

st.title('Content Extractor Website')

with st.form("my_form"):
    user_name = st.text_input("Enter your WebURL:")
    submit_button = st.form_submit_button("Submit")
if submit_button:
    st.write(f"Welcome, {user_name}!") 