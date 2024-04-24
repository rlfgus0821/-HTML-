import streamlit as st

# Headeings and Body text (markdown / title / header / subheader)

st.title('Streamlit 맛보기')
# divider -> 밑줄
st.header('1. 텍스트 요소', divider='rainbow')
st.subheader('1) 제목을 작성하기 위한 API', divider=False)

# : ~~~ : -> emoji
st.write('Emojis Link: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/')
st.write('Hello streamlit :cool: :sunglasses:')
# 공백 2개 -> enter

st.write('''st.title()  
st.header()  
st.subheader()  
''')

# _~~_ -> rotation / :color[~~] -> 색 지정
st.subheader('2) _Text_ 본문을 구성하는 :red[API]', divider=False)
st.write('''
- st.caption()  
- st.text()  
- st.code()  
- st.markdown()  
''')

# write / text / caption -> 폰트와 크기, 색 등이 다르다
st.text('This is some text')
st.caption('This is caption')
st.write(':blue[makrdown]')
st.markdown('''한 줄 끝에 공백(space) 두 칸을 입력하면  
줄바꿈(soft return).

한 행에 두 개 이상의 newline은 hard return. ''')

sample_code = '''
def fun():
    print('Hello!!')
'''

# 코드 표시
st.write(':blue[st.code]')
st.code(sample_code, language='python')

# 수식 표현 -> latex
st.write('[st.latex]')
st.latex('b \over a')
st.latex('\sqrt{x^2 + y^2}')
# divider() -> 밑줄
st.divider()
st.write('---')
# echo() -> 코드로 만들어 보여주기
with st.echo():
    st.write('This code will be printed')

greeting = 'Hi, Hello'
bye = 'Good Bye'
# 변수로 사용가능
st.write(greeting, bye)