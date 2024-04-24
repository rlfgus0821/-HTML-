import numpy as np
import pandas as pd
import time
import streamlit as st
from datetime import datetime, date, time

st.header('Data Column Config')
st.subheader('1. Column')
df = pd.DataFrame([{'command':'st.write','rating':4,'is_widget':False},
                   {'command':'st.dataframe','rating':5,'is_widget':True},
                   {'command':'st.time_input','rating':3,'is_widget':True},
                   {'command':'st.metric','rating':4,'is_widget':True}])
st.dataframe(df)

st.divider()

st.markdown('column_config(label= 열 이름, help=열에 대한 도움말, width=너비)')
st.dataframe(df, column_config={
    'command':st.column_config.Column(
                 label='Streamlit commands',
                 help='Streamlit **widget**',
                 width='small')})
st.data_editor(df, column_config={
    'command':st.column_config.Column(
                 label='Streamlit commands',
                 help='Streamlit **widget**',
                 width='medium',
                    disabled=True)})
st.divider()

st.subheader('2. Text Column')
st.markdown('text_column(default= 행을 추가 할 때 defalut로 나오는 글자)')
st.data_editor(df,column_config={'command': st.column_config.TextColumn(
    label='Streamlit commands',
    help='Streamlit **widget** commands',
    default='st.')},num_rows='dynamic')

st.markdown('text_column(max_chars= 최대 글자수)/num_rows=행을 추가할 수 있도록 설정')
st.data_editor(df,column_config={'command': st.column_config.TextColumn(
    label='Streamlit commands',
    help='Streamlit **widget** commands',
    default='st.',max_chars=20)},num_rows='dynamic')

st.markdown('text_column(validate= 정규표현식으로 설정)')
st.data_editor(df,column_config={'command': st.column_config.TextColumn(
    label='Streamlit commands',
    help='Streamlit **widget** commands',
    default='st.',max_chars=20,validate='^st\.[a-z_]+$'
)},num_rows='dynamic')

st.divider()

st.subheader('3. Number Column')
st.markdown('min_value / max_value -> 최솟값/최댓값 설정')
st.markdown('step= 최소 증가 or 감소 값 / step=1 -> 1씩 증가 or 감소 0.5증가x')
st.data_editor(df,column_config={
    'rating':st.column_config.NumberColumn(
        label='좋아요',
        help='한달동안의 좋아요 수',
        min_value=0,
        max_value=10,
        step=1,
        format='%d'
    )})

st.divider()

st.subheader('4. Checkbox Column')
st.data_editor(df,
               column_config={
                   'is_widget':st.column_config.CheckboxColumn(
                   label='위젯인가?',
                   default= False,
                   ),
                   'command': st.column_config.TextColumn(
                       label='Streamlit commands',
                       help='Streamlit **widget** commands',
                       default='st.', max_chars=20, validate='^st\.[a-z_]+$')
               },num_rows='dynamic')

st.divider()

st.subheader('5. Selectbox Column')
df2 = pd.DataFrame(
    {
        "category": [
            "📊 Data Exploration",
            "📈 Data Visualization",
            "🤖 LLM",
            "📊 Data Exploration",],})

st.data_editor(df2)
st.markdown('선택할 수 있는 옵션 목록')
st.markdown('required -> 필수로 값이 있어야 하는지 여부')
st.data_editor(df2,column_config={'category': st.column_config.SelectboxColumn(
    label='App Category',
    help='The category of the app',
    width='medium',
    options=["📊 Data Exploration",
            "📈 Data Visualization",
            "🤖 LLM",
            "📊 Data Exploration"],required=True)},hide_index=True)

st.divider()

st.subheader('6. Datetime Column')
df3 = pd.DataFrame({'meeting_date':
                        [datetime(2024,2,5,12,30),
                         datetime(2024,2,7,2,20),
                         datetime(2024,3,12,1,40),
                         datetime(2024,3,19,11,30),
                         datetime(2024,4,1,10,10)]})
st.data_editor(df3)
st.markdown('format -> 표현 형식 지정')
st.data_editor(df3,column_config={
    'meeting_date':st.column_config.DatetimeColumn(
        min_value=datetime(2024,1,1),
        max_value=datetime(2024,4,10),
        format='D MMM YYYY, h:mm a'
    )})

st.divider()

st.subheader('7. Date Column')
df4 = pd.DataFrame({
    'meeting_date':
        [date(2024,2,5),
     date(2024,2,7),
     date(2024,3,12),
     date(2024,3,19),
     date(2024,4,1)]})
st.dataframe(df4)
st.data_editor(df4,column_config={
    'meeting_date':st.column_config.DateColumn(
        min_value=date(2023,1,1),
        max_value=date(2025,12,31),
        format='DD.MM.YYYY')})

st.divider()

st.subheader('8. Time Column')
df5 = pd.DataFrame({
    'meeting_time':    [time(12,30),
     time(2,20),
     time(1,40),
     time(11,30),
     time(10,10)]})
st.data_editor(df5,column_config={
    'meeting_time': st.column_config.TimeColumn(
        min_value=time(9,0,0),
        max_value=time(18,0,0),
        format='hh:mm a')})

st.divider()

st.subheader('9. List Column')
df6 = pd.DataFrame({'score':[[0,4,60,80,100],
                             [80,30,80,50,70],
                             [90,30,60,80,100]]})
st.markdown('List -> dataframe()')
st.dataframe(df6)
st.markdown('List -> table()')
st.table(df6)
st.markdown('List -> data_editor / 편집불가')
st.data_editor(df6,
             column_config={
             'score':st.column_config.ListColumn(
                 width='medium'
             )})

df7 = pd.DataFrame({
    'site':['naver','daum','google'],
    'url':['https://naver.com',
           'https://daum.net',
           'https://google.com']
})
st.markdown('display_text -> 대신 보여지는 text')
st.data_editor(df7,column_config={
    'url': st.column_config.LinkColumn(
        help='Search portal site!',
        max_chars= 100,
        validate='^https:/www\.[a-z]+\.[a-z]+',
        display_text='Search site'
    )
})

st.divider()

st.subheader('11. Chart Column')
st.markdown('LineChartColumn -> 라인 그래프로 시각화')
st.markdown('AreaChartColumn -> 채워진 라인 그래프로 시각화')
st.markdown('BarChartColumn -> 바 그래프로 시각화')
df8 = pd.DataFrame({'name':['kim','lee','choi'],
                    'score1':[[0,4,60,80,100],
                             [80,30,80,50,70],
                             [90,30,60,80,100]],
                    'score2':[[0,4,60,80,100],
                             [80,30,80,50,70],
                             [90,30,60,80,100]],
                    'score3': [[0, 4, 60, 80, 100],
                               [80, 30, 80, 50, 70],
                               [90, 30, 60, 80, 100]]
                    })
st.dataframe(df8,column_config={
    'score2': st.column_config.LineChartColumn(
        y_min=0,y_max=100
    ),'score3': st.column_config.AreaChartColumn(
        y_min=0,y_max=100),
'score1': st.column_config.BarChartColumn(
        y_min=0,y_max=100)})

st.divider()

st.subheader('12. Image Column')
df9 = pd.DataFrame({'image':["https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/5435b8cb-6c6c-490b-9608-799b543655d3/Home_Page.png",
"https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/ef9a7627-13f2-47e5-8f65-3f69bb38a5c2/Home_Page.png",
"https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/31b99099-8eae-4ff8-aa89-042895ed3843/Home_Page.png",
"https://storage.googleapis.com/s4a-prod-share-preview/default/st_app_screenshot_image/6a399b09-241e-4ae7-a31f-7640dc1d181e/Home_Page.png"
      ]})
st.markdown('LinkColumn() -> 링크로 보여주기')
st.dataframe(df9, column_config={
    'image':st.column_config.LinkColumn()})

st.markdown('ImageColumn() -> 이미지로 보여주기')
st.dataframe(df9, column_config={
    'image':st.column_config.ImageColumn()})

st.divider()

st.subheader('13. Progress Column')
df10 = pd.DataFrame({'sales':[100,50,60,42]})

st.markdown('ProgressColumn -> percent bar로 표현')
st.data_editor(df10,column_config={
    'sales': st.column_config.ProgressColumn(
        min_value=0, max_value=150,
        format='%f원')})