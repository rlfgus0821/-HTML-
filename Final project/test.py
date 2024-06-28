import streamlit as st
from openai import OpenAI

st.title('음식추천-ChatGPT')

client = OpenAI(api_key= st.secrets['OPENAI_API_KEY'])

if 'openai_model' not in st.session_state:
    st.session_state['openai_model'] = 'gpt-3.5-turbo'

# chat 히스토리를 초기화
if 'messages' not in st.session_state:
    st.session_state.messages = []

# chat 히스토리로부터 들어있는 메시지를 출력
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# 비오는 날 추천 음식 리스트
rainy_day_foods = [
    {"name": "부대찌개", "link": "http://example.com/budaejjigae"},
    {"name": "파전", "link": "http://example.com/pajeon"},
    {"name": "수제비", "link": "http://example.com/sujebi"},
]

# 매운 음식 리스트
spicy_foods = [
    {"name": "떡볶이", "link": "http://example.com/budaejjigae"},
    {"name": "마라탕", "link": "http://example.com/pajeon"},
    {"name": "매운갈비", "link": "http://example.com/sujebi"},
]

# st.session_state.messages -> 대화했던 내용들 저장한 히스토리
if prompt := st.chat_input('메시지를 입력하세요'):
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    with st.chat_message('user'):
        st.markdown(prompt)

    if any(keyword in prompt for keyword in ["비오는", "비 올", "비 내리",'비올','비내리']):
        # 비오는 날 음식 추천
        response_content = "비오는 날 추천 음식:\n"
        for food in rainy_day_foods:
            response_content += f"- [{food['name']}]({food['link']})\n"

        with st.chat_message('assistant'):
            st.markdown(response_content)
    elif "매운" in prompt:
        # 매운 음식 추천
        response_content = "매운 음식 추천:\n"
        for food in spicy_foods:
            response_content += f"- [{food['name']}]({food['link']})\n"

        with st.chat_message('assistant'):
            st.markdown(response_content)
    else:
        # 일반적인 GPT 대화
        with st.chat_message('assistant'):
            results = client.chat.completions.create(model=st.session_state['openai_model'],
                messages=[{'role': msg['role'], 'content': msg['content']} for msg in st.session_state.messages],
                stream=True)

            response = st.write_stream(results)

        st.session_state.messages.append({'role': 'assistant', 'content': response})
