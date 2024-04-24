import streamlit as st

st.title('Input widgets')
st.header('1. Button elements')

st.divider()

st.subheader('Button')
st.button('초기화', type='primary')
if st.button('안녕'):
    st.write('반가워 :smile:')
else:
    st.write('잘가! :raising_hand:')

st.divider()

st.subheader('Link button')

st.divider()

st.subheader('Submit button')
