import streamlit as st


st.set_page_config(
    page_title='Hotel Review Analysis',
    page_icon=':hotel:',
    layout='wide',
    initial_sidebar_state='auto'
)

st.header(':airplane_departure:호텔 리뷰 분석:running:')
st.divider()

st.balloons()

with st.chat_message("user"):
    st.write("안녕하세요 👋 뭘 보여주려고 하나요?")
    st.write('''호텔 영업을 하는 사업자 또는 호텔 영업을 계획중인 예비 창업자를 위해,   
    마케팅 전략에 도움이 될 수 있도록 국내 호텔의 리뷰 데이터를 분석할거에요!''')
      
    st.write('''**전국 호텔 리뷰 분석** 에서는, 국내 모든 호텔의 리뷰를 분석하여 가장 많이 언급된 키워드가 무엇인지 보여주고자 합니다  
    **지역별 호텔 리뷰 분석** 에서는, 국내 지역을 시 단위로 나누어 각 지역별 호텔의 리뷰를 분석하여  
    가장 많이 언급된 키워드가 무엇인지 보여주고, 리뷰에서 해당 키워드의 빈도 수가 많은 호텔 정보를 보여주고자 합니다  
    또한 **주요 관광지 근접 호텔** 에서는, 주요 관광지 별로 관광지와 근접한 호텔의 위치와 세부사항 정보를 보여줍니다''')

    st.page_link('pages/1_전국 호텔 리뷰 분석.py', label='*전국 호텔 리뷰 분석 페이지로 이동*')
    st.page_link('pages/2_지역별 호텔 리뷰 분석.py', label='*지역별 호텔 리뷰 분석 페이지로 이동*')
    st.page_link('pages/3_주요 관광지 근접 호텔.py', label='*주요 관광지 근접 호텔 페이지로 이동*')

with st.chat_message("user"):
    st.write("분석 대상이 뭔지 궁금합니다")
    st.write('''국내 호텔 총 767개의 호텔 정보와 34,434개의 리뷰 정보를 대상으로 분석했습니다!''')

with st.chat_message("user"):
    st.write("많은 도움이 될 것 같네요 :smile:")
    st.write('''더 나아가 호텔 운영자 뿐만 아니라,  
    이용자들에게도 호텔을 선택할 때 참고할 수 있는 정보가 되기를 기대합니다:fire:''')
    st.image('https://www.wyndhamhotels.com/content/dam/creative-images/apac/flat/1x1/apac_1x1_57994_gr__kien_giang_province.jpg?downsize=700:*')