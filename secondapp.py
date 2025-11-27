import streamlit as st
# Page Setup
st.set_page_config(page_title="😇 My streamlit app - Sareeyah")

st.title("Layout And Sidebar")
col1, col2 = st.columns(2)

with col1:
    st.header("Left Side")
    name = st.text_input("Enter Your Name ?")
    if name:
        st.success(f"Welcome User {name} !")

with col2:
    st.header("Odd Even Checker")
    num = st.slider("Select A Number",1,100,3)
    if num%2==0:
        st.write("Even Number")
    else:
        st.write("Odd Number")


with st.sidebar:
    st.header("Control Panel")
    user_color = st.color_picker("Pick Your Favorite Color","#000000")
    st.write("You have selected :",user_color)

# in sidebar provide 2 options to user
# select dark or light theme
# if user select dark change the theme of streamlit app

# ------------------ SIDEBAR TOGGLE SWITCH ------------------
st.sidebar.write("### Theme")

toggle = st.sidebar.checkbox("Dark Mode 🌙", value=False)

# ------------------ BASE CSS WITH ANIMATION ------------------
base_css = """
<style>
/* Smooth transition on theme change */
[data-testid="stAppViewContainer"], body {
    transition: background-color 0.5s ease, color 0.5s ease;
}
</style>
"""

# ------------------ LIGHT & DARK CSS ------------------
light_css = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #FFFFFF;
    color: #000000;
}

/* Fix input labels */
label, .stSlider > label, .stTextInput > label {
    color: #000 !important;
}
</style>
"""

dark_css = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0E1117;
    color: #FFFFFF;
}

/* Fix input labels */
label, .stSlider > label, .stTextInput > label {
    color: #FFF !important;
}
</style>
"""

# ------------------ APPLY CSS ------------------
st.markdown(base_css, unsafe_allow_html=True)

if toggle:
    st.markdown(dark_css, unsafe_allow_html=True)
    theme_label = "Dark Mode 🌙"
else:
    st.markdown(light_css, unsafe_allow_html=True)
    theme_label = "Light Mode ☀️"

# ------------------ PAGE CONTENT ------------------
st.title("🌗 Animated Theme Switch (Dark / Light)")
st.write(f"Current theme: **{theme_label}**")



