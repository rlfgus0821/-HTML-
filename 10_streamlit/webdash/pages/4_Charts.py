import streamlit as st
import pandas as pd
import numpy as np

st.title('Metric')
st.metric(label='온도', value='23℃', delta='1.2℃')
st.metric(label='체감온도', value='24℃', delta='2℃')
st.metric(label='풍속', value='9mph', delta='-8%')

st.divider()

st.markdown('가로로 보여주기')
col1, col2, col3 = st.columns(3)
col1.metric(label='온도', value='23℃', delta='1.2℃')
col2.metric(label='체감온도', value='24℃', delta='2℃')
col3.metric(label='풍속', value='9mph', delta='-8%')

st.divider()

st.markdown('inverse -> 증가, 감소 색 chage / off -> 색 없애기')
col1, col2, col3 = st.columns(3)
col1.metric(label='체감온도', value='24℃', delta='2℃',
            delta_color='inverse')
col2.metric(label='풍속', value='9mph', delta='-8%',
            delta_color='inverse')
col3.metric(label='온도', value='23℃', delta='1.2℃',
            delta_color='off')

st.divider()
st.title('Chart')
st.header('1. Bar chart')
df = pd.DataFrame(np.random.rand(20,3),
                  columns=list('ABC'))
df2 = pd.DataFrame({'A':list(range(20)),
                   'B':np.random.rand(20),
                   'C':['x']*5 +['y']*5+['z']*5+['s']*5})
st.dataframe(df)

st.markdown('bar Chart')
st.bar_chart(df)
st.bar_chart(df['A'])

st.dataframe(df2)
st.bar_chart(df2, x='A',y='B')
st.bar_chart(df2, x='A',y='B',color='C')
st.bar_chart(df2, x='A',y='B',color='#ff0000')

st.header('2. Line Chart')
st.line_chart(df)

st.header('3. Area Chart')
st.area_chart(df.A)
st.area_chart(df, y=list('ABC'), color=['#ff0033', '#009933','#000066'])

st.header('4. Scatter plot')
st.scatter_chart(df, x='A', y='B')
st.scatter_chart(df, x='A', y='B',color='C')

df['D'] = np.random.choice(list('xyz'), 20)
st.scatter_chart(df, x='A',y='B',color='C', size='D')

st.divider()

st.header('5. Map')
loc = {'강남구청':[37.52579, 127.0483],
        '서초구청':[37.49093, 127.0329],
        '동작구청':[37.51871, 126.9364],
        '구로구청':[37.50237, 126.8890],
        '양천구청' :[37.52007, 126.9549],
        '영등포구청': [37.54240, 126.8402],
        '관악구청': [37.48467, 126.9515],
        '용산구청' :[37.53804, 126.9913],
        '서대문구청': [37.58567, 126.9357],
        '마포구청' : [37.57003, 126.9019],
        '은평구청' : [37.60675, 126.9302],
        '종로구청' : [37.57615, 126.9790],
        '중구청' : [37.56798, 126.9975],
        '성북구청' : [37.59342, 127.0172],
        '동대문구청' : [37.57792, 127.0401],
        '중랑구청' : [37.60961, 127.0931],
        '노원구청' : [37.65664, 127.0559],
        '도봉구청' : [37.67214, 127.0462],
        '강북구청' : [37.64278, 127.0253],
        '광진구청' : [37.54104, 127.0826],
        '강동구청' : [37.53246, 127.1237],
        '송파구청' : [37.51803, 127.105]}
df_loc = pd.DataFrame(loc).T
df_loc.columns=['lat','lon']
st.dataframe(df_loc)

st.map(df_loc, size=20, color='#00ff00', zoom=14)

st.divider()

st.header('6. matplotlib pyplot')
import matplotlib.pyplot as plt

fig , ax = plt.subplots()
ax.hist(df.A)
st.pyplot(fig)

ax.scatter(df.A, df.B)
ax.set_title('Scatterplot')
ax.set_xlabel('A')
ax.set_ylabel('B')
st.pyplot(fig)

import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

st.header('지도시각화: folium')
map = folium.Map(location=[35.574,126.973],zoom_start=10)

mc = MarkerCluster().add_to(map)

for name, lo in loc.items():
    folium.Marker(location= lo,
              popup=folium.Popup(name,max_width=200)).add_to(mc)
st_folium(map, width=600, height=400)

st.divider()

st.markdown('지도 가로로 나열')
c1, c2 = st.columns(2)

m1 = folium.Map([37.574,126.973], zoom_start=9)
m2 = folium.Map([37.574,126.973], zoom_start=8)

with c1:
    st.subheader('지도1')
    st_folium(m1, key='x')

with c2:
    st.subheader('지도2')
    st_folium(m1, key='y')

st.divider()

st.header('경기도 인구데이터 지도 시각화')
import json
with open('../data/경기도행정구역경계.json', encoding='utf-8') as f:
    geo_gg = json.loads(f.read())
df_gg = pd.read_excel('data/경기도인구데이터.xlsx', index_col='구분')

st.dataframe(df_gg)
st.markdown('2007년 경기도 인구데이터')
map = folium.Map(location=[37.5666,126.9782], zoom_start=8)
folium.GeoJson(geo_gg).add_to(map)
folium.Choropleth(geo_data=geo_gg,
                  data=df_gg[2007],
                  columns=[df_gg.index, df_gg[2007]],
                  key_on='feature.properties.name').add_to(map)
st_folium(map, width=600, height=400)