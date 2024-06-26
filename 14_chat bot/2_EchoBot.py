import streamlit as st

st.title('Echo bot')

if 'messages' not in st.session_state:
    st.session_state.messages = []

# chat 히스토리로 부터 들어있는 메시지를 출력
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# st.session_state.messages -> 대화했던 내용들 저장한 히스토리
if prompt := st.chat_input('메시지를 입력하세요'):
    st.chat_message('user').markdown(prompt)
    st.session_state.messages.append({'role':'user','content':prompt})

    response = f'Echo: {prompt}'
    with st.chat_message('assistant'):
        st.markdown(response)
        st.session_state.messages.append({'role':'assistant','content':response})
