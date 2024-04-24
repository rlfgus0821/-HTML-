import streamlit as st
import numpy as np
import time

st.header('Column layout')
col= st.columns(3)
col[0].subheader('영역1')
col[0].image("https://static.streamlit.io/examples/cat.jpg")
col[1].subheader('영역2')
col[1].image("https://static.streamlit.io/examples/dog.jpg")
col[2].subheader('영역3')
col[2].image("https://static.streamlit.io/examples/owl.jpg")

st.divider()

col1, col2 = st.columns([1,3],gap='medium')
data = np.random.randn(10,1)

with col1:
   st.metric('점수',55,0.5)

with col2:
   st.line_chart(data)

st.divider()

st.header('Container')
st.subheader('1. 컨테이너 내부와 외부', divider=True)
with st.container():
   st.write('컨테이너 내부')
   st.bar_chart(np.random.randn(30))
st.write('컨테이너 외부')

st.subheader('2. 컨테이너에 요소 추가', divider=True)
container = st.container(border=True)
container.write('컨테이너 안에 있어요')
container.area_chart(data)
st.write('컨테이너 외부에 있어요')
container.button('시작')

st.subheader('3. 그리드 모양의 컨테이너 구성',divider=True)
row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
   tile = col.container(height=120)
   tile.subheader(':smile:')

st.subheader('4. long container: scollbar',divider=True)
with st.container(height=300):
   st.markdown('long_text '*300)

st.subheader('Empty container: single element',divider=True)
with st.empty():
   for seconds in range(10):
      st.write(f'{seconds}초')
      time.sleep(1)
   st.write('time over!')
