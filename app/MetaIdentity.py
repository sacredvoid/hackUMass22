import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import os
import requests
from Secrets import API_TOKEN
from PIL import Image
# import moviepy.editor as mp
import requests

import requests # request img from web
import shutil # save img locally

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

# convert to toon
def image2toon(image, parent_path):

    """
    r = requests.post(
        "https://api.deepai.org/api/toonify",
        files={
            'image': open(image, 'rb'),
        },
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    print(r.json())
    """

    """
    import replicate
    model = replicate.models.get("minivision-ai/photo2cartoon")
    version = model.versions.get("39a9e414d9ed06af42f0b98e9b4c96c34b7aa712")
    output = version.predict(photo=image)
    
    """

    #https://rapidapi.com/sensorai-sensorai-default/api/3d-cartoon-face/
    url = "https://3d-cartoon-face.p.rapidapi.com/run"

    gcplink = "https://jixjiastorage.blob.core.windows.net/public/sensor-ai/3d_cartoon_face/1.jpg"

    payload = {
        "image": gcplink,
        "render_mode": "3d",
        "output_mode": "url"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "007e1eee8dmshe8856ed6b250f8fp123656jsn93ffb4c92092",
        "X-RapidAPI-Host": "3d-cartoon-face.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.text)

    url = response.json()["output_url"]
    file_name = os.path.join(parent_path,GENERATED_ASSETS) +"/toonimage.jpg"
    res = requests.get(url, stream = True)

    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',file_name)
    else:
        print('Image Couldn\'t be retrieved')
    
    
    
# toon image + audio
def audiotovideo(image, audio, parent_path, va):
    vid, aud = va(image, audio)
    va.save_video(vid, aud, os.path.join(parent_path,GENERATED_ASSETS) +"/output.mp4")
    
    """
    if text!="":
        #open audio
        audio = mp.AudioFileClip(os.path.join(parent_path,GENERATED_ASSETS) + "/reply.wav")
        #open video
        video1 = mp.VideoFileClip(os.path.join(parent_path,UPLOADED_ASSETS)+"./video1.mp4")
        #merge 
        final = video1.set_audio(audio)
        final.write_videofile(os.path.join(parent_path,GENERATED_ASSETS) +"output.mp4",codec= 'mpeg4' ,audio_codec='libvorbis')
    """

