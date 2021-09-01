import base64
import requests

import streamlit as st

headers = {
        "Content-Type": "text/plain"
    }

st.title("Welcome to the demo!")
url = st.text_input(label="api url")
instructions = "Either upload your own image or select from the sidebar to get a preconfigured image. " \
               "The image you select or upload will be fed through the algorithm and the output will be displayed to the screen."
st.write(instructions)

image_file = st.file_uploader('Upload An Image')

if image_file:
    encoded_string = base64.b64encode(image_file.read())
    st.title("Here is the image you've selected")
    st.image(image_file)
    response = requests.request("POST", url, headers=headers, data=encoded_string)
    st.title("Here is the most likely prediction:")
    st.write(response.text)


st.write("Made with ♡ by the DS team")