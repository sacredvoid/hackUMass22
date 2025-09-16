# Meta-Identity 🚀

[![HackUMass Winner](https://img.shields.io/badge/HackUMass%20'22-Best%20AI%2FML%20Hack-brightgreen?style=for-the-badge&logo=github)](https://devpost.com/software/meta-identity-0t94fp)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.14.1-red?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-1.13.1-orange?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

![Meta-Identity](https://user-images.githubusercontent.com/33939902/201859267-ff740ab5-2c66-42b6-b0b5-43d4fe53b98e.png)

**Create Your Digital Clone for the Metaverse** 🎭

Meta-Identity is an innovative AI-powered platform that creates digital avatars that look, sound, and behave like you. This project won **"Best AI/ML Hack"** at HackUMass '22 and represents a breakthrough in digital identity creation for the metaverse.

## 🌟 Features

- **🎭 Digital Avatar Creation**: Transform your photos into animated digital avatars
- **🗣️ Voice Cloning**: Generate speech that sounds like your own voice
- **🧠 Personality Cloning**: Train AI on your chat data to replicate your personality
- **🎬 Video Generation**: Create talking head videos with lip-sync
- **📱 Multi-Platform Integration**: WhatsApp and SMS capabilities via Twilio
- **☁️ Cloud Deployment**: Scalable Google Cloud Platform integration

## 🏆 Awards & Recognition

- **🥇 Best AI/ML Hack** - HackUMass '22
- **📱 Featured on Devpost** - [View Project](https://devpost.com/software/meta-identity-0t94fp)

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google Cloud Platform account
- Twilio account (for messaging features)
- Hugging Face API token

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/meta-identity.git
   cd meta-identity
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `Secrets.py` file with your API credentials:
   ```python
   API_TOKEN = "your_huggingface_token"
   TOON_KEY = "your_rapidapi_key"
   GCP_BUCKET_NAME = "your_gcp_bucket"
   GCP_CREDENTIALS = "path_to_gcp_credentials.json"
   STORAGE_LINK_HEADER = "https://storage.googleapis.com/"
   ```

4. **Run the application**
   ```bash
   streamlit run app/app.py
   ```

## 🏗️ Architecture

Meta-Identity combines multiple cutting-edge AI technologies:

### Core Components

1. **Personality Cloning** 🧠
   - Uses GPT-2 architecture for conversational AI
   - Trains on WhatsApp, Facebook, and Instagram chat data
   - Maintains conversation context and personality traits

2. **Voice Cloning** 🗣️
   - GAN-based voice spectral transfer learning
   - Text-to-speech with personalized voice characteristics
   - Gender-specific voice modulation

3. **Face Animation** 🎭
   - StyleGAN and StackGAN for image generation
   - RNN LSTM for audio-visual correlation
   - Real-time lip-sync with speech

4. **Video Synthesis** 🎬
   - Combines animated face with cloned voice
   - Generates MP4 output with synchronized audio
   - Cloud-optimized processing pipeline

### Technology Stack

- **Frontend**: Streamlit, React (TypeScript)
- **Backend**: Python, Flask
- **AI/ML**: TensorFlow, PyTorch, Hugging Face Transformers
- **Cloud**: Google Cloud Platform, Google Cloud Storage
- **APIs**: Twilio (SMS/WhatsApp), RapidAPI (3D Cartoon Face)
- **Audio Processing**: SpeechRecognition, pyttsx3, gTTS

## 📁 Project Structure

```
meta-identity/
├── app/                          # Main application
│   ├── app.py                   # Streamlit main application
│   ├── MetaIdentity.py          # Core AI functionality
│   ├── gcp_helpers.py           # Google Cloud integration
│   ├── sr_audio_recorder.py     # Audio recording component
│   ├── faceanimator/            # Face animation library
│   │   ├── sda/                 # Speech-driven animation
│   │   └── main.py              # Animation examples
│   ├── st_audiorec/             # Audio recorder frontend
│   └── assets/                  # Media files
├── Twilio Bot/                  # WhatsApp/SMS integration
│   └── app.py                   # Flask bot server
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## 🎯 How It Works

### 1. Data Collection
- Upload your photo for avatar creation
- Record voice samples for voice cloning
- Provide chat data for personality training

### 2. AI Processing
- **Image Processing**: Convert photo to cartoon-style avatar
- **Voice Analysis**: Extract voice characteristics and patterns
- **Personality Training**: Process chat data to understand communication style

### 3. Digital Clone Generation
- Generate personalized responses using trained models
- Convert text to speech with cloned voice
- Create animated video with lip-sync

### 4. Output
- Interactive digital avatar
- Video files with synchronized audio
- WhatsApp/SMS integration for remote interaction

## 🔧 Configuration

### Model Selection
The face animator supports multiple pre-trained models:
- `grid` - GRID dataset (default)
- `timit` - TCD-TIMIT dataset
- `crema` - CREMA-D dataset
- `lrw` - LRW dataset

### Voice Settings
- Male voice (default)
- Female voice (for "HappyWoman" character)
- Adjustable speech rate and volume

## 🌐 API Integration

### Required APIs
1. **Hugging Face** - For DialoGPT conversation model
2. **RapidAPI** - For 3D cartoon face generation
3. **Google Cloud** - For file storage and processing
4. **Twilio** - For WhatsApp and SMS capabilities

### Rate Limits
- Hugging Face: 1000 requests/month (free tier)
- RapidAPI: Varies by plan
- Google Cloud: Pay-per-use
- Twilio: Varies by plan

## 🚀 Deployment

### Local Development
```bash
# Start the main application
streamlit run app/app.py

# Start the Twilio bot (separate terminal)
cd "Twilio Bot"
python app.py
```

### Cloud Deployment
1. Deploy to Google Cloud Run
2. Set up Google Cloud Storage bucket
3. Configure environment variables
4. Set up Twilio webhook endpoints

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Team

- **Samanvya** - AI/ML Engineer
- **Rajat** - Full Stack Developer

## 🔮 Future Roadmap

- **AR/VR Integration**: Move from 2D to 3D avatars
- **Real-time Processing**: Live avatar generation
- **Enhanced Personality**: More sophisticated personality modeling
- **Multi-language Support**: Support for multiple languages
- **Mobile App**: Native mobile application

## 🐛 Known Issues

- Audio recording may fail on some systems
- Large file uploads may timeout
- Voice cloning quality varies by input quality

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Contact us via [Devpost](https://devpost.com/software/meta-identity-0t94fp)

## 🙏 Acknowledgments

- Hugging Face for the DialoGPT model
- Google Cloud Platform for infrastructure
- Twilio for messaging capabilities
- The open-source community for various libraries

---

**Built with ❤️ for the future of digital identity**

*Meta-Identity - Where You Meet Your Digital Self* 🚀