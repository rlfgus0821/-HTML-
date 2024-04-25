import streamlit as st
from streamlit.connections import SQLConnection

# my SQL 연결(접속)
conn= st.connection('shopdb', type='sql',
              url='mysql://streamlit:1234@localhost:3306/shopdb')

# 질의 수행 (ttl -> 시간(초 단위)
df = conn.query('select * from customer;', ttl=600)

st.dataframe(df)

# for row in df.itertuples():
#     st.write(f'{row.customer_name}의 번호는 {row.phone}.')
#
# sql = '''insert into customer (customer_id, customer_name,phone, customer_birthday)
# values (:id,:name,:phone,:birth);'''
#
# with conn.session as s:
#     s.execute({'id':6,'name':"홍길동", 'phone':"010-1111-1111",'birth':"2000-01-30"})
#     s.commit()

