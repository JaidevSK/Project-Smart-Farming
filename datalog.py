# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 11:34:42 2023

@author: jaide
"""


import streamlit as st
st.title("Project Smart Farming")
st.header("Data Log")

datalog = st.form('Data Log')

sentence = datalog.text_input('Enter the Activity performed')
date = datalog.date_input("Enter the Date")
time = datalog.time_input("Enter the Time")
remarks = datalog.text_input("Enter the Remarks")

submit = datalog.form_submit_button("Submit")
if submit:
    st.success('Response Submitted', icon="✅")


import pandas as pd

df = pd.DataFrame(
    {
        "Activity": ["Soil Testing", "Ploughing", "Sowing"],
        "Date": ["9/12/23", "10/12/23", "11/12/23"],
        "Time": ["1 PM", "2 PM", "3 PM"],
        "Remarks": ["Good Soil", "Tractor used", "Cotton sowed"]        
    }
)
st.dataframe(
    df
)
