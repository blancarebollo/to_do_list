import os
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title='To do list', page_icon="🎄", initial_sidebar_state='collapsed')

url = 'http://localhost:8501/'

CSS = """
h1 {
    color: black;
}
.stApp {
    background-image: url(https://www.freeimages.com/photo/snow-1380912);
    background-size: cover;
}
"""

if st.checkbox('Inject CSS'):
    st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

checkboxes = {
     'Clothes':['Socks🧦', 'Underwear👙', 'Sweaters🧣', 'T-shirts👕', 'Pants👖', 'Xmas🤶🏻', 'Shoes👟'],
     'Toilet':['Makeup💄', 'Perfume👃🏻'],
     'Tech': ['Computer💻', 'Phone📱', 'Chargers🔌', 'Ipad🍫'],
     'Others':['Books📚', 'Gifts🎁']
 }

col1, col2, col3= st.columns([3, 3, 3, ])
with col2:
    st.markdown('# XMAS List')
with col3:
    if st.checkbox('I have it all🎈') == True:
        st.balloons()
    else:
        st.snow()


col1, col2, col3, col4 = st.columns([3, 3, 3, 3])
with col1:
    st.write('## Clothes')
    for checkbox in checkboxes['Clothes']:
        if st.checkbox(checkbox):
            st.write(f'Perfect! You got {checkbox}!')
with col2:
    st.write('## Toilet')
    for checkbox in checkboxes['Toilet']:
        if st.checkbox(checkbox):
            st.write(f'Perfect! You got {checkbox}!')
with col3:
    st.write('## Tech')
    for checkbox in checkboxes['Tech']:
        if st.checkbox(checkbox):
            st.write(f'Perfect! You got {checkbox}!')
with col4:
    st.write('## Others')
    for checkbox in checkboxes['Others']:
        if st.checkbox(checkbox):
            st.write(f'Perfect! You got {checkbox}!')
