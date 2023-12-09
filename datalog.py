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




st.sidebar.link_button("Go to Data Uploading Page", "https://project-smart-farming-vd6eonndrahxbzdq7sybvv.streamlit.app/")
st.sidebar.link_button("Go to Datalog", "https://project-smart-farming-ynd8tuet7bvfplkmbdmt8t.streamlit.app/")
st.sidebar.link_button("Go to Image Viewer", "https://project-smart-farming-zdgdgxvdjwjhzdjayfsoyj.streamlit.app/")
st.sidebar.link_button("Go to Weed Density Visualiser", "https://project-smart-farming-ztxhdu7jtbbvnpgpujlfdg.streamlit.app/")
st.sidebar.link_button("Go to Yield Prediction Page", "https://project-smart-farming-bbtrh6txamftuhp2svgrf4.streamlit.app/")
st.sidebar.link_button("Go to Soil Suitability Analysis Page", "https://project-smart-farming-rl8ttyplxcidujmvjqzdtt.streamlit.app/")
st.sidebar.link_button("Go to Type-Wise Weed Distribution Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/")
st.sidebar.link_button("Go to Crop Density Distribution Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/")
st.sidebar.link_button("Go to Cotton Bud Lifecycle Stage Distribution Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/")
st.sidebar.link_button("Go to Disease, Pest and Deficiency distribution Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/")
st.sidebar.link_button("Go to  Cotton Bud Counter and Visualiser Page", "https://project-smart-farming-gu7k3hxuvkcajs3jjqbbzo.streamlit.app/")
st.sidebar.link_button("Go to Weather, Prices and other Information Page", "https://mausam.imd.gov.in/imd_latest/contents/satellite.php")
st.sidebar.link_button("Go to Main Page", "https://project-smart-farming-vefkkxyjh72zcdmf4pgzbs.streamlit.app/")


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
