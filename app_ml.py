import streamlit as st 
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sb


def run_ml_app() :
    st.subheader('거래량과 가격으로 예측')
    
    df = pd.read_csv('csv/BTC-USD.csv')
    
    # X,y 나누기 
    X = df.loc[ : , 'Volume'].to_frame()
    y = df.loc[ : ,'Close'].to_frame()
    # 시험, 훈련 나누기
    from sklearn.model_selection import train_test_split
    X_train , X_test , y_train , y_test = train_test_split(X , y,test_size = 0.2 ,random_state=1 )
    # 학습 하기
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train,y_train)
    # 시험 하기 
    y_pred = regressor.predict(X_test)
    error = y_test - y_pred
    EMS=(error ** 2).mean()
    st.text('EMS값은 1.099070e+08 입니다.')
    # 그래프로 나타내기
    fig1 = plt.figure()
    plt.plot(y_test.values) #numpy값으로 바꾼 후 입력해야한다.
    plt.plot(y_pred)
    plt.legend( ['Real' , 'Pred'] ) #그래프 우측 상단 이름 표시
    st.pyplot(fig1)
    
    st.text('따라서 거래량을 이용한 가격 예측은 불가능 합니다.')