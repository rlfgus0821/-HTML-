import streamlit as st
import numpy as np
import pandas as pd

st.header('Expander')
st.bar_chart({'data':[10,30,15,25,20]})

with st.expander('참고 설명', expanded=True):
    st.write('''위 차트는 점심식사 선호도를 조사한 결과로서,
    나타낸 차트입니다''')
    st.image("https://static.streamlit.io/examples/dice.jpg")
    
expander = st.expander('expander 사용 시 주의점')
expander.write('expander 내에 다른 expander를 사용할 수 없다.')

