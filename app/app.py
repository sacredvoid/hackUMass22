import os
import streamlit as st
import streamlit.components.v1 as components
from MetaIdentity import s2t2huggingface, GENERATED_ASSETS, UPLOADED_ASSETS
# def file_writer(file_like_object):
PAST_USER_INPUTS = []
MAX_CONVO_WINDOW = 5
GENERATED_RESPONSE = []


def write_audio_file(path, data):
    with open(path, mode='bx') as f:
        f.write(data)

def audio_app(st_audiorec):
    st.write("""
    # RIP
    Our first app
    """)
    st_audiorec()
    uploaded_file = st.file_uploader("Choose a file")
    if(uploaded_file is not None):
        # Call the s2t2huggingface here
        path = os.path.join(UPLOADED_ASSETS,"input_audio.wav")
        write_audio_file(path,uploaded_file)
        botreply = s2t2huggingface(PAST_USER_INPUTS, MAX_CONVO_WINDOW, GENERATED_RESPONSE)
        print("In app.py, response from bot:"+botreply)


def main():
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "st_audiorec/frontend/build")
    st_audiorec = components.declare_component("st_audiorec", path=build_dir)
    audio_app(st_audiorec)


if __name__ == "__main__":
    main()