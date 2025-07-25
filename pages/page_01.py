import requests
import streamlit as st
import numpy as np


st.set_page_config(page_title="Hello")


st.markdown("# Streamlit is awesome !")


query = st.text_input("Search a GIF")
url = "https://api.giphy.com/v1/gifs/search"

st.write(st.secrets)

params = {"api_key": st.secrets['API_KEYS']['GIPHY'],
          "q": query,
          "limit": 10}
response = requests.get(url, params=params).json()

while not query:
    st.stop()

gif_url = response['data'][0]['embed_url']
st.write(f'<iframe src="{gif_url}" width="480" height="240">', unsafe_allow_html=True)
