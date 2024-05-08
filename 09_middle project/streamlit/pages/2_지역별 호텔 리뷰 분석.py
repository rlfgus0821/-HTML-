import ast
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

def goodbad_wordcloud(region):

    df = pd.read_csv(f'data/wordcloud/{region}_빈도_good.csv')
    df2 = df.set_index('Unnamed: 0').to_dict()['freq']

    df3 = pd.read_csv(f'data/wordcloud/{region}_빈도_bad.csv')
    df4 = df3.set_index('Unnamed: 0').to_dict()['freq']

    if region == '세종':
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
        col2.subheader('<부정 키워드>')
        col2.write('부정적 리뷰 없음')


    else:
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


#

st.header('지역별 호텔 리뷰 분석')
st.divider()
st.markdown('지역을 선택해주세요!')
region = st.selectbox('지역을 선택하세요',
             options=['서울', '경기', '강원', '제주도', '세종', '경남', '경북', '광주', '대구', '대전', '부산', '울산', '인천', '전남', '전북', '충남', '충북'],
                      index=0,
                      placeholder='지역을 선택해주세요',
                      label_visibility='collapsed')


goodbad_wordcloud(region)

st.divider()
st.subheader('긍정 키워드별 호텔 정보')

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
# 딕셔너리에 문자열이 덮혀있어서 제거

def dict(df):
    for i in range(len(df)):
        df.at[i, 'good_keyword_ratio'] = ast.literal_eval(df.at[i, 'good_keyword_ratio'])
        df.at[i, 'services'] = ast.literal_eval(df.at[i, 'services'])
        df.at[i, 'star&reviews'] = ast.literal_eval(df.at[i, 'star&reviews'])
        df.at[i, 'good_keyword_freq'] = ast.literal_eval(df.at[i, 'good_keyword_freq'])
        df.at[i, 'good_keyword'] = ast.literal_eval(df.at[i, 'good_keyword'])
        df.at[i, 'bad_keyword'] = ast.literal_eval(df.at[i, 'bad_keyword'])
    return df
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

def rebuild_review(reviews):
    re_review = []
    for review in reviews:
        re_review.append([review[0], review[2]])
    return re_review

if region == '서울':
    col1, col2, col3 = st.columns([1,2,3],gap='medium')
    with col1:
        keyword = st.selectbox('키워드 선택',options=seoul_keywordlist, placeholder='키워드를 선택하세요!')
    with col2:
        one_sor_freq = freq_topn(seoul,keyword,10)
        hotels = st.selectbox('호텔 선택',options=one_sor_freq['hotel_name'].tolist(),placeholder='호텔을 선택하세요!')
    with col3:
        hotel_name, services, review = click_hotel(seoul, hotels, 3)
        review = rebuild_review(review)
        tab1, tab2, tab3 = st.tabs(["호텔명", "서비스 및 부대시설", "리뷰"])
        with tab1:
            st.subheader("호텔명")
            st.write(hotel_name)

        with tab2:
            st.subheader("서비스 및 부대시설")
            df = pd.DataFrame(services, columns=['서비스 사항'])
            st.dataframe(df, hide_index=True)

        with tab3:
            st.subheader("리뷰")
            df2 = pd.DataFrame(review, columns=['평점', '리뷰내용'])
            st.dataframe(df2, hide_index=True)

if region == '경기':
    col1, col2, col3 = st.columns([1,2,3],gap='medium')
    with col1:
        keyword = st.selectbox('키워드 선택',options=gg_keywordlist, placeholder='키워드를 선택하세요!')
    with col2:
        one_sor_freq = freq_topn(gg,keyword,10)
        hotels = st.selectbox('호텔 선택',options=one_sor_freq['hotel_name'].tolist(),placeholder='호텔을 선택하세요!')
    with col3:
        hotel_name, services, review = click_hotel(gg, hotels, 3)
        review = rebuild_review(review)
        tab1, tab2, tab3 = st.tabs(["호텔명", "서비스 및 부대시설", "리뷰"])
        with tab1:
            st.subheader("호텔명")
            st.write(hotel_name)

        with tab2:
            st.subheader("서비스 및 부대시설")
            df = pd.DataFrame(services, columns=['서비스 사항'])
            st.dataframe(df, hide_index=True)

        with tab3:
            st.subheader("리뷰")
            df2 = pd.DataFrame(review, columns=['평점', '리뷰내용'])
            st.dataframe(df2, hide_index=True)

if region == '강원':
    col1, col2, col3 = st.columns([1,2,3],gap='medium')
    with col1:
        keyword = st.selectbox('키워드 선택',options=one_keywordlist, placeholder='키워드를 선택하세요!')
    with col2:
        one_sor_freq = freq_topn(one,keyword,10)
        hotels = st.selectbox('호텔 선택',options=one_sor_freq['hotel_name'].tolist(),placeholder='호텔을 선택하세요!')
    with col3:
        hotel_name, services, review = click_hotel(one, hotels, 3)
        review = rebuild_review(review)
        tab1, tab2, tab3 = st.tabs(["호텔명", "서비스 및 부대시설", "리뷰"])
        with tab1:
            st.subheader("호텔명")
            st.write(hotel_name)

        with tab2:
            st.subheader("서비스 및 부대시설")
            df = pd.DataFrame(services, columns=['서비스 사항'])
            st.dataframe(df, hide_index=True)

        with tab3:
            st.subheader("리뷰")
            df2 = pd.DataFrame(review, columns=['평점', '리뷰내용'])
            st.dataframe(df2, hide_index=True)

if region == '제주도':
    col1, col2, col3 = st.columns([1,2,3],gap='medium')
    with col1:
        keyword = st.selectbox('키워드 선택',options=jeju_keywordlist, placeholder='키워드를 선택하세요!')
    with col2:
        one_sor_freq = freq_topn(jeju,keyword,10)
        hotels = st.selectbox('호텔 선택',options=one_sor_freq['hotel_name'].tolist(),placeholder='호텔을 선택하세요!')
    with col3:
        hotel_name, services, review = click_hotel(jeju, hotels, 3)
        review = rebuild_review(review)
        tab1, tab2, tab3 = st.tabs(["호텔명", "서비스 및 부대시설", "리뷰"])
        with tab1:
            st.subheader("호텔명")
            st.write(hotel_name)

        with tab2:
            st.subheader("서비스 및 부대시설")
            df = pd.DataFrame(services, columns=['서비스 사항'])
            st.dataframe(df, hide_index=True)

        with tab3:
            st.subheader("리뷰")
            df2 = pd.DataFrame(review, columns=['평점', '리뷰내용'])
            st.dataframe(df2, hide_index=True)

if region == '세종':
    col1, col2, col3 = st.columns([1,2,3],gap='medium')
    with col1:
        keyword = st.selectbox('키워드 선택',options=sejong_keywordlist, placeholder='키워드를 선택하세요!')
    with col2:
        one_sor_freq = freq_topn(sejong,keyword,10)
        hotels = st.selectbox('호텔 선택',options=one_sor_freq['hotel_name'].tolist(),placeholder='호텔을 선택하세요!')
    with col3:
        hotel_name, services, review = click_hotel(sejong, hotels, 3)
        review = rebuild_review(review)
        tab1, tab2, tab3 = st.tabs(["호텔명", "서비스 및 부대시설", "리뷰"])
        with tab1:
            st.subheader("호텔명")
            st.write(hotel_name)

        with tab2:
            st.subheader("서비스 및 부대시설")
            df = pd.DataFrame(services, columns=['서비스 사항'])
            st.dataframe(df, hide_index=True)

        with tab3:
            st.subheader("리뷰")
            df2 = pd.DataFrame(review, columns=['평점', '리뷰내용'])
            st.dataframe(df2, hide_index=True)

if region == '경남':
    col1, col2, col3 = st.columns([1,2,3],gap='medium')
    with col1:
        keyword = st.selectbox('키워드 선택',options=gnam_keywordlist, placeholder='키워드를 선택하세요!')
    with col2:
        one_sor_freq = freq_topn(gnam,keyword,10)
        hotels = st.selectbox('호텔 선택',options=one_sor_freq['hotel_name'].tolist(),placeholder='호텔을 선택하세요!')
    with col3:
        hotel_name, services, review = click_hotel(gnam, hotels, 3)
        review = rebuild_review(review)
        tab1, tab2, tab3 = st.tabs(["호텔명", "서비스 및 부대시설", "리뷰"])
        with tab1:
            st.subheader("호텔명")
            st.write(hotel_name)

        with tab2:
            st.subheader("서비스 및 부대시설")
            df = pd.DataFrame(services, columns=['서비스 사항'])
            st.dataframe(df, hide_index=True)

        with tab3:
            st.subheader("리뷰")
            df2 = pd.DataFrame(review, columns=['평점', '리뷰내용'])
            st.dataframe(df2, hide_index=True)

if region == '경북':
    col1, col2, col3 = st.columns([1,2,3],gap='medium')
    with col1:
        keyword = st.selectbox('키워드 선택',options=gbook_keywordlist, placeholder='키워드를 선택하세요!')
    with col2:
        one_sor_freq = freq_topn(gbook,keyword,10)
        hotels = st.selectbox('호텔 선택',options=one_sor_freq['hotel_name'].tolist(),placeholder='호텔을 선택하세요!')
    with col3:
        hotel_name, services, review = click_hotel(gbook, hotels, 3)
        review = rebuild_review(review)
        tab1, tab2, tab3 = st.tabs(["호텔명", "서비스 및 부대시설", "리뷰"])
        with tab1:
            st.subheader("호텔명")
            st.write(hotel_name)

        with tab2:
            st.subheader("서비스 및 부대시설")
            df = pd.DataFrame(services, columns=['서비스 사항'])
            st.dataframe(df, hide_index=True)

        with tab3:
            st.subheader("리뷰")
            df2 = pd.DataFrame(review, columns=['평점', '리뷰내용'])
            st.dataframe(df2, hide_index=True)

if region == '광주':
    col1, col2, col3 = st.columns([1,2,3],gap='medium')
    with col1:
        keyword = st.selectbox('키워드 선택',options=gj_keywordlist, placeholder='키워드를 선택하세요!')
    with col2:
        one_sor_freq = freq_topn(gj,keyword,10)
        hotels = st.selectbox('호텔 선택',options=one_sor_freq['hotel_name'].tolist(),placeholder='호텔을 선택하세요!')
    with col3:
        hotel_name, services, review = click_hotel(gj, hotels, 3)
        review = rebuild_review(review)
        tab1, tab2, tab3 = st.tabs(["호텔명", "서비스 및 부대시설", "리뷰"])
        with tab1:
            st.subheader("호텔명")
            st.write(hotel_name)

        with tab2:
            st.subheader("서비스 및 부대시설")
            df = pd.DataFrame(services, columns=['서비스 사항'])
            st.dataframe(df, hide_index=True)

        with tab3:
            st.subheader("리뷰")
            df2 = pd.DataFrame(review, columns=['평점', '리뷰내용'])
            st.dataframe(df2, hide_index=True)

if region == '대구':
    col1, col2, col3 = st.columns([1,2,3],gap='medium')
    with col1:
        keyword = st.selectbox('키워드 선택',options=daegu_keywordlist, placeholder='키워드를 선택하세요!')
    with col2:
        one_sor_freq = freq_topn(daegu,keyword,10)
        hotels = st.selectbox('호텔 선택',options=one_sor_freq['hotel_name'].tolist(),placeholder='호텔을 선택하세요!')
    with col3:
        hotel_name, services, review = click_hotel(daegu, hotels, 3)
        review = rebuild_review(review)
        tab1, tab2, tab3 = st.tabs(["호텔명", "서비스 및 부대시설", "리뷰"])
        with tab1:
            st.subheader("호텔명")
            st.write(hotel_name)

        with tab2:
            st.subheader("서비스 및 부대시설")
            df = pd.DataFrame(services, columns=['서비스 사항'])
            st.dataframe(df, hide_index=True)

        with tab3:
            st.subheader("리뷰")
            df2 = pd.DataFrame(review, columns=['평점', '리뷰내용'])
            st.dataframe(df2, hide_index=True)

if region == '대전':
    col1, col2, col3 = st.columns([1,2,3],gap='medium')
    with col1:
        keyword = st.selectbox('키워드 선택',options=daej_keywordlist, placeholder='키워드를 선택하세요!')
    with col2:
        one_sor_freq = freq_topn(daej,keyword,10)
        hotels = st.selectbox('호텔 선택',options=one_sor_freq['hotel_name'].tolist(),placeholder='호텔을 선택하세요!')
    with col3:
        hotel_name, services, review = click_hotel(daej, hotels, 3)
        review = rebuild_review(review)
        tab1, tab2, tab3 = st.tabs(["호텔명", "서비스 및 부대시설", "리뷰"])
        with tab1:
            st.subheader("호텔명")
            st.write(hotel_name)

        with tab2:
            st.subheader("서비스 및 부대시설")
            df = pd.DataFrame(services, columns=['서비스 사항'])
            st.dataframe(df, hide_index=True)

        with tab3:
            st.subheader("리뷰")
            df2 = pd.DataFrame(review, columns=['평점', '리뷰내용'])
            st.dataframe(df2, hide_index=True)

if region == '부산':
    col1, col2, col3 = st.columns([1,2,3],gap='medium')
    with col1:
        keyword = st.selectbox('키워드 선택',options=busan_keywordlist, placeholder='키워드를 선택하세요!')
    with col2:
        one_sor_freq = freq_topn(busan,keyword,10)
        hotels = st.selectbox('호텔 선택',options=one_sor_freq['hotel_name'].tolist(),placeholder='호텔을 선택하세요!')
    with col3:
        hotel_name, services, review = click_hotel(busan, hotels, 3)
        review = rebuild_review(review)
        tab1, tab2, tab3 = st.tabs(["호텔명", "서비스 및 부대시설", "리뷰"])
        with tab1:
            st.subheader("호텔명")
            st.write(hotel_name)

        with tab2:
            st.subheader("서비스 및 부대시설")
            df = pd.DataFrame(services, columns=['서비스 사항'])
            st.dataframe(df, hide_index=True)

        with tab3:
            st.subheader("리뷰")
            df2 = pd.DataFrame(review, columns=['평점', '리뷰내용'])
            st.dataframe(df2, hide_index=True)

if region == '울산':
    col1, col2, col3 = st.columns([1,2,3],gap='medium')
    with col1:
        keyword = st.selectbox('키워드 선택',options=ulsan_keywordlist, placeholder='키워드를 선택하세요!')
    with col2:
        one_sor_freq = freq_topn(ulsan,keyword,10)
        hotels = st.selectbox('호텔 선택',options=one_sor_freq['hotel_name'].tolist(),placeholder='호텔을 선택하세요!')
    with col3:
        hotel_name, services, review = click_hotel(ulsan, hotels, 3)
        review = rebuild_review(review)
        tab1, tab2, tab3 = st.tabs(["호텔명", "서비스 및 부대시설", "리뷰"])
        with tab1:
            st.subheader("호텔명")
            st.write(hotel_name)

        with tab2:
            st.subheader("서비스 및 부대시설")
            df = pd.DataFrame(services, columns=['서비스 사항'])
            st.dataframe(df, hide_index=True)

        with tab3:
            st.subheader("리뷰")
            df2 = pd.DataFrame(review, columns=['평점', '리뷰내용'])
            st.dataframe(df2, hide_index=True)

if region == '인천':
    col1, col2, col3 = st.columns([1,2,3],gap='medium')
    with col1:
        keyword = st.selectbox('키워드 선택',options=ic_keywordlist, placeholder='키워드를 선택하세요!')
    with col2:
        one_sor_freq = freq_topn(ic,keyword,10)
        hotels = st.selectbox('호텔 선택',options=one_sor_freq['hotel_name'].tolist(),placeholder='호텔을 선택하세요!')
    with col3:
        hotel_name, services, review = click_hotel(ic, hotels, 3)
        review = rebuild_review(review)
        tab1, tab2, tab3 = st.tabs(["호텔명", "서비스 및 부대시설", "리뷰"])
        with tab1:
            st.subheader("호텔명")
            st.write(hotel_name)

        with tab2:
            st.subheader("서비스 및 부대시설")
            df = pd.DataFrame(services, columns=['서비스 사항'])
            st.dataframe(df, hide_index=True)

        with tab3:
            st.subheader("리뷰")
            df2 = pd.DataFrame(review, columns=['평점', '리뷰내용'])
            st.dataframe(df2, hide_index=True)

if region == '전남':
    col1, col2, col3 = st.columns([1,2,3],gap='medium')
    with col1:
        keyword = st.selectbox('키워드 선택',options=jnam_keywordlist, placeholder='키워드를 선택하세요!')
    with col2:
        one_sor_freq = freq_topn(jnam,keyword,10)
        hotels = st.selectbox('호텔 선택',options=one_sor_freq['hotel_name'].tolist(),placeholder='호텔을 선택하세요!')
    with col3:
        hotel_name, services, review = click_hotel(jnam, hotels, 3)
        review = rebuild_review(review)
        tab1, tab2, tab3 = st.tabs(["호텔명", "서비스 및 부대시설", "리뷰"])
        with tab1:
            st.subheader("호텔명")
            st.write(hotel_name)

        with tab2:
            st.subheader("서비스 및 부대시설")
            df = pd.DataFrame(services, columns=['서비스 사항'])
            st.dataframe(df, hide_index=True)

        with tab3:
            st.subheader("리뷰")
            df2 = pd.DataFrame(review, columns=['평점', '리뷰내용'])
            st.dataframe(df2, hide_index=True)

if region == '전북':
    col1, col2, col3 = st.columns([1,2,3],gap='medium')
    with col1:
        keyword = st.selectbox('키워드 선택',options=jbook_keywordlist, placeholder='키워드를 선택하세요!')
    with col2:
        one_sor_freq = freq_topn(jbook,keyword,10)
        hotels = st.selectbox('호텔 선택',options=one_sor_freq['hotel_name'].tolist(),placeholder='호텔을 선택하세요!')
    with col3:
        hotel_name, services, review = click_hotel(jbook, hotels, 3)
        review = rebuild_review(review)
        tab1, tab2, tab3 = st.tabs(["호텔명", "서비스 및 부대시설", "리뷰"])
        with tab1:
            st.subheader("호텔명")
            st.write(hotel_name)

        with tab2:
            st.subheader("서비스 및 부대시설")
            df = pd.DataFrame(services, columns=['서비스 사항'])
            st.dataframe(df, hide_index=True)

        with tab3:
            st.subheader("리뷰")
            df2 = pd.DataFrame(review, columns=['평점', '리뷰내용'])
            st.dataframe(df2, hide_index=True)

if region == '충남':
    col1, col2, col3 = st.columns([1,2,3],gap='medium')
    with col1:
        keyword = st.selectbox('키워드 선택',options=cnam_keywordlist, placeholder='키워드를 선택하세요!')
    with col2:
        one_sor_freq = freq_topn(cnam,keyword,10)
        hotels = st.selectbox('호텔 선택',options=one_sor_freq['hotel_name'].tolist(),placeholder='호텔을 선택하세요!')
    with col3:
        hotel_name, services, review = click_hotel(cnam, hotels, 3)
        review = rebuild_review(review)
        tab1, tab2, tab3 = st.tabs(["호텔명", "서비스 및 부대시설", "리뷰"])
        with tab1:
            st.subheader("호텔명")
            st.write(hotel_name)

        with tab2:
            st.subheader("서비스 및 부대시설")
            df = pd.DataFrame(services, columns=['서비스 사항'])
            st.dataframe(df, hide_index=True)

        with tab3:
            st.subheader("리뷰")
            df2 = pd.DataFrame(review, columns=['평점', '리뷰내용'])
            st.dataframe(df2, hide_index=True)

if region == '충북':
    col1, col2, col3 = st.columns([1,2,3],gap='medium')
    with col1:
        keyword = st.selectbox('키워드 선택',options=cbook_keywordlist, placeholder='키워드를 선택하세요!')
    with col2:
        one_sor_freq = freq_topn(cbook,keyword,10)
        hotels = st.selectbox('호텔 선택',options=one_sor_freq['hotel_name'].tolist(),placeholder='호텔을 선택하세요!')
    with col3:
        hotel_name, services, review = click_hotel(cbook, hotels, 3)
        review = rebuild_review(review)
        tab1, tab2, tab3 = st.tabs(["호텔명", "서비스 및 부대시설", "리뷰"])
        with tab1:
            st.subheader("호텔명")
            st.write(hotel_name)

        with tab2:
            st.subheader("서비스 및 부대시설")
            df = pd.DataFrame(services, columns=['서비스 사항'])
            st.dataframe(df, hide_index=True)

        with tab3:
            st.subheader("리뷰")
            df2 = pd.DataFrame(review, columns=['평점', '리뷰내용'])
            st.dataframe(df2, hide_index=True)