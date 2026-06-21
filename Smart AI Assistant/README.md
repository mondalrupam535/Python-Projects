# 🤖 Smart AI Assistant

Smart AI Assistant listens to your voice, transcribes it, and responds instantly using Groq AI. It combines speech recording, automatic transcription, and AI chat completion to deliver a fast, spoken conversational assistant.

## ✨ Features

- Voice input recording
- Speech-to-text transcription
- AI-powered responses
- Text-to-speech output

## 🛠️ Tech Stack

- Python
- `sounddevice` for recording audio
- `scipy` for saving WAV files
- `pyttsx3` for text-to-speech
- `openai` client for Groq AI integration
- `GROQ_API_KEY` environment variable for secure credentials

## 🚀 Usage

1. Set the `GROQ_API_KEY` environment variable.
2. Run the script from the `Smart AI Assistant` folder.
3. Speak when prompted.
4. The assistant will reply with a spoken response.

## 📌 Notes

- The API key is read from an environment variable to avoid storing secrets in the repository.
- Adjust the recording duration and models as needed.
