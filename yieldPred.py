# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 15:09:00 2023

@author: jaide
"""


import streamlit as st
st.title("Project Smart Farming")
st.header("Yield Prediction based on Weather and Soil Data")

a = st.file_uploader("Upload the csv file of the required parameters")
st.write("""
         ## OR
         """)
b = st.text_area("Write the data of the parameters in comma separated format")

s = st.button("Submit")
if s:
    st.write("The predicted yield is ____ kg per hectare")