import speech_recognition as sr
def record_audio():
    r = sr.Recognizer()
    print("Initialized sr recognizer")
    with sr.Microphone() as source:
        print("inside microphone")
        audio = r.listen(source, timeout=10, phrase_time_limit=5)
    
    return audio
    
def save_audio(path, audio):
    with open(path, "wb") as f:
        f.write(audio.get_wav_data())