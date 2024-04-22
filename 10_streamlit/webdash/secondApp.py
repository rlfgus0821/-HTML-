import streamlit as st
import pandas as pd

st.title('Data Elements')
st.header('1. DataElements', divider=True)
# DataFrame도 wirte 가능
df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[10,20,30,40]})
st.write(df)
st.divider()
# use_container_width = True -> 페이지 크기에 알맞게 변경
st.dataframe(df, use_container_width=True)