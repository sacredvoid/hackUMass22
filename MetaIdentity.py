
import speech_recognition as sr
from gtts import gTTS
import os
import requests
from Secrets import API_TOKEN
from PIL import Image

def audiototext(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
        return text

def texttoaudio(text):
    language = 'en'
    myobj = gTTS(text=reply, lang=language, slow=False)
    myobj.save("reply.mp3")

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


#----------------------------------------------------
max_convo = 5
past_user_inputs = []
generated_responses = []


#--------------------------------
# get the image from user
im = Image.open("input_img.jpg") 
  

# Get audio from user
filename = "input_audio.wav"
text = audiototext(filename)

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
print(reply)

# text to audio - reply.mp3
texttoaudio(reply)


# convert to toon - https://github.com/williamyang1991/VToonify

# toon + audio to video synthezier (Takes input image) - https://github.com/tg-bomze/Face-Image-Motion-Model