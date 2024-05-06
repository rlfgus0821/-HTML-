import pandas as pd
import numpy as np
import ast
import streamlit as st

cnam = pd.read_csv('pages/전처리데이터/충남1.csv')
one = pd.read_csv('pages/전처리데이터/강원1.csv')
gg = pd.read_csv('pages/전처리데이터/경기1.csv')
ic = pd.read_csv('pages/전처리데이터/인천1.csv')
cbook = pd.read_csv('pages/전처리데이터/충북1.csv')
jeju = pd.read_csv('pages/전처리데이터/제주도1.csv')
seoul = pd.read_csv('pages/전처리데이터/서울1.csv')
gnam = pd.read_csv('pages/전처리데이터/경남1.csv')
gbook = pd.read_csv('pages/전처리데이터/경북1.csv')
daegu = pd.read_csv('pages/전처리데이터/대구1.csv')
daej = pd.read_csv('pages/전처리데이터/대전1.csv')
busan = pd.read_csv('pages/전처리데이터/부산1.csv')
sejong = pd.read_csv('pages/전처리데이터/세종1.csv')
ulsan = pd.read_csv('pages/전처리데이터/울산1.csv')
jnam = pd.read_csv('pages/전처리데이터/전남1.csv')
jbook = pd.read_csv('pages/전처리데이터/전북1.csv')
gj = pd.read_csv('pages/전처리데이터/광주1.csv')

# 1. 딕셔너리에 문자열이 덮혀있어서 제거
def dict(df):
    for i in range(len(df)):
        df.at[i, 'good_keyword_ratio'] = ast.literal_eval(df.at[i, 'good_keyword_ratio'])
        df.at[i, 'services'] = ast.literal_eval(df.at[i, 'services'])
        df.at[i, 'star&reviews'] = ast.literal_eval(df.at[i, 'star&reviews'])
        df.at[i, 'good_keyword_freq'] = ast.literal_eval(df.at[i, 'good_keyword_freq'])
    return df

one_keywordlist = '청결 객실 시설 바다 직원 속초 이용 가격 예약 위치'.split()
cnam_keywordlist = '청결 시설 객실 이용 직원 주변 조식 가격 화장실 주차'.split()
gg_keywordlist = '청결 객실 직원 이용 시설 주변 주차 침대 조식 가격'.split()
ic_keywordlist = '청결 객실 시설 직원 이용 주변 가격 주차 체크 근처'.split()
cbook_keywordlist = '청결 객실 시설 직원 이용 주변 조식 청주 예약 생각'.split()
jeju_keywordlist = '청결 직원 가격 객실 시설 이용 침대 위치 근처 주차'.split()
seoul_keywordlist = '청결 객실 직원 이용 위치 가격 시설 체크 조식 근처'.split()
gnam_keywordlist = '청결 객실 시설 직원 이용 조식 예약 주변 바다 침대'.split()
gbook_keywordlist = '청결 객실 시설 조식 직원 경주 이용 가격 위치 가족'.split()
daegu_keywordlist = '청결 조식 시설 객실 직원 이용 주변 주차 가격 예약'.split()
daej_keywordlist = '청결 객실 가격 조식 주차 이용 직원 시설 위치 주변'.split()
busan_keywordlist = '청결 객실 직원 위치 바다 이용 가격 시설 해운대 오션'.split()
sejong_keywordlist = '청결 시설 여유 주차 식당 상태 주변 청소 침구 주차공간'.split()
ulsan_keywordlist = '청결 객실 주차 시설 위치 직원 조식 가격 침대 이용'.split()
jnam_keywordlist = '청결 객실 시설 직원 여수 조식 가격 침대 이용 바다'.split()
jbook_keywordlist = '청결 직원 객실 시설 전주 조식 마을 이용 침대 위치'.split()
gj_keywordlist = '청결 조식 시설 직원 객실 이용 주차 침대 가격 주변'.split()
# 모든 지역 진행
lists = cnam, one, gg, ic, cbook, jeju, seoul, gnam, gbook, daegu,daej, busan, sejong, ulsan, jnam, jbook, gj

for i in lists:
    dict(i)

cnam, one, gg, ic, cbook, jeju, seoul, gnam, gbook, daegu,daej, busan, sejong, ulsan, jnam, jbook, gj = lists


def freq_topn(df,keyword,n):
    clean_list = []
    for i in range(len(df['good_keyword_freq'])):
        dict = df.at[i, 'good_keyword_freq']
        if keyword in dict:
            clean_list.append(dict[keyword])
        else:  # keyword 키가 없으면 기본값으로 0을 추가
            clean_list.append(0)
    # 데이터프레임을 정렬
    df_sorted = df.iloc[pd.Series(clean_list).sort_values(ascending=False).index][:n]
    return df_sorted


# TOPn 리뷰 추출
def review_topn(df,hotel_name, n):
    for i in range(len(df)):
        reviews = df[df['hotel_name'] == hotel_name]['star&reviews'].tolist()
        sorted_reviews = sorted(reviews, key=lambda x: x[0], reverse=True)
        result = sorted_reviews[0][:n]
    return result

def click_hotel(df,hotel_name,n):
    hotel = df[df['hotel_name'] == hotel_name]['hotel_name'].iloc[0]
    services = df[df['hotel_name'] == hotel_name]['services'].iloc[0]
    review = review_topn(df,hotel_name,n)
    return hotel, services, review

seoul_sor_freq = freq_topn(seoul,'청결',10)

# 2) multiselect를 이용하여 품종(species)을 선택하면, 해당 품종의 데이터에 대한 데이터프레임으로 표시

col1, col2, col3 = st.columns([1,2,3],gap='medium')

with col1:
    # keyword = st.radio(label="키워드",
    #         key="키워드",
    #         options=one_keywordlist,index=None)
    keyword = st.selectbox('키워드',options=one_keywordlist,placeholder='키워드를 선택하세요!')

with col2:
    one_sor_freq = freq_topn(one,keyword,10)
    hotels = st.selectbox('키워드',options=one_sor_freq['hotel_name'].tolist(),placeholder='호텔을 선택하세요!')
#     hotels = st.radio(label="호텔",
#             key='호텔',
#             options=one_sor_freq['hotel_name'].tolist(),index=None)

with col3:
    hotel_name, services, review = click_hotel(one, hotels, 3)
    tab1, tab2, tab3 = st.tabs(["호텔명", "서비스 및 부대시설", "리뷰"])
    with tab1:
       st.subheader("호텔명")
       st.write(hotel_name)

    with tab2:
       st.subheader("서비스 및 부대시설")
       st.table(services)

    with tab3:
       st.subheader("리뷰")
       st.table(review)
