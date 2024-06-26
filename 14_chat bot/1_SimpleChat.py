import streamlit as st
import random
import time

st.title('Simple Chat')

def response_generator():
    response = random.choice([
        '안녕하세요. 무엇을 도와드릴까요?',
        '도움이 필요하신가요?',
        '당신의 질문에 최선을 다해 답변드릴게요'
    ])
    for word in response.split():
        yield word + ' '
        time.sleep(0.05)

# chat 히스토리를 초기화
if 'messages' not in st.session_state:
    st.session_state.messages = []

# chat 히스토리로 부터 들어있는 메시지를 출력
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# st.session_state.messages -> 대화했던 내용들 저장한 히스토리
if prompt := st.chat_input('메시지를 입력하세요'):
    st.session_state.messages.append({'role':'user', 'content':prompt})
    with st.chat_message('user'):
        st.markdown(prompt)

    with st.chat_message('assistant'):
        response = st.write(response_generator())
        st.session_state.messages.append({'role': 'assistant', 'content': response})