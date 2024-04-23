import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# 뉴스 데이터 kor_news_20240326.xlsx를 이용하여 스트림릿으로 구현하기
df = pd.read_excel('data\kor_news_240326.xlsx')

# 1. 뉴스데이터를 dataframe으로 표시하기
st.data_editor(df, use_container_width=True, hide_index=True)
st.divider()
# 2. 뉴스데이터의 url 컬럼을 실제 뉴스기사 페이지로 이동하도록 적절한 column configuration 사용
st.data_editor(df,column_config={'URL': st.column_config.LinkColumn()}, hide_index=True)

# 3. 분류 컬럼 중 대분류 컬럼에 대한 빈도를 bar chart로 그리기
df['대분류'] =[i.split('>')[0] for i in df['분류']]
data = df['대분류'].value_counts()
st.bar_chart(data)

# 4. 제목 컬럼에 대하여 텍스트 전처리를 진행한 결과를 토대로 경제, 사회 분야의 빈도가 많은 주요 키워드 20위를 bar chart로 그리기
