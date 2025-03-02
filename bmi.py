import streamlit as st
import pandas as pd
st.title('BMI calculator')
height = st.slider('Enter your height in cm', min_value=100, max_value=250, value=170)
weight = st.slider('Enter your weight in kg', min_value=40, max_value=200, value=70)
bmi = weight / ((height/100))**2
st.write(f'your BMI is {bmi:.2f}')
st.write('###  BMI categories ###')
st.write('-underweight: BMI less than 18.5')
st.write('-normal: BMI between 18.5 and 24.9')
st.write('-overweight: BMI between 25 and 29.9')
st.write('-obesity: BMI 30 or greater')

