import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sb
import streamlit as st
import plotly.graph_objects as go

def run_eda_app() :
    st.title('정보 분석 페이지 입니다.')
    df = pd.read_csv('csv/BTC-USD.csv')
    
    choice = st.number_input('정보 개수를 정해주세요' ,1,20)
    st.text('모든 데이터를 최대 20개 까지 가져올 수 있습니다. \n숫자를 수정하고 버튼을 누를 시 나타납니다.')
    if st.button('최근 데이터 보기') :
        st.dataframe(df.tail(choice))
    
    choice2 = st.radio('원하시는 값을 선택해주세요 모든 컬럼을 보여드립니다.', ['최대값' , '최소값 ','표준편차','평균','개수'])
    if choice2 == '최대값' :
        st.dataframe(df.describe().iloc[7,])
    elif choice2 == '최소값 ' :
        st.dataframe(df.describe().iloc[3,])
    elif choice2 == '표준편차' :
        st.dataframe(df.describe().iloc[2,])
    elif choice2 == '평균' :
        st.dataframe(df.describe().iloc[1,])
    elif choice2 == '개수' :
        st.dataframe(df.describe().iloc[0,])
        
    st.subheader('컬럼의 상관 계수를 보여드립니다.')
    
    fig1 = plt.figure()
    sb.heatmap(data=df.corr() , annot=True , fmt='.2f' , cmap='coolwarm' , vmin= -1 , vmax=1 , linewidths=0.5 )
    st.pyplot(fig1)
    st.text('피어슨의 상관계수로 해석하면 \n거래량과 가격은 약한 음적 선형 관계라는것을 알 수 있다.')
    st.image('https://patentimages.storage.googleapis.com/67/b9/0e/4261356f8eaf28/112016094691347-pat00013.png')
    
    st.subheader('원하시는 날짜를 기준으로 증감률을 보여드립니다.')
    
    # 깨달은 점 이미 st.dataframe을 해버리고 거기다가 연산을 하는건 안된다. 
    # 괄호안에 한번에 연산해야한다. 
    # 주의 깊게 보자!
    my_date = st.date_input('날짜를 입력하시오')
    
    Ratio = ((df['Close'][365]- df.loc[df['Date'] == str(my_date) , :]['Close']) / df.loc[df['Date'] == str(my_date) , :]['Close']* 100)  
    
    st.success('{}부터 2022-12-14까지 증감률은 {}%입니다.' .format(my_date ,Ratio.values ))
    
    st.subheader('가격과 거래량을 차트로 보여드릴게요')
    chart = ['캔들차트' , '선차트' , '바차트']
    choice3 = st.selectbox('차트 종류를 선택하세요',chart)
    
    st.text('가격차트')
    
    if choice3 == '캔들차트' :
        
        fig2 = plt.figure()
        fig100 = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'], high=df['High'],
                low=df['Low'], close=df['Close'])
                      ])

        fig100.update_layout(xaxis_rangeslider_visible=False)
        st.plotly_chart(fig100)
        st.pyplot(fig2)
    elif choice3 == '선차트' :
        
        fig3 = plt.figure()
        fig99 = go.Figure([go.Scatter(x=df['Date'], y=df['High'])])
        st.plotly_chart(fig99)
        st.pyplot(fig3)
        
    elif choice3 == '바차트' :
        fig4 = plt.figure()
        fig98 = px.bar(df, x=df.index, y="Open")
        st.plotly_chart(fig98)
        st.pyplot(fig4)  
        
    chart2 = [ '선차트' , '바차트']
    choice4 = st.selectbox('차트 종류를 선택하세요',chart2)
    st.text('거래량 차트')
    
    if choice4 == '선차트' :
        fig5 = plt.figure()
        fig97 = go.Figure([go.Scatter(x=df['Date'], y=df['Volume'])])
        st.plotly_chart(fig97)
        st.pyplot(fig5)
        
    if choice4 == '바차트' :
        fig6 = plt.figure()
        fig96 = px.bar(df, x=df.index, y="Volume")
        st.pyplot(fig6)