# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 16:46:25 2023

@author: ASUS
"""

import streamlit as st
import joblib
import pandas as pd

def main():
    html_temp = """
    <div style="background-color:Lightblue;padding:20px">
    <h2 style="color:black";text-align:center> Health Insurance Cost Prediction using Machine Learning</h2>
    </div>
    
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    model = joblib.load('GradientBoostingRegressor_Model')
    
    p1 = st.slider('Enter yout Age',18,80)
    
    s1 = st.selectbox('Sex',('Male','Female'))
    
    if s1=='Male':
        p2=1
    else:
        p2=0
    
    p3 = st.number_input('Enter your BMI Value')
    
    p4 = st.slider('Enter number of your Children',0,4)
    
    s2 = st.selectbox('Smoker',('Yes','No'))
    
    if s2=='Yes':
        p5=1
    else:
        p5=0
        
    p6 = st.slider('Enter your region',1,4)
    st.text('1=southwest\n2=southeast\n3=northwest\n4=northeast')
    
    if st.button('Predict'):
      prediction = model.predict([[p1,p2,p3,p4,p5,p6]])
      st.balloons()
      st.success('Insurance Amount is {} '.format(round(prediction[0],2)))
    
if __name__ == '__main__':
    main()
    
    
    
