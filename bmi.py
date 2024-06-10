import streamlit
import streamlit as str

str.title('BMI Calculator App') # es ku run karne se phale terminal par jaa ke ( streamlit run file name ) run kar le

weight = streamlit.number_input("Enter Your Weight ")
height = str.number_input("Enter Your Height ")
click = str.button(" Click Here")
if click == True:
     b = weight/height**2*1000
     str.title(b)