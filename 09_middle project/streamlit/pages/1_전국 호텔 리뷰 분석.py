import pandas as pd
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(
    page_title='Hotel Review Analysis',
    page_icon=':hotel:',
    layout='wide',
    initial_sidebar_state='auto'
)
st.header('전국 호텔 리뷰 분석')
st.divider()

with st.container(border=True):
    st.write('''**분석 내용**  
    긍정 키워드 빈도 Top10 : 청결, 객실, 시설, 직원, 이용, 조식, 가격, 위치, 주변, 주차  
    부정 키워드 빈도 Top10 : 객실, 직원, 냄새, 예약, 청소, 시설, 상태, 모텔, 생각, 침대  
      
       
    *통합적으로 청결, 객실, 직원, 시설과 같은 키워드들이 많이 언급됩니다.  
    이를 통해 사람들이 호텔 이용 시 중요하게 생각하는 요소를 알 수 있습니다.*
    ''')


df = pd.read_csv(f'data/wordcloud/전국_빈도_good.csv', encoding='utf-8')
df2 = df.set_index('keyword').to_dict()['freq']

df3 = pd.read_csv(f'data/wordcloud/전국_빈도_bad.csv', encoding='utf-8')
df4 = df3.set_index('keyword').to_dict()['freq']

col1, col2 = st.columns(2)
# font_path = 'C:/Windows/Fonts/malgun.ttf'
wc = WordCloud(width=400, height=400, max_words=50, font_path='fonts/malgun.ttf',
               background_color='white').generate_from_frequencies(df2)

fig = plt.figure(figsize=(8, 8))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
col1.subheader('<긍정 키워드>')
col1.pyplot(fig)

wc2 = WordCloud(width=400, height=400, max_words=50, font_path='fonts/malgun.ttf',
                background_color='white').generate_from_frequencies(df4)

fig = plt.figure(figsize=(8, 8))
plt.imshow(wc2, interpolation='bilinear')
plt.axis('off')
plt.show()
col2.subheader('<부정 키워드>')
col2.pyplot(fig)

st.divider()

col1, col2 = st.columns(2)
col1.subheader('<긍정 키워드 빈도>')
col1.bar_chart(df.iloc[:10], x = 'keyword', y='freq')


col2.subheader('<부정 키워드 빈도>')
col2.bar_chart(df3.iloc[:10], x = 'keyword', y='freq')

col1, col2 = st.columns(2)
col1.markdown('긍정 키워드 Top10')
col1.dataframe(df.iloc[:10], hide_index=True, use_container_width=True)
col2.markdown('부정 키워드 Top10')
col2.dataframe(df3.iloc[:10], hide_index=True, use_container_width=True)