# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 11:00:30 2022

@author: Dustin.Smith
"""
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_folium import folium_static
from sklearn.cluster import KMeans
import folium

st.write("""
# Clustering Tool Beta Testing
### Created by Dustin Smith
""")