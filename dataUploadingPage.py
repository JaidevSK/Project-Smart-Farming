# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 11:12:46 2023

@author: jaide
"""
import streamlit as st
import time

st.title("Project Smart Farming")
st.header("Upload the Field images on this page")

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
