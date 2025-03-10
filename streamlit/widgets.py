import pandas as pd
import streamlit as st

st.title('Streamlit Text Input')

name = st.text_input('Enter your name:')

age = st.slider('What is your age?', 0, 100, 25)

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("Choose your favourite language", options)

if name:
  st.write(f"Hello {name}")
  
st.write(f"Your age is {age}")
st.write(f"You selected {choice}")

data = {
  "Name": ["John", "Jane", "Jake", "Jill"],
  "Age": [28, 24, 35, 40],
  "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv('sample_data.csv')
st.write(df)

uploaded_file = st.file_uploader('Choose a CSV file to upload', type='csv')

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)
