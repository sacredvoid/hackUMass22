# Meta-Identity
![Meta-Identity](https://user-images.githubusercontent.com/33939902/201859267-ff740ab5-2c66-42b6-b0b5-43d4fe53b98e.png)
**This is our winning submission for HackUMass '22, where we were named the 'Best AI/ML Hack'.**

## Inspiration
In the world today, the number of people using the internet and social media, and creating a digital presence, has been increasing day by day. At this rate, the internet can be treated as another universe itself. This led to our inspiration of creating Meta-Identity, which directly translates to one personifying his or her own real personality into a digital clone. Meta-Identity facilitates and provides a way to create your presence in the metaverse and digital sphere, by actually truly being in it, while not being it in at the same time.

## What it does
Meta-Identity clones one's personality, voice, and facial looks into a digital form. The aim is to create a clone of one's self that would be indistinguishable from the real person. Meta-Identity builds one's presence in the virtual world, without the person directly controlling their clone. The clone is a copy of the person, with its own digital thought process. Meta-Identity creates your digital clone, who looks like you, can speak like you, and can act like you. The Digital personification is exactly like a real person, where not only he/she can talk to a human, but can also send message and call humans based on will (Powered by Twilio).

## How we built it
We used 3 ML models to build this software - 1) Personality cloning via NLP chatbot, 2) Speech cloning via GANs, 3) Face and digital avatar creation and cloning using StackGAN and RNN LSTM. The personality is cloned with the help of WhatsApp, Facebook, and Instagram chat data of the user. The chat is used as a dataset, as the way a person talks on chat gives out a lot about what the person likes or what their personality is as a whole. The NLP chat bot was built from scratch using GPT-2 architecture. Secondly, the digital avatar should sound like the person themselves and this is done by speech cloning using GANs voice spectral transfer learning. Lastly, the digital clone should look like the person, and this is done using two ML models - Toonify and creating the animated digital character of the person, based on the input image given, and generating and synthesizing audio with the image to produce a conversational video. The image translation and video synthesizer models were built using RNN LSTM for correlating audio with the image and lipsync. The digital avatar is created using StyleGAN and StackGAN. We additionally expanded our digital persona to have capabilities to call and send whatsapp messages to humans. This is powered by Twilio APIs. Also, all the 3 ML models which we built are deployed on Google Cloud.

## Challenges we ran into
We bumped into many challenges throughout the 36 hours. The Major challenge we bumped into was creating a true personification of a person based on their chat data. Using state of art GPT - 2 proved to be handy, however, training and avoiding overfitting the chat data was a big challenge, which we overcame by experimenting and analyzing. Another challenge was to integrate all the models to create the digital clone in a shorter and quicker time.

## Accomplishments that we're proud of
We finished our project in 36 hours!

## What we learned
We learnt how to built scalable software solutions in the field of ML with multiple ML models, with low latency and high performance.

## What's next for Meta-Identity
The next step for this project would be to move it into the AR/VR shere. Currently our digital clone is restricted to a 2D image. The next step would be to bring the 2D clone into a 3D space and into AR/VR technologies.

## Devpost
https://devpost.com/submit-to/16758-hackumass-x/manage/submissions/370074-meta-identity/finalization

## Run Locally
1) pip install -r requirements
2) streamlit run app.py
