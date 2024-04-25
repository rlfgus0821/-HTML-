import streamlit as st
import time

with st.spinner('Wait for it...'):
    time.sleep(3)
st.balloons()
st.success('Success!')
st.snow()