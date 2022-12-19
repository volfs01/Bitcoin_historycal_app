import streamlit as st 
import webbrowser
def run_home_app() :
    
    st.title('비트코인 역사관에 오신걸 환영합니다.')
    st.subheader('비트코인 가격 검색 앱입니다.')
    st.text(' 상한가 , 하한가 , 시작가 , 종가 , 날짜 등으로 조회가 가능합니다.')
    st.text('비트코인의 데이터는 2021-12-14부터 2022-12-14까지 1년치 데이터입니다.')
    
    
    if st.button('개요') :
        st.subheader('비트코인의 가격,차트 검색과 가격예측 여부')
        st.text('데이터 분석  \n1. 원하는 날짜를 조회하면 날짜에 해당하는 정보를 볼 수 있다.\n2. 컬럼간의 상관 계수를 heatmap으로 나타냈다. \n3. 최대,최소,평균,개수,표준편차를 나타냈다.\n4. 가격과 거래량을 차트별로 나타냈다.\n\n가격 예측 \n1. Linear Regression로 시도하였으며 가능하지 않다는걸 밝혀냈다. \n2. 그래프로 시각화 함으로써 쉽게 나타냈다.')
    st.subheader('코인 뉴스를 볼 수 있는 사이트입니다.')
    if st.button('뉴스페이지 이동')  : 
        webbrowser.open( 'https://www.coindeskkorea.com/' )