import streamlit as st
import requests
# from src.settings import BASE_SETTINGS

question_input = st.text_input("Question:")

if question_input:
    # url = f"{BASE_SETTINGS.API_URL}/query/"
    url = f"http://fastapi:8000/query/"
    response = requests.post(url, json={"txt": question_input})
    if response.status_code != 200:
        raise Exception(f"Error: API request unsuccessful. Status code: {response.status_code}")
    answer = response.json()["txt"]
    st.text_area("Answer:", answer)

