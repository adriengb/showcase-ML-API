import base64
import requests
import json

import streamlit as st
import plotly.graph_objects as go


headers = {
        "Content-Type": "text/plain"
    }

st.title("Welcome to the demo!")
url = st.text_input(label="Please paste here the url of the service we provide you")
instructions = "Either upload your own image or select from the sidebar to get a preconfigured image. " \
               "The image you select or upload will be fed through the algorithm and the output will be displayed to the screen."
st.write(instructions)

image_file = st.file_uploader('Upload An Image')

if image_file:
    encoded_string = base64.b64encode(image_file.read())
    st.subheader("Here is the image you've selected")
    st.image(image_file)
    response = requests.request("POST", url, headers=headers, data=encoded_string)
    pred = json.loads(response.text)
    st.subheader("Here is the most likely prediction")
    most_likely_cat = max(pred, key=pred.get)
    confidence = max(pred.values())
    st.write("{} with a confidence of {}%".format(most_likely_cat, round(confidence*100, 0)))
    fig = go.Figure(go.Bar(
        x=list(pred.values()),
        y=list(pred.keys()),
        orientation='h'))
    st.plotly_chart(figure_or_data=fig)

st.write("Made with ♡ by the DS team")