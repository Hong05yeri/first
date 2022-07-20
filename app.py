import streamlit as st
import sqlite3

con = sqlite3.connect('db.db')
cur = con.cursor()

def login_user(id, pw):
    cur.execute(f"SELECT *"
                f" FROM users "
                f"WHERE id='{id}' and pwd='{pw}'")
    return cur.fetchone()

st.title('안녕하세요')
st.write('Hello streamlit')

st.title('This is a title')
st.header('This is a header')
st.subheader('This is a subheader')

st.text('Hello World. Streamlit text')
name = 'Hong gildong'
st. text('Hi, {}'.format(name))

st.markdown('## This is markdown')

st.markdown('## This is markdown')
st.markdown('Streamlit is **_really_ cool**.')

st.caption('This is a string that explains something above. ')

code='''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

#버튼만들기
if st.button('버튼'):
    st.write('버튼 클릭 성공')
else:
    st.write('안녕하세요!!!')

#다운로드 버튼을 클릭하면 txt파일을 다운로드
text_contents = '''다운로드 받은 파일입니다.'''
st.download_button('다운로드', text_contents)

#사이드바 제작
menu = st.sidebar.selectbox('MENU', options=['로그인','회원가입','회원목록'])

if menu == '로그인':
    st.subheader('로그인')


    login_id = st.text_input('아이디',  placeholder='아이디를 입력하세요')
    login_pw = st.text_input('비밀번호', placeholder='비밀번호를 입력하세요',type='password')

    login_btn = st.button('로그인')
    if login_btn:
        user_info = login_user(login_id, login_pw)
        st.write(user_info[4],'님 환영합니다.')
    st.sidebar.subheader('로그인')
if menu == '회원가입':
    st.subheader('회원가입')
    st.sidebar.subheader('회원가입')
if menu == '회원목록':
    st.subheader('회원목록')
    st.sidebar.subheader('회원목록')

#데이터 베이스 만들기

