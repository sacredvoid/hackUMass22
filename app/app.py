import os
import streamlit as st
import streamlit.components.v1 as components
from MetaIdentity import s2t2huggingface, GENERATED_ASSETS, UPLOADED_ASSETS, texttoaudio, audiotovideo, audiototext
import time
import streamlit as st
from audiorecorder import audiorecorder
from sr_audio_recorder import record_audio, save_audio
PARENT_DIR = os.path.dirname(os.path.abspath(__file__))

# def file_writer(file_like_object):
PAST_USER_INPUTS = []
MAX_CONVO_WINDOW = 5
GENERATED_RESPONSE = []
DURATION = 5


def audio_app():
    st.write("""
    # RIP
    Our first app
    """)
    # Call button to call sr.listen()
    # audio = audiorecorder("Click to record", "Recording...")
    path = os.path.join(PARENT_DIR,"assets/uploaded/sr_input_audio.wav")
    # path = "input2_audio.mp3"
    st.write("""
    Trying to run this file
    """)
    save_audio(path,record_audio()) 

    text = audiototext(path)
    print(text)
    botreply = s2t2huggingface(PAST_USER_INPUTS, MAX_CONVO_WINDOW, GENERATED_RESPONSE, text)
    print(botreply)
    texttoaudio(PARENT_DIR,botreply)
    audiotovideo(botreply)
    print("In app.py, response from bot:"+botreply)
    
    #st_audiorec()
    uploaded_file = st.file_uploader("Choose a file")
    if(uploaded_file is not None):
        # Call the s2t2huggingface here
        write_audio_file(path,uploaded_file)

        text = audiototext(path)
        botreply = s2t2huggingface(PAST_USER_INPUTS, MAX_CONVO_WINDOW, GENERATED_RESPONSE, text)
        texttoaudio(botreply)
        audiotovideo(botreply)
        print("In app.py, response from bot:"+botreply)



    
    

def main():
    # build_dir = os.path.join(PARENT_DIR, "st_audiorec/frontend/build")
    # st_audiorec = components.declare_component("st_audiorec", path=build_dir)
    audio_app()


if __name__ == "__main__":
    main()