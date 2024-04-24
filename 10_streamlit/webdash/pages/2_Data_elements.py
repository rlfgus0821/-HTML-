import streamlit as st
import pandas as pd
import numpy as np

st.title('Data Elements')
st.header('1. DataElements', divider=True)
# DataFrame도 wirte 가능
df = pd.DataFrame({'col1':[1,2,3,4],
                   'col2':[10,20,30,40]})
st.write(df)
st.divider()
st.markdown('use_container_width = True -> 페이지 크기에 알맞게 변경')
st.dataframe(df, use_container_width=True)

df1 = pd.DataFrame(np.random.randn(5,10),
                   columns=['col_%d'% (i+1) for i in range(10)])

st.dataframe(df1, width=400, height=150)
st.divider()
st.markdown('hide_index -> index 안보여주기')
st.dataframe(df1, width=400, height=150, hide_index=True)
st.divider()
st.markdown('column_order -> column 이름 지정')
st.dataframe(df,column_order=('col2','col1'))
st.divider()
st.markdown('최댓값, 최솟값 강조 표시')
st.dataframe(df1.style.highlight_max(axis=0))
st.dataframe(df1.style.highlight_min(axis=1))
st.divider()

st.markdown('write와 dataframe은 편집 불가능')
st.markdown('True / False -> checkbox형태로 표시')
df2 = pd.DataFrame([{'command':'st.write','rating':4,'is_widget':False},
                   {'command':'st.dataframe','rating':5,'is_widget':True},
                   {'command':'st.time_input','rating':3,'is_widget':True},
                   {'command':'st.metric','rating':4,'is_widget':True}])

df3 = pd.read_excel('data\kor_news_240326.xlsx').iloc[:30]
df3_part1 = df3.iloc[:10]
df3_part2 = df3.iloc[20:30]

st.write(df2)
st.dataframe(df2, use_container_width=True)


st.header('2. data editor')
st.markdown('data_editer -> dataframe을 편집할 수 있다')
edited_df = st.data_editor(df2)

st.markdown('idxmax() -> 최댓값')
edited_df.loc[edited_df['rating'].idxmax()]
fav_com = edited_df.loc[edited_df['rating'].idxmax()]['command']
st.markdown(f'가장 높은 점수의 위젯은? :blue[{fav_com}] :+1:')
st.divider()

st.markdown('excel 파일을 읽어 dataframe 생성')
st.dataframe(df3, hide_index=True)

edited_df3 = st.data_editor(df3, hide_index=True)

st.markdown('num_rows=dynamic')
st.data_editor(df3_part1, num_rows='dynamic')

st.header('3. table: st.table()')
st.markdown('table() -> 데이터 프레임 뿐만 아니라 리스트, 딕셔너리 등 표시 / 모든 내용을 다 보여준다.')
st.table(df3.iloc[:3])

st.subheader('add_rows()')
st.markdown('add_rows() -> concat처럼 행을 추가')
out_df = st.dataframe(df3_part1)
out_df.add_rows(df3_part2)

st.markdown('disabled=[col,...] -> 편집 불가능하게 만들기')
st.data_editor(df2, disabled=['command','is_widget'])
