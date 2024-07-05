import streamlit as st
import google.generativeai as genai

#api_key = st.secrets["GOOGLE_API_KEY"]
#genai.configure(api_key=api_key)
genai.configure(api_key="AIzaSyAuzUJj270D6XRjFzWG8dSJzlU509TEyxQ")

model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Taz")

with col2:
    st.image("images/taz.jpg")

st.title(" ")

st.title("Taz's AI Bott")
user_question = st.text_input("Ask anything about me")

if st.button("ASK", use_container_width=400):
    prompt = user_question
    response = model.generate_content(prompt)
    st.write(response.text)
    # print(response.text)

st.title(" ")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Taz Channel")


with col2:
    st.video("https://youtu.be/BFlRmIvqwSA?si=a6qL3krtRgqVIKOZ")

st.title(" ")

st.title("My Setup")
st.image("images/setup.jpg")

# st.subheader(" ")
st.write(" ")
st.slider("Programming", 0,100,70)
st.slider("Teaching", 0,100,70)
st.slider("Robotics", 0,100,70)

# st.file_uploader("Upload a file")
st.write(" ")
st.title("Gallery")

col1,col2,col3 = st.columns(3)

with col1:
    st.image("images/g1.jpg")
    st.image("images/g2.jpg")
    st.image("images/g3.jpg")

with col2:
    st.image("images/g4.jpg")
    st.image("images/g5.jpg")
    st.image("images/g6.jpg")

with col3:
    st.image("images/g7.jpg")
    st.image("images/g8.jpg")
    st.image("images/g9.jpg")

st.write("CONTACT")
st.title("For any inquiries, please contac me at:")
st.write("polarnikka@google.com")
