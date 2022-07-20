import streamlit as st

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

#버튼을 만들어서 클릭해보자!!
if st.button('버튼'):
    st.write('버튼 클릭 성공')
else:
    st.write('안녕하세요!!!')

#다운로드 버튼을 클릭하면 txt파일을 다운로드 합니다.
text_contents = '''다운로드 받은 파일입니다.'''
st.download_button('다운로드', text_contents)

#[깃허브] pycharm에서 github 연동하기


