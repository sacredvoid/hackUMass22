import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
import streamlit as st
import streamlit.components.v1 as components
from MetaIdentity import s2t2huggingface, texttoaudio, audiotovideo, audiototext, image2toon
import time
from Secrets import GCP_BUCKET_NAME
import streamlit as st
from sr_audio_recorder import record_audio, save_audio
from gcp_helpers import upload_blob
from faceanimator import sda

PARENT_DIR = os.path.dirname(os.path.abspath(__file__))

# def file_writer(file_like_object):
PAST_USER_INPUTS = []
MAX_CONVO_WINDOW = 5
GENERATED_RESPONSE = []
DURATION = 5
video_animator = sda.sda.VideoAnimator(gpu=-1, model_path="crema")# Instantiate the animator

def audio_app(col2):
    with col2:
        # Call button to call sr.listen()
        path = os.path.join(PARENT_DIR,"assets/uploaded/sr_input_audio.wav")
        st.session_state['chatbot_status'] = "failed"
        clicked = st.button("Click me 👈...",help="Click to start recording your voice and talking to your bot! It only records max of upto 10 seconds",
                            on_click=save_audio(path,record_audio()))
        if clicked:
            print("Saving audio file..")

            try:
                # convert audio to text
                text = audiototext(path)
                st.write(f'😎 {text}')
                print("Text from user: ", text)

                # generate reply for text
                botreply = s2t2huggingface(PAST_USER_INPUTS, MAX_CONVO_WINDOW, GENERATED_RESPONSE, text)
                print("In app.py, response from bot:"+botreply)
                st.write(f'🤖 {botreply}')
                
                # convert reply to audio -- voice cloning 
                texttoaudio(PARENT_DIR,botreply)
                
                print("Converting reply to audio")
            except Exception as e:
                st.error("Something went wrong while conversing!: ",e)
                st.session_state['chatbot_status'] = "failed"
            
            st.session_state['chatbot_status'] = "success"

            
def img_selected(option):
    
    if option is "Samanvya": img_name = "1.jpg"
    elif option is "Rajat": img_name = "2.jpg"
    elif option is "Disney Character": img_name = "toonimage_woman.jpg"
    elif option is "Grumpy man": img_name = "grumpy_man.bmp"
    else:
        img_name = ""

    print("selected: ", img_name)
    st.session_state['animate_image_file'] = img_name
    try:
        final_img_dir = os.path.join(PARENT_DIR,"assets","uploaded",img_name)
    except:
        st.error("Sorry, the image entered is picked is not found.")
    print("selected: ", final_img_dir)
    return final_img_dir

def chat_train(col3):
    with col3:
        option = st.radio(
                'Would you like to train the ChatBot on your own data???',
                ('Yes','No'))

        st.write('You selected:', option)
        if(option == "Yes"): st.session_state['train_chatbot'] = "true"
        else: st.session_state['train_chatbot'] = "false"

def video(col1):
    with col1:
        option = st.selectbox(
                'Who would you like to see animated?',
                ('Samanvya', 'Rajat', 'Disney Character','Grumpy man'))

        st.write('You selected:', option)
        st.session_state['animate_image_file'] = option
        

def ui():
    st.write("""
        # MetaIdentity
        ## One stop shop for all your Avatar needs
        Create your identity on the Metaverse now!!!
        """)
    col1, col2, col3 = st.columns([10, 10, 10])
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
    video(col1)
    chat_train(col3)
    if(st.session_state.chatbot_status == "success"):
        if (st.session_state.animate_image_file != ""):
            target_img_gcp_uri = upload_blob(GCP_BUCKET_NAME,img_selected(st.session_state.animate_image_file))
            # Call image input on col1
            # Call chat input on col3
            # # update this with gcp link
            print("******!!!!!!!,,,,,,,",target_img_gcp_uri)
            image2toon(target_img_gcp_uri, PARENT_DIR)
            print("Generating Digital clone...")
            print("Saving clone...")
            audiotovideo(os.path.join(PARENT_DIR,"assets/generated/toonimage.jpg"),os.path.join(PARENT_DIR,"assets/generated/reply.wav"), PARENT_DIR, video_animator)
            print("Done...")


if __name__ == "__main__":
    main()