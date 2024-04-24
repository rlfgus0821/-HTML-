import streamlit as st

st.header('Popover container')

with st.popover('Open popover'):
    st.write('Hello')
    name = st.text_input("What's your name?")

st.write('Your name', name)

popover = st.popover('좋아하는 색상은?',use_container_width=True)
red = popover.checkbox('red')
blue = popover.checkbox('blue')

if red:
    st.write(':red[red]')
if blue:
    st.write(':blue[blue]')

with st.popover('popover 사용 시 주의점'):
    st.write('popover를 또 다른 popover 안에 배치 불가')
