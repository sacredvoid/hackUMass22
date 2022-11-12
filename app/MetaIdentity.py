import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import os
import requests
from Secrets import API_TOKEN
from PIL import Image
#import moviepy.editor as mp

GENERATED_ASSETS = './assets/generated'
UPLOADED_ASSETS = './assets/uploaded'
engine = pyttsx3.init()

def audiototext(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text

def texttoaudio(parent_path,text):
    if text!="":
        #language = 'en'
        #myobj = gTTS(text=text, lang=language, slow=False, tld='com.in')
        #myobj.save(GENERATED_ASSETS+"/reply.mp3")

        # male voice
        engine.save_to_file(text, os.path.join(parent_path,GENERATED_ASSETS)+"/reply.wav")
        engine.runAndWait()

        # read audio and apply style transfer

def chatbot(textinput,  past_user_inputs, generated_responses):

    API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    reply = query({
        "inputs": {
            "past_user_inputs":  past_user_inputs,
            "generated_responses": generated_responses,
            "text": textinput
        },
    })
    return reply["generated_text"]


#--------------------------------
def s2t2huggingface(past_user_inputs, max_convo, generated_responses, text):
    # Storing user input
    if len(past_user_inputs) == max_convo:
        past_user_inputs.pop(0)
    past_user_inputs.append(text)

    # send text to NLP GPT3
    # get the reply back from NLP
    reply = chatbot(text, past_user_inputs, generated_responses)
    # Storing chat output
    if len(generated_responses) == max_convo:
        generated_responses.pop(0)
    generated_responses.append(reply)

    return reply


# get the image from user
# im = Image.open(UPLOADED_ASSETS+"input_img.jpg") 
  
# Get audio from user

# convert to toon - https://github.com/williamyang1991/VToonify
def image2toon(image):
    pass

# toon + audio to video synthezier (Takes input image) - https://github.com/tg-bomze/Face-Image-Motion-Model
def audiotovideo(text):
    if text!="":
        #open audio
        audio = mp.AudioFileClip(GENERATED_ASSETS + "/reply.wav")
        #open video
        video1 = mp.VideoFileClip("./assets/video1.mp4")
        #merge 
        final = video1.set_audio(audio)
        final.write_videofile("output.mp4",codec= 'mpeg4' ,audio_codec='libvorbis')


def imageonvideo(image,video):
    pass

