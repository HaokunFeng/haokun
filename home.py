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


st.markdown("#### 👋 Greetings ")
st.markdown("Hi, I'm Haokun Feng, a robotics reseacher at the University of Washington. "
            "I'm passionate about robotics, machine learning, and computer vision. "
            "And I'm also interested in web development and data visualization. "
            "Currently I'm working on developing algorithms for robotic manipulation and grasping. "
            "I hope to use my skills to make the world a better place. ")
st.markdown("In my free time, I enjoy hiking, and traveling. "
            "I'm also a big fan of photography and I love to capture the beauty of the world. "
            "Besides, I'm always looking for new opportunities and challenges. "
            "In the future, I hope to become an entrepreneur work on projects that can change the world."
            "Feel free to reach out to me if you have any questions or just want to chat. ")

st.markdown("---")
st.markdown("#### 📚 Contact ")
st.markdown("📧 Email: haokunf@uw.edu")
st.markdown("🌐 Website: [Github](https://github.com/HaokunFeng)")
st.markdown("📝 Twitter: [Haokun Feng](https://twitter.com/Haokun_Feng)")