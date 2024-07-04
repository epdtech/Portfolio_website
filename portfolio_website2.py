import streamlit as st
import google.generativeai as genai

api_key = st.secrets=["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Murtaza Hassan")

with col2:
    st.image("Images/taz.jpg")

st.title(" ")

st.title("Murtaza's AI Bot")
user_question = st.text_input("Ask anything about me")

if st.button("ASK", use_container_width=400):
    prompt = user_question
    response = model.generate_content(prompt)
    st.write(response.text)
    # print(response.text)

