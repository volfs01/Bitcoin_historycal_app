import streamlit as st 
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sb


def run_ml_app() :
    st.subheader('거래량과 가격으로 예측')
    
    df = pd.read_csv('csv/BTC-USD.csv')
    
    st.subheader('제작 과정')
    st.text('피처스케일링을 자동으로 해주는 Linear Regression로 제작하였으며 \n거래량을 기반으로 가격(종가)를 예측했다.\n\n평가 기준은 EMS로 정했다. \n\ntain값과 test값을 나누어 모델링 후 학습을 했으며, \n학습 후 얻어낸 예측값과 실제값을 그래프로 나타냈다.')
    st.subheader('결과')
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
    
    st.text('주식 시장은 완벽한 시장이 아니며, 정보가 완전하지 않기 때문에\n주식 시장의 가격을 정확하게 예측할 수 없음을 인정해야 합니다.\n따라서 거래량을 이용한 가격 예측은 불가능 합니다.')