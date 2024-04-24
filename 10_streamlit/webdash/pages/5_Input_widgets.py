import streamlit as st

st.title('Input widgets')
st.header('1. Button elements')

st.subheader('Button', divider=True)
st.markdown('type=secondary(default) / primary -> 색으로 강조')
st.button('초기화', type='primary')
if st.button('안녕', type='secondary'):
    st.write('반가워 :smile:')
else:
    st.write('잘가! :raising_hand:')

st.subheader('Link button', divider=True)
st.markdown('Link button -> 페이지 연결')
st.link_button('google', 'https://www.google.com')

st.subheader('Page link', divider=True)
st.page_link('app.py', label='Home', icon='🏠')
st.page_link('pages/1_Text_elements.py', label='Text elements')
st.page_link('pages/2_Data_elements.py', label='Data elements')
st.page_link('pages/연습문제.py', label='Exercise', disabled=True)
st.page_link('https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/'
             ,label='Emojis', icon='🌝')

st.subheader('Form_Submit_button', divider=True)

with st.form(key='form1'):
    id= st.text_input('Id')
    pw= st.text_input('Password', type='password')
    submitted = st.form_submit_button()
    if submitted:
        st.write('id:', id,'password:',pw)
        
form = st.form(key='form2')
title = form.text_input('제목 / text_input')
contents = form.text_area(('질문입력 / text_area'))
submit = form.form_submit_button('작성 / submit button')
if submit:
    st.write('제목:', title)

st.header('2. Selection elements')
st.subheader('Checkbox', divider=True)

agree = st.checkbox('찬성',value=True)
if agree:
    st.write('Agree!')
else:
    st.write('Disagree!')

st.subheader('Toggle',divider=True)
on = st.toggle('Select')
if on:
    st.write('on')
else:
    st.write('off')

st.subheader('Radio',divider=True)
fruit = st.radio(label='좋아하는 과일은?',
                 options=['바나나','멜론','딸기','사과'],
                 captions=['달콤해요','시원해요','상큼해요','맛있어요'],
                 horizontal=True,
                 index=2)
if fruit == '딸기':
    st.write(f'당신이 선택한 과일은 🍓')
elif fruit == '바나나':
    st.write(f'당신이 선택한 과일은 🍌')
elif fruit == '사과':
    st.write(f'당신이 선택한 과일은 🍎')
elif fruit == '멜론':
    st.write(f'당신이 선택한 과일은 🍈')

st.subheader('Selectbox',divider=True)
fruit1 = st.selectbox(label='과일을 선택하세요.',
                      options=['바나나', '멜론', '딸기', '사과'],
                      index=None,
                      placeholder='과일을 선택하세요!')
if fruit1 == '딸기':
    st.write(f'당신이 선택한 과일은 🍓')
elif fruit1 == '바나나':
    st.write(f'당신이 선택한 과일은 🍌')
elif fruit1 == '사과':
    st.write(f'당신이 선택한 과일은 🍎')
elif fruit1 == '멜론':
    st.write(f'당신이 선택한 과일은 🍈')

st.divider()

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"])
with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled)

st.subheader('Multiselect', divider=True)
colors = st.multiselect('당신이 좋아하는 색상은?',
               ['red','green','blue','yellow','pink'])
st.write('선택한 색상은', colors)

st.subheader('Select slider', divider=True)
color_st, color_end = st.select_slider('당신이 좋아하는 색상은?',
               ['red','green','blue','yellow','pink'],
            value=('blue','yellow'))
st.write('당신이 좋아하는 색상은', color_st,',',color_end)

st.subheader('color picker', divider=True)
color = st.color_picker('Pick A Color', '#00f900')
st.write('선택한 색상은', color)

st.header('3. Number input elements')
st.subheader('Number input', divider=True)
num = st.number_input('숫자입력', value=None,
                      min_value=0,
                      max_value=100,
                      step=1,
                      format='%d',
                      placeholder='숫자를 입력하세요!')
st.write(f'현재 숫자:{num}')

st.subheader('Slider', divider=True)
score = st.slider('점수', min_value=0.0, max_value=100.0, value=20.0,step=0.1)
st.write(f'현재 점수: {score}점')

st.header('4. Text input elements')
st.subheader('Text input', divider=True)
id = st.text_input('아이디', value='id')
pw = st.text_input('비밀번호',type='password')
st.write(f'아이디: {id}, 비밀번호: {pw}')

st.subheader('Text area', divider=True)
text = st.text_area('질문을 입력하시오.')
st.write(text)

st.header('5. Date & Time input elements')
st.subheader('Date input', divider=True)

from datetime import datetime, date, time, timedelta
date = st.date_input('일자 선택', value=date(2024,3,1),
                     min_value=date(2023,1,1)
                     ,max_value=date(2024,12,31),
                     format='YYYY.MM.DD')
st.write(date)

st.subheader('Time input', divider=True)
time = st.time_input('시간입력',value=time(8,45),
                     step=timedelta(minutes=1))
st.write(time)

import time
with st.spinner('Wait for it...'):
    time.sleep(3)
st.success('Success!')
