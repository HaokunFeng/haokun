import streamlit as st

st.set_page_config(
    page_title="MyHomepage",
    page_icon="🚩",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None,
)

st.title("🌎 Welcome to my homepage")
st.caption("This is a simple homepage created using Streamlit. Feel free to explore the different pages and widgets.")


st.markdown("#### Greetings 👋")
st.markdown("Hi, I'm Haokun Feng, a robotics reseacher at the University of Washington."
            "I'm passionate about robotics, machine learning, and computer vision. ")

st.markdown("---")
st.markdown("#### 📚 Contact")
st.markdown("📧 Email: haokunf@uw.edu")
st