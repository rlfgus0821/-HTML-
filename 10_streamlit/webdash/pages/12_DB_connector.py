import streamlit as st
import pandas as pd
import mysql.connector as mc
import datetime

conn = mc.connect(
    host='localhost',
    database='shopdb',
    user='streamlit',
    password='1234')
if conn.is_connected():
    db_info= conn.get_server_info()
    st.write('server_version:',db_info)

cur = conn.cursor(buffered=True)
cur.execute('select * from customer;')

# record = cur.fetchone()
# st.write('connected to DB:', record)

# st.write(records)
def make_df():
    cur.execute('select * from customer;')
    records = cur.fetchall()
    st.write(pd.DataFrame(records, columns=['id','name','phone','birth']))

make_df()

with st.form(key='input form'):
    id = st.number_input('고객 번호',min_value=1)
    name = st.text_input('고객 이름')
    phone = st.text_input('전화번호')
    birth = st.date_input('생년월일', format='YYYY-MM-DD',value=None)
    submitted = st.form_submit_button('입력')

if submitted:
    sql = 'insert into customer (customer_id, customer_name, phone, birthday) values (' \
        + str(id) + ', \"' + name + '\" , \"' + phone + '\" , \"' + str(birth) + '\");'
    cur.execute(sql)
    conn.commit()
    make_df()
