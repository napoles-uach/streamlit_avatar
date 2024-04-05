import streamlit as st
from streamlit_avatar import avatar

text = "Hola, este es un ejemplo."
lang = "es"

prompt = st.chat_input("Say something",key=0)
avatar(prompt)#, n_frames, url, lang)
