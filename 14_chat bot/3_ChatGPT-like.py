import streamlit as st
from openai import OpenAI

st.title('ChatGPT-like clone')

client = OpenAI(api_key= st.secrets['OPENAI_API_KEY'])

if 'openai_model' not in st.session_state:
    st.session_state['openai_model'] = 'gpt-3.5-turbo'

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
        results = client.chat.completions.create(model= st.session_state['openai_model'],
                                                 messages= [{'role': msg['role'], 'content': msg['content'} for msg in st.session_state.messages],
                                                 stream= True)
        response = st.write_stream(results)

    st.session_state.messages.append({'role': 'assistant', 'content': response})