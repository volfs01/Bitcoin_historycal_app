import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sb
import streamlit as st
import plotly.graph_objects as go

def run_chart_app() :
    df = pd.read_csv('csv/BTC-USD.csv')
    
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