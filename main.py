import streamlit as st

st.title("Welcome to Python Web Application")

name = st.text_input("Enter Your Name: ")
fname = st.text_input("Enter Your Father Name: ")
adr = st.text_area("Enter Your Text: ")
classdata = st.selectbox("Enter Your Class : ",(1,2,3,4,5, 6,7,8,9,10,12,))

button = st.button("Done")

if button :
  st.markdown(f"""
  Name : {name}
  Father Name : {fname}
  Address : {adr}
  Class :{classdata}""")