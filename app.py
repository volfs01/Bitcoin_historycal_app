import streamlit as st 

from app_home import run_home_app
from app_eda import run_eda_app
from app_ml import run_ml_app
from app_chart import run_chart_app
def main() :
    menu = ['Home' , 'EDA','ml','chart']
    choice = st.sidebar.selectbox('메뉴' , menu)

    if choice == 'Home' :
        run_home_app()
    elif choice == 'EDA' :
        run_eda_app()
    elif choice == 'ml' :
        run_ml_app()
    elif choice == 'chart' :
        run_chart_app()
    
    

if __name__ == '__main__' :
    main()