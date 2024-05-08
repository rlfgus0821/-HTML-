import streamlit as st
import pandas as pd
import folium
from haversine import haversine
from streamlit_folium import st_folium
import numpy as np

st.set_page_config(
    page_title='Hotel Review Analysis',
    page_icon=':hotel:',
    layout='wide',
    initial_sidebar_state='auto'
)

st.header('주요 관광지 근접 호텔')

st.divider()

@st.cache_data
def load_data():
    cnam = pd.read_csv('data/Top10/충남1.csv')
    one = pd.read_csv('data/Top10/강원1.csv')
    gg = pd.read_csv('data/Top10/경기1.csv')
    ic = pd.read_csv('data/Top10/인천1.csv')
    cbook = pd.read_csv('data/Top10/충북1.csv')
    jeju = pd.read_csv('data/Top10/제주도1.csv')
    seoul = pd.read_csv('data/Top10/서울1.csv')
    gnam = pd.read_csv('data/Top10/경남1.csv')
    gbook = pd.read_csv('data/Top10/경북1.csv')
    daegu = pd.read_csv('data/Top10/대구1.csv')
    daej = pd.read_csv('data/Top10/대전1.csv')
    busan = pd.read_csv('data/Top10/부산1.csv')
    sejong = pd.read_csv('data/Top10/세종1.csv')
    ulsan = pd.read_csv('data/Top10/울산1.csv')
    jnam = pd.read_csv('data/Top10/전남1.csv')
    jbook = pd.read_csv('data/Top10/전북1.csv')
    gj = pd.read_csv('data/Top10/광주1.csv')
    return cnam, one, gg, ic, cbook, jeju, seoul, gnam, gbook, daegu,daej, busan, sejong, ulsan, jnam, jbook, gj

cnam, one, gg, ic, cbook, jeju, seoul, gnam, gbook, daegu,daej, busan, sejong, ulsan, jnam, jbook, gj = load_data()


landmark = pd.read_csv('data/map/관광지_위경도.csv')
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
                      placeholder='관광지를 선택해주세요',
                      label_visibility='collapsed')

mapping_region_dict = { '충남':'cnam', '강원':'one', '경기':'gg', '인천':'ic',
                        '충북':'cbook', '제주':'jeju', '서울':'seoul', '경남':'gnam',
                        '경북':'gbook', '대구':'daegu', '대전':'daej', '부산':'busan',
                        '세종':'sejong', '울산':'ulsan', '전남':'jnam', '전북':'jbook',
                        '광주':'gj'}

select_region = mapping_region_dict[region]
selected_df = globals()[select_region]


# 호텔 위치 정보
hotels = []
for _, row in selected_df.iterrows():
    name = row['hotel_name']
    latitude = row['위도']
    longitude = row['경도']
    hotels.append([name, (latitude,longitude)])

# 관광지 위치 정보
tourist_spots = []
for _, row in landmark.loc[region].iterrows():
    name = row['관광지']
    latitude = row['위도']
    longitude = row['경도']
    tourist_spots.append([name, (latitude,longitude)])


# 관광지 근처 호텔 탐색
def find_hotels_nearby(tourist_spot, distance, hotels):
    nearby_hotels = []
    hotel_names = []
    for hotel_data in hotels:
       if haversine(tourist_spot, hotel_data[1], unit = 'km') <= distance:
           nearby_hotels.append(hotel_data)
           hotel_names.append(hotel_data[0])
    return nearby_hotels, hotel_names

st.write('''
  
  ''')
# 선택한 관광지와 거리 입력
x = int(st.select_slider('원하는 거리를 선택해주세요! (단위 : km)', np.arange(1,31)))

# 관광지 인덱스 체크
idx_tourist = None
for i, spot in enumerate(tourist_spots):
    if spot[0] == site:
        idx_tourist = i
        break

# Folium 지도 생성
m = folium.Map(location = tourist_spots[idx_tourist][1], zoom_start=12)

# 관광지 마커 추가
folium.Marker(
    location = tourist_spots[idx_tourist][1],
    popup=site,
    icon=folium.Icon(color='blue', icon='info-sign')
).add_to(m)

# 관광지 지군 x(km) 반지름의 원
folium.Circle(
    location=tourist_spots[idx_tourist][1],
    radius = x * 1000,
    color = 'red',
    fill = False
).add_to(m)

# 선택된 관광지 근처 호텔 마커 추가
nearby_hotels, nearby_hotels_names = find_hotels_nearby(tourist_spots[idx_tourist][1], x, hotels)
for hotel_data in nearby_hotels:
    folium.Marker(
        location=hotel_data[1],
        popup=folium.Popup(hotel_data[0], max_width=len(hotel_data[0])*50),
        icon=folium.Icon(color='green', icon='glyphicon glyphicon-home')
    ).add_to(m)

st_folium(m, width=800, height=600)

# 근접한 호텔 정보(호텔명, 서비스, 장소)
def hotel_info(df):
    nearby_hotels_df = pd.DataFrame(columns = ['hotel_name','services','location'])
    for names in nearby_hotels_names:
        nearby_hotels_df = pd.concat([nearby_hotels_df,df[df['hotel_name'] == names][['hotel_name', 'services', 'location']].reset_index(drop=True)])
    nearby_hotels_df.reset_index(drop=True, inplace=True)
    hotel = st.selectbox('호텔 목록', options=nearby_hotels_df['hotel_name'].tolist())

    st.divider()
    st.markdown("서비스 및 부대시설")
    st.dataframe(nearby_hotels_df[nearby_hotels_df['hotel_name'] == hotel]['services'], hide_index=True, use_container_width=True)


    st.markdown("위치")
    st.dataframe(nearby_hotels_df[nearby_hotels_df['hotel_name'] == hotel]['location'], hide_index=True, use_container_width=True)

hotel_info(selected_df)
