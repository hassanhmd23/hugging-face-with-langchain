from dotenv import load_dotenv
import requests
from os.path import join, dirname
import os
import streamlit as st

load_dotenv(join(dirname(__file__), ".env"))


def image_to_text(image: str) -> str:
    api_url = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
    headers = {"Authorization": f'Bearer {os.environ.get("HUGGING_FACE_TOKEN")}'}

    with open(image, "rb") as f:
        data = f.read()
    response = requests.post(api_url, headers=headers, data=data)
    return response.json()[0]['generated_text']


def main():
    st.set_page_config(page_title="img to audio description", page_icon="🤖")

    st.header("Turn Image to Audio Description")
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        with open(uploaded_file.name, "wb") as file:
            file.write(bytes_data)
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
        description = image_to_text(uploaded_file.name)

        with st.expander("description"):
            st.write(description)


if __name__ == "__main__":
    main()
