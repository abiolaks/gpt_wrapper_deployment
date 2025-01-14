# streamlit deployement
import streamlit as st

import streamlit as st
from gpt_wrapper import generate_text, generate_image

# title of the app
st.title("Thought and Imaginations are Real- KING AI")

# Header for the openai wrapper
st.header("Text Generator")

# text box for prompt
open_ai_prompt = st.text_input("Enter your prompt")

# button to send the prompt
if st.button("Send"):  # check wether the button for our prompt is clicked
    # gpt method text generation
    generate_text(open_ai_prompt)
    # success message
    st.sucess("Content generated successfully")
else:
    # error message if prompt is not entered.
    # st.error("Content generation failed")
    st.warning("Please insert a prompt")

st.divider()

st.header("Image Generation")
# variable to store the prompt
openai_image_prompt = st.text_input("Enter your prompt", key=2)

if st.button("Send", key=3):
    # gpt method image generation
    generate_image(openai_image_prompt)
    st.success("Image generated successfully")
else:
    st.warning("Please insert a prompt to generate an image")
