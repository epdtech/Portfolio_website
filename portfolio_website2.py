# 1. Add the streamlit library to the project.
import streamlit as st
# to test
# streamlit run epdtech_web.py

# 2. Add the title to the app.
st.title('Welcome to EPDTech / KP-Toys')



# 5. Subheader
st.subheader('Diy mole repeller')

# 22. Adding Columns
col1, col2 ,col3 = st.columns(3)

with col1:
#     # placeholder.image(image, caption='2022 UK Trip with Mom', use_column_width='always')
     st.image("images/Diy mole repeller1.jpg")
#     st.text('Running time about 50 days ')
#     st.text('with 2500 milliamp capacity battery.')
# st.write("""
# # Running time about 50 days
# # with 2500 milliamp capacity battery*
# """)
with col2:
# 5. Subheader
    st.subheader('Mini Arcades')


    #st.video("https://youtu.be/BFlRmIvqwSA?si=a6qL3krtRgqVIKOZ")
    st.image("images/Mini Arcades.jpg")

with col3:
# 5. Subheader
    st.subheader('DIY marlboro maze')


    #st.video("https://youtu.be/BFlRmIvqwSA?si=a6qL3krtRgqVIKOZ")
    st.image("images/diy marlboro maze.jpg")


col1, col2 = st.columns(2)
with col1:
    st.subheader('Diy mole repeller')
    st.text('Running time about 50 days ')
    st.text('with 2500 milliamp capacity battery.')

with col2:
    st.image("images/Diy mole repeller1.jpg")
