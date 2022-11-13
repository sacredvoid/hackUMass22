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
from PIL import Image

PARENT_DIR = os.path.dirname(os.path.abspath(__file__))

video_animator = sda.sda.VideoAnimator(gpu=-1, model_path="crema")# Instantiate the animator

st.set_page_config(layout="wide")

def audio_app(col2):
    with col2:
        # Call button to call sr.listen()
        path = os.path.join(PARENT_DIR,"assets/uploaded/sr_input_audio.wav")
        st.session_state['chatbot_status'] = "failed"
        clicked = False
        st.write("Talk to a version of yourself here!")
        try:
            clicked = st.button("Click me 👈...",help="Click to start recording your voice and talking to your bot! It only records max of upto 10 seconds",
                            on_click=save_audio(path,record_audio()))
        except:
            st.error("Unable to record at this time!")
            st.stop
        if clicked:
            print("Saving audio file..")
            text = ""
            try:
                # convert audio to text
                text = audiototext(path)
            except:
                st.error("Recording not clear enough!")
                st.session_state['chatbot_status'] = "failed"
                st.stop

            st.write(f'😎 {text}')
            print("Text from user: ", text)

            # generate reply for text
            botreply = ""
            try:
                botreply = s2t2huggingface(st.session_state['PAST_USER_INPUTS'], 
                st.session_state['MAX_CONVO_WINDOW'], 
                st.session_state['GENERATED_RESPONSE'], text)
            except:
                st.error("Bot could not comprehend you")
                st.session_state['chatbot_status'] = "failed"
                st.stop
            
            print("In app.py, response from bot:"+botreply)
            st.write(f'🤖 {botreply}')
            
            # convert reply to audio -- voice cloning 
            try:    
                texttoaudio(PARENT_DIR,botreply, st.session_state.animate_image_file)
            except:
                st.error("Could not clone your voice!") 
                st.session_state['chatbot_status'] = "failed" 
                st.stop
            
            print("Converting reply to audio")
            st.session_state['chatbot_status'] = "success"

            
def img_selected(option):
    
    if option is "Samanvya": img_name = "1.jpg"
    elif option is "Rajat": img_name = "2.jpg"
    elif option is "HappyWoman": img_name = "toonimage_woman.jpg"
    elif option is "GrumpyMan": img_name = "grumpy_man.bmp"
    else:
        img_name = ""

    print("selected: ", img_name)
    st.session_state['animate_image_file'] = img_name
    try:
        final_img_dir = os.path.join(PARENT_DIR,"assets","uploaded",img_name)
    except:
        st.error("Sorry, the image entered is picked is not found.")
        st.stop
    print("selected: ", final_img_dir)
    return final_img_dir

def chat_train(col3):
    with col3:
        option = st.radio(
                'Would you like to *train* the ChatBot on your own data???',
                ('Yes','No'))

        st.write('You selected:', option)
        if(option == "Yes"): 
            st.session_state['train_chatbot'] = "true"
            st.file_uploader(label="Upload your 📜 chat data here!")
        else: 
            st.session_state['train_chatbot'] = "false"

def video(col1):
    with col1:
        option = st.selectbox(
                'Who would you like to see animated?',
                ('Samanvya', 'Rajat', 'HappyWoman','GrumpyMan'))

        st.write('You selected:', option)
        st.session_state['animate_image_file'] = option
        st.file_uploader("Upload a (well-lit) 📷 photo of your face here!")
        print()
        

def ui():
    coltitle, colimage, coldesc = st.columns([1,1,1])
    with coltitle:
        st.write("""
            # *Meta-Identity*
            ## Create Your Presence in Another Reality Now!!!
            """)

    #with colimage:
    #    st.image(Image.open("Meta-Identity.png"), use_column_width="auto")
    
    with coldesc:
        st.write("""
        ## About us
        We are a privacy-first Metaverse solutions company that can make you a digital avatar, a version of 
        yourself that will be compatible with any Metaverse!
        """)
    
    
    st.markdown("""---""")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.header("Your image goes here")

    with col2:
        st.header("Your audio goes here")
    
    with col3:
        st.header("Your 📜chats go here")
    
    return col1,col2,col3

def main():
    # build_dir = os.path.join(PARENT_DIR, "st_audiorec/frontend/build")
    # st_audiorec = components.declare_component("st_audiorec", path=build_dir)
    st.session_state['PAST_USER_INPUTS'] = []
    st.session_state['MAX_CONVO_WINDOW'] = 5
    st.session_state['GENERATED_RESPONSE'] = []
    st.session_state['DURATION'] = 5
    with st.container():
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
                try:
                    image2toon(target_img_gcp_uri, PARENT_DIR)
                except:
                    st.error("Could not make a toon out of your photo!")
                    st.stop
                print("Generating Digital clone...")
                print("Saving clone...")
                try:
                    audiotovideo(os.path.join(PARENT_DIR,"assets/generated/toonimage.jpg"),os.path.join(PARENT_DIR,"assets/generated/reply.wav"), PARENT_DIR, video_animator)
                except:
                    st.error("Failed to generate tooni-fied video!")
                    st.stop
                print("Done...")
                
                st.markdown("""---""")
                with st.container(): 
                    st.write("""
                    # Demo
                    ## This is how your your digital avatar would look and talk like!
                    """)
                    _, col1, col3 , _ = st.columns([1,1,1,1])
                    with col1:
                        image = Image.open(os.path.join(PARENT_DIR,"assets/generated/toonimage.jpg"))
                        st.image(image, caption="Your \"Toonified\" image")
                    with col3:
                        st.video(os.path.join(PARENT_DIR,"assets/generated/output.mp4"))



if __name__ == "__main__":
    main()