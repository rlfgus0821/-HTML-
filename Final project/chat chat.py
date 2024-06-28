import streamlit as st
import openai
from openai import OpenAI

# 제목
st.title('음식추천-ChatGPT')

# OpenAI API 키 설정
client = OpenAI(api_key= st.secrets['OPENAI_API_KEY'])

# 세션 상태에 openai_model이 없으면 -> gpt-3.5-turbo 설정
if 'openai_model' not in st.session_state:
    st.session_state['openai_model'] = 'gpt-3.5-turbo'

# 세션 상태에 messages가 없으면 chat 히스토리를 빈 리스트로 초기화
if 'messages' not in st.session_state:
    st.session_state.messages = []

# chat 히스토리로부터 들어있는 메시지를 대화박스형태로 반복하여 화면에 출력
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

# 비오는 날 추천 음식 리스트
rainy_day_foods = [
    {"name": "부대찌개", "link": "http://example.com/budaejjigae"},
    {"name": "파전", "link": "http://example.com/pajeon"},
    {"name": "수제비", "link": "http://example.com/sujebi"},
]

# 매운 음식 추천 리스트
spicy_foods = [
    {"name": "떡볶이", "link": "http://example.com/tteokbokki"},
    {"name": "매운 갈비찜", "link": "http://example.com/spicy_galbijjim"},
    {"name": "불닭볶음면", "link": "http://example.com/buldak_bokkeummyun"},
]

# 조건과 함수 매핑
def recommend_rainy_day_foods():
    response_content = "비오는 날 추천 음식:\n"
    for food in rainy_day_foods:
        response_content += f"- [{food['name']}]({food['link']})\n"
    return response_content

def recommend_spicy_foods():
    response_content = "매운 음식 추천:\n"
    for food in spicy_foods:
        response_content += f"- [{food['name']}]({food['link']})\n"
    return response_content

# 조건과 함수 수행 조건
conditions = {
    "비오는 날": (lambda prompt: any(keyword in prompt for keyword in ["비오는", "비 올", "비 내리",'비올','비내리']), recommend_rainy_day_foods),
    "매운": (lambda prompt: "매운" in prompt, recommend_spicy_foods),
}

# st.session_state.messages -> 대화했던 내용들 저장한 히스토리
# 사용자가 입력한 메시지를 prompt 변수에 저장 -> messages 리스트에 추가하고 화면에 출력
if prompt := st.chat_input('메시지를 입력하세요'):
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    with st.chat_message('user'):
        st.markdown(prompt)

    # 조건 확인 및 해당하는 조건 -> 관련 함수를 호출
    response_content = None
    for keyword, (condition, recommend_func) in conditions.items():
        if condition(prompt): # 조건에 맞는 응답이 있으면 조건을 response_content에 저장
            response_content = recommend_func()
            break
    # 조건에 맞는 응답이 있으면 출력 및 세션에 추가
    if response_content:
        with st.chat_message('assistant'):
            st.markdown(response_content)
        st.session_state.messages.append({'role': 'assistant', 'content': response_content})
    else:
        # 조건에 맞는 응답이 없으면 GPT-3.5 대화 수행하여 응답 및 세션 상태에 추가
        with st.chat_message('assistant'):
            results = client.chat.completions.create(model=st.session_state['openai_model'],
                                                     messages=[{'role': msg['role'], 'content': msg['content']} for msg
                                                               in st.session_state.messages],
                                                     stream=True)
            response = st.write_stream(results)

        # st.session_state.messages 리스트에 새로운 답변 및 질문 메시지 추가
        st.session_state.messages.append({'role': 'assistant', 'content': response})
