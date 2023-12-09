# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 14:56:26 2023

@author: jaide
"""


import streamlit as st
st.title("Project Smart Farming")
st.header("Soil Suitability Analysis")
typ = st.radio("How would you like to use this?", ["Soil Suitability Map Generator", "Individual Sample Testing"])

if typ == "Soil Suitability Map Generator":
    st.file_uploader("Input the .csv file of the Field")
else:
    st.number_input("Enter the Value of N")
    st.number_input("Enter the Value of P")
    st.number_input("Enter the Value of K")
    st.number_input("Enter the Value of pH")
    st.number_input("Enter the Value of Salinity")
    st.number_input("Enter the Value of Moisture Content")
    st.number_input("Enter the Value of Temperature")
    s = st.button("Submit")
    if s:
        st.write("The suitability index is 0.8")
        st.write("The range is 0-1. 1 is good; 0 is bad.")
    