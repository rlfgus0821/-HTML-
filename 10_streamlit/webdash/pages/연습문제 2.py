import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
import seaborn as sns
from konlpy.tag import Okt
from nltk.corpus import stopwords
import folium
import json
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
rc('font', family = font_name)


# 1. iris 데이터 셋을 이용하여
st.header('1. iris Data', divider=True)
iris = pd.DataFrame(sns.load_dataset('iris'))

# 1) iris 데이터 셋을 데이터프레임으로 표시
st.dataframe(iris)

# 2) multiselect를 이용하여 품종(species)을 선택하면, 해당 품종의 데이터에 대한 데이터프레임으로 표시
specie = st.multiselect('품종(species)',iris.species.unique())
st.write(iris.loc[iris['species'].isin(specie)])

# 3) 품종을 제외한 4가지 컬럼을 radio 요소를 사용하여 선택, 선택한 컬럼에 대한 matplotlib을 이용하여 hist() 그리기
col4 = iris.columns[iris.columns != 'species']
columns = st.radio(label='columns', options=col4,horizontal=True,index=2)

fig, ax = plt.subplots()
ax.hist(iris[columns])
st.pyplot(fig)

# 2. kor_news 데이터셋을 이용 / 대분류 기준을 선택하면 해당 분야의 주요 키워드 20위에 대한 bar_chart 표시
st.header('2. Kor_news Data', divider=True)
df = pd.read_excel('data\kor_news_240326.xlsx')
df['대분류'] =[i.split('>')[0] for i in df['분류']]
data = df['대분류'].value_counts()
def news_dist(names, column='제목', n=10):
    okt = Okt()
    stopwords_kr = pd.read_csv('data/한국어 불용어 리스트.csv', encoding='CP949')
    stopwords_list = stopwords_kr.values.tolist()

    # '대분류'로 그룹화
    group_news = df.groupby('대분류')
    stop_words = stopwords_list

    for name, data in group_news:
        if name == names:
            # 그룹별 제목을 합치기
            title = ' '.join(data[column])
            # 단어 토큰화
            word_tokens = okt.pos(title)
            # 명사만 추출 / 1글자 이하 제거 / 불용어 제거
            token_sw = [word for word, tag in word_tokens if len(word) > 1 if tag == 'Noun' if word not in stop_words]
            freq = pd.DataFrame(pd.Series(Counter(token_sw)).sort_values(ascending=False), columns=['freq'])
            print(f'{name}:\n {freq.head(n)}')

            # 바그래프 시각화
            data = freq.iloc[:n]
            st.bar_chart(data)
            plt.title(f'{name}의 TOP{n} 그래프')
            plt.show()

news_dist('경제','본문',20)

# 3. 경기도 인구 데이터 / 연도별 인구수에 대한 지도시각화(2007,2015,2017년 연도를 탭으로 제시)
st.header('3. 경기도 인구 데이터', divider=True)
df_gg = pd.read_excel('data/경기도인구데이터.xlsx', index_col='구분')
st.dataframe(df_gg)

with open('data/경기도행정구역경계.json', encoding='utf-8') as f:
    geo_gg = json.loads(f.read())
df_gg = pd.read_excel('data/경기도인구데이터.xlsx', index_col='구분')

tab1, tab2, tab3 = st.tabs(['2007','2015','2017'])
with tab1:
   st.subheader('2007년 경기도 인구데이터')
   map = folium.Map(location=[37.566, 126.978], zoom_start=8)
   folium.GeoJson(geo_gg).add_to(map)
   folium.Choropleth(geo_data=geo_gg,
                     data=df_gg[2007],
                     columns=[df_gg.index, df_gg[2007]],
                     key_on='feature.properties.name').add_to(map)
   st_folium(map, width=600, height=400)

with tab2:
   st.subheader('2015년 경기도 인구데이터')
   map = folium.Map(location=[37.566, 126.978], zoom_start=8)
   folium.GeoJson(geo_gg).add_to(map)
   folium.Choropleth(geo_data=geo_gg,
                     data=df_gg[2015],
                     columns=[df_gg.index, df_gg[2015]],
                     key_on='feature.properties.name').add_to(map)
   st_folium(map, width=600, height=400)

with tab3:
   st.subheader('2017년 경기도 인구데이터')
   map = folium.Map(location=[37.566, 126.978], zoom_start=8)
   folium.GeoJson(geo_gg).add_to(map)
   folium.Choropleth(geo_data=geo_gg,
                     data=df_gg[2017],
                     columns=[df_gg.index, df_gg[2017]],
                     key_on='feature.properties.name').add_to(map)
   st_folium(map, width=600, height=400)
