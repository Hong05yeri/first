import streamlit as st
import sqlite3
import pandas as pd
import os.path

con = sqlite3.connect('db.db')
cur = con.cursor()

def login_user(id, pw):
    cur.execute(f"SELECT *"
                f" FROM users "
                f"WHERE id='{id}' and pwd='{pw}'")
    return cur.fetchone()

menu = st.sidebar.selectbox('MENU', options=['로그인','회원가입','회원목록'])
functions = st.sidebar.selectbox('FUNCTIONS', options=['번역기', '환율 계산기', '만족도조사'])
if menu == '로그인':
    st.subheader('로그인')


    login_id = st.text_input('아이디',  placeholder='아이디를 입력하세요')
    login_pw = st.text_input('비밀번호', placeholder='비밀번호를 입력하세요',type='password')

    login_btn = st.button('로그인')
    st.sidebar.subheader('로그인')

    if login_btn:
        user_info = login_user(login_id, login_pw)
        file_name = './ing/'+user_info[0]+'.png.jpg'

        if os.path.exists(file_name):
            st.sidebar.image(file_name)
            st.sidebar.write(user_info[4],'님 환영합니다.')
        else:
            st.write(user_info[4], '님 환영합니다.')

if menu == '회원가입':
    st.subheader('회원가입')
    st.info('다음 양식을 모두 입력후 회원가입 버튼을 클릭하세요.')
    uid = st.text_input('아이디', max_chars=10)
    uname = st.text_input('이름', max_chars=10)
    upw = st.text_input('비밀번호', type='password')
    upw_chk = st.text_input('비밀번호 확인', type='password')
    uage = st.text_input('나이')
    ugender = st.radio('성별', options=['여','남'], horizontal=True)

    ubtn = st.button('회원가입')

    if ubtn:
        if upw != upw_chk:
            st.error('비밀번호가 일치하지 않습니다.')
            st.warning('비밀번호가 일치하지 않습니다.')
            st.stop()


        cur.execute(f"INSERT INTO users(id, pwd, gender, age, name) "
                    f"VALUES('{uid}','{upw}','{ugender}',{uage},'{uname}')")
        st.success('회원가입에 성공했습니다.')
        con.commit()


    st.sidebar.subheader('회원가입')
if menu == '회원목록':
    st.subheader('회원목록')
    df = pd.read_sql('SELECT * FROM users', con)
    st.dataframe(df)
    st.sidebar.subheader('회원목록')

if functions == '만족도조사':
    st.subheader('만족도조사')
    st.info('저희 앱을 이용해주셔서 감사합니다. 여러분의 좋은 의견을 참고하기 위한 간단한 설문 조사입니다. 다음 양식을 모두 입력후 제출 버튼을 클릭하세요.')
    st.sidebar.subheader('만족도조사')

    st.subheader('1. 전반적인 앱 만족도')
    question1 = st.radio("전반적인 앱 기능에 대한 만족도는 어떤가요?", ('좋음', '보통', '나쁨'))
    if question1 == '좋음':
        st.write('You selected 좋음.')
    elif question1 == '보통':
        st.write('You selected 보통.')
    elif question1 == '나쁨':
        st.write('You selected 나쁨')

    st.subheader('2. 번역기 기능')
    question2 = st.radio("번역기 기능에 대한 만족도는 어떤가요?", ('좋음', '보통', '나쁨'))

    if question2 == '좋음':
        st.write('You selected 좋음.')
    elif question2 == '보통':
        st.write('You selected 보통.')
    elif question2 == '나쁨':
        st.write('You selected 나쁨')

    st.subheader('3. 환율 계산기 기능')
    question3 = st.radio("환율 계산기 기능에 대한 만족도는 어떤가요?", ('좋음', '보통', '나쁨'))

    if question3 == '좋음':
        st.write('You selected 좋음.')
    elif question3 == '보통':
        st.write('You selected 보통.')
    elif question3 == '나쁨':
        st.write('You selected 나쁨')

    st.subheader('4. 가장 만족스러운 서비스')
    question4 = st.radio("번역기, 환율 계산기 기증 중 가장 도움이 되는 서비스는 뭔가요?", ('번역기', '환율 계산기'))

    if question4 == '번역기':
        st.write('You selected 번역기.')
    elif question4 == '환율 계산기':
        st.write('You selected 환율 계산기.')

    st.info('아래 항목은 필수항목은 아닙니다.')
    st.subheader('5. 피드백')
    question5 = st.text_input('그 외 앱에 대한 평가, 원하는 추가적인 서비스', max_chars=100)

    if st.button('제출'):
        st.write('소중한 의견 감사합니다.')
        cur.execute(f"INSERT INTO Survey(Q1, Q2, Q3, Q4, Q5) "
                    f"VALUES('{question1}','{question2}','{question3}','{question4}','{question5}')")
        con.commit()
    else:
        st.write('저희 앱을 사용해주셔서 언제나 감사합니다.')




