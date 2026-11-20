import streamlit as st

st.write("hello World")

## User details application

st.title('User Registration')

name = st.text_input('Enter Your Name')
age  = st.number_input('Enter Your age',min_value=1, max_value=100)

gender = st.selectbox(
    "Select Gender",
    ["Male", "Female", "Other"]
)

if st.button("Register"):

    st.write("Registration Details")

    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Gender:", gender)

## This creates an interactive form without writing HTML or CSS.