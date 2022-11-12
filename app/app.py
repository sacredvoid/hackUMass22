import os
import streamlit as st
import streamlit.components.v1 as components
from MetaIdentity import s2t2huggingface, GENERATED_ASSETS, UPLOADED_ASSETS, texttoaudio, audiotovideo, audiototext, image2toon
import time
import streamlit as st
from audiorecorder import audiorecorder
from sr_audio_recorder import record_audio, save_audio
from gcp_helpers import upload_blob, download_blob

PARENT_DIR = os.path.dirname(os.path.abspath(__file__))

# def file_writer(file_like_object):
PAST_USER_INPUTS = []
MAX_CONVO_WINDOW = 5
GENERATED_RESPONSE = []
DURATION = 5


def audio_app(col2):
    with col2:
        # Call button to call sr.listen()
        path = os.path.join(PARENT_DIR,"assets/uploaded/sr_input_audio.wav")
        st.button("Click to record...",help="Click to start recording your voice! It only records max of upto 10 seconds",on_click=save_audio(path,record_audio()))
        # audio = audiorecorder("Click to record", "Recording...")
        # path = "input2_audio.mp3"
        st.write("""
        ### Audio file saved I guess...
        """)
        # save_audio(path,record_audio()) 

        text = audiototext(path)
        st.write("""
        ### Audio  
        """)
        print(text)
        botreply = s2t2huggingface(PAST_USER_INPUTS, MAX_CONVO_WINDOW, GENERATED_RESPONSE, text)
        print(botreply)
        texttoaudio(PARENT_DIR,botreply)
        # audiotovideo(botreply, PARENT_DIR)
        # image2toon(os.path.join(PARENT_DIR,"assets/uploaded/c.jpg"), PARENT_DIR)

        print("In app.py, response from bot:"+botreply)

def ui():
    st.write("""
        # RIP
        Create your identity on the Metaverse now!!!
        """)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Your image goes here")

    with col2:
        st.header("Your audio goes here")
    
    with col3:
        st.header("Your chats go here")
    
    return col1,col2,col3

def main():
    # build_dir = os.path.join(PARENT_DIR, "st_audiorec/frontend/build")
    # st_audiorec = components.declare_component("st_audiorec", path=build_dir)
    col1, col2, col3  = ui()
    audio_app(col2)
    # Call image input on col1
    # Call chat input on col3


if __name__ == "__main__":
    main()