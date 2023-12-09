# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 11:12:46 2023

@author: jaide
"""
import streamlit as st
import time

st.title("Project Smart Farming")
st.header("Upload the Field images on this page")

a1=st.file_uploader("Upload the Field Images taken from altitude 100m", accept_multiple_files=True)
a2=st.file_uploader("Upload the Field Images taken from altitude 50m", accept_multiple_files=True)
a3=st.file_uploader("Upload the Field Images taken from altitude 25m", accept_multiple_files=True)
a4=st.file_uploader("Upload the Field Images taken from altitude 5m", accept_multiple_files=True)
a5=st.file_uploader("Upload the DSLR images", accept_multiple_files=True)

d=st.date_input("Enter today's Date")

s=st.button("Submit, Stitch the Images / Super Resolution the Large image, Run the models on the image and store the results in the database")

if s:
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)
    
    for percent_complete in range(100):
        time.sleep(1)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(20)
    
    st.success('Process Completed', icon="✅")