from flask import Flask, request, Response
from twilio.twiml.messaging_response import MessagingResponse, Body, Message, Redirect
import requests 

API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
API_TOKEN = "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"

past_user_inputs = []
generated_responses = []

app = Flask(__name__)
 
@app.route("/wa")
def wa_hello():
    return "Hello, World!"
 
@app.route("/wasms", methods=['POST'])
def wa_sms_reply():
    msg = request.form.get('Body').lower() 
    print("msg-->",msg)
    
    if len(past_user_inputs)==5:
        past_user_inputs.pop(0)
    past_user_inputs.append(msg)

    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()    
    r = query({
        "inputs": {
            "past_user_inputs":  past_user_inputs,
            "generated_responses": generated_responses,
            "text": msg
        },
    })
    print(r["generated_text"])


    if msg:
        response = MessagingResponse()
        response.message(r["generated_text"])
        return Response(str(response), mimetype="application/xml")
 
if __name__ == "__main__":	
    app.run(debug=True)