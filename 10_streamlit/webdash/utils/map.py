import pandas as pd
import os
import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter
import seaborn as sns
from konlpy.tag import Okt
import folium
import json
from streamlit_folium import st_folium
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
rc('font', family = font_name)

def load_data(file_path):
    fname, ext = os.path.splitext(file_path)
    if ext in ['xlsx','xls']:
        return pd.read_excel(file_path)
    elif ext == 'csv':
        return pd.read_csv(file_path, encoding='utf-8')


def fmap(year):
    map = folium.Map(location=[37.566, 126.978], zoom_start=8)
    folium.GeoJson(geo_gg).add_to(map)
    folium.Choropleth(geo_data=geo_gg,
                      data=df_gg[year],
                      columns=[df_gg.index, df_gg[year]],
                      key_on='feature.properties.name').add_to(map)
    st_folium(map, width=600, height=400)

tab1, tab2, tab3 = st.tabs(['2007','2015','2017'])
with tab1:
   st.subheader('2007년 경기도 인구데이터')
   fmap(2007)

with tab2:
   st.subheader('2015년 경기도 인구데이터')
   fmap(2015)

with tab3:
   st.subheader('2017년 경기도 인구데이터')
   fmap(2017)