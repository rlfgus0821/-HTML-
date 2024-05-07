import pandas as pd
import numpy as np
import ast
import streamlit as st
import folium
from haversine import haversine
from streamlit_folium import st_folium

df1 = pd.read_csv('pages/전처리데이터/제주도1.csv')

landmark = pd.read_csv('pages/전처리데이터/관광지_위경도.csv')
landmark.set_index('지역_구역', inplace=True)

col1, col2 = st.columns(2)
col1.markdown('지역을 선택해주세요!')
region = col1.selectbox('지역을 선택하세요',
             options=['서울', '경기', '강원', '제주', '세종', '경남', '경북', '광주', '대구', '대전', '부산', '울산', '인천', '전남', '전북', '충남', '충북'],
                      index=0,
                      placeholder='지역을 선택해주세요',
                      label_visibility='collapsed')

col2.markdown('관광지를 선택해주세요!')
site = col2.selectbox('관광지를 선택하세요',
             options=landmark.loc[region],
                      index=0,
                      placeholder='지역을 선택해주세요',
                      label_visibility='collapsed')

hotels = {}
for _, row in df1.iterrows():
    name = row['hotel_name']
    latitude = row['위도']
    longitude = row['경도']
    hotels[name] = (latitude,longitude)

tourist_spots = {}
for _, row in landmark.loc[region].iterrows():
    name = row['관광지']
    latitude = row['위도']
    longitude = row['경도']
    tourist_spots[name] = (latitude,longitude)

#

def find_hotels_nearby(tourist_spot, distance, hotels):
    nearby_hotels = []
    for hotel, coord in hotels.items():
       if haversine(tourist_spot, coord, unit = 'km') <= distance:
            nearby_hotels.append((hotel, coord))
    return nearby_hotels

# 선택한 관광지와 거리 입력
# site = "비자림" # selectbox 정보 가져오기
x = st.select_slider('원하는 거리를 선택해주세요! (단위 : km)',
                 options=np.arange(1,31))
st.write('당신이 선택한 거리는', x)


# Folium 지도 생성
m = folium.Map(location=tourist_spots[site], zoom_start=12)

# 관광지 마커 추가
folium.Marker(
    location=tourist_spots[site],
    popup=site,
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(m)
# 관광지 지군 x(km) 반지름의 원
folium.Circle(
    location=tourist_spots[site],
    radius = x * 1000,
    color = 'red',
    fill = False
).add_to(m)

# 선택된 관광지 근처 호텔 마커 추가
nearby_hotels = find_hotels_nearby(tourist_spots[site], x, hotels)
for hotel, coord in nearby_hotels:
    folium.Marker(
        location=coord,
        popup=hotel,
        icon=folium.Icon(color='red', icon='bed')
    ).add_to(m)

st_folium(m)