# 스트림릿 메인페이지

import streamlit as st
import numpy as np

st.header('다양한 챗봇 기능 연습')

prompt = st.chat_input('메시지를 입력하세요')
st.markdown(prompt)

with st.chat_message('user'):
    st.write('Hello!')
    st.line_chart(np.random.randn(30,3))

message = st.chat_message('assistant')
message.write('Hi!!')

message = st.chat_message('ai')
message.write('Hello CHAT')


st.write('1. Simple chat')
st.write('2. Echo bot')
st.write('3. chatGPT-like')