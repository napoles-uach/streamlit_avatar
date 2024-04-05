import streamlit as st
from streamlit_avatar import avatar


prompt = st.chat_input("Say something",key=0)
avatar(prompt)
