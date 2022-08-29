# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 11:00:30 2022

@author: Dustin.Smith
"""
import streamlit as st
import pandas as pd

def ODtool():
    st.write("Hello")

st.sidebar.write("# Help")
st.sidebar.write("For any issues and or errors with the source code, please contact one of the following:")
st.sidebar.write("### Contact Fasil Sagir:")
st.sidebar.markdown('<a href="mailto:fsagir@lochgroup.com">fsagir@lochgroup.com</a>', unsafe_allow_html=True)
st.sidebar.write("### Contact Dustin Smith:")
st.sidebar.markdown('<a href="mailto:dustin.smith@govelis.com">dustin.smith@govelis.com</a>', unsafe_allow_html=True)


st.write("""
# Origin-Destination Matrix Tool
This tool is used to create an Origin-Destination Matrix from Synchro in order to develop VISSIM static routes.
The source code was developed by Fasil Sagir at Lochmueller Group. In order to run the tool, the user will need to export
both a layout.csv and volume.csv from the corresponding Synchro model.
""")

uploaded_file = st.file_uploader("Upload your Volume.csv file:", type=["csv"])
if uploaded_file is not None:
    volume_df = pd.read_csv(uploaded_file,header=0)
    st.write(volume_df)
    
uploaded_file = st.file_uploader("Upload your Layout.csv file:", type=["csv"])
if uploaded_file is not None:
    layout_df = pd.read_csv(uploaded_file,header=0)
    st.write(layout_df)
    
if st.button("Run OD-Tool", ):
    ODtool()
    
st.markdown("##### Disclaimer")
st.markdown("""**_Open source projects are made available and contributed to under licenses that include 
            terms that, for the protection of contributors, make clear that the projects are offered 
            “as-is”, without warranty, and disclaiming liability for damages resulting from using the 
            projects. This guide is no different.Running an open source project, like any human 
            endeavor, involves uncertainty and trade-offs. We hope this guide helps, but it may include
            mistakes, and can’t address every situation. If you have any questions about your project, 
            we encourage you to do your own research, seek out experts, and discuss with your community
            . If you have any legal questions, you should consult with your own legal counsel before 
            moving forward._** """)
