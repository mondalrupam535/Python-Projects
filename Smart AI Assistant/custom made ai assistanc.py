import os
import time
import sounddevice as sd
from scipy.io.wavfile import write
from openai import OpenAI
import pyttsx3

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise EnvironmentError("Please set the GROQ_API_KEY environment variable before running this script.")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

def record_audio():
    fs = 16000
    duration = 2

    input("\nPress Enter and start speaking...")

    print("Listening...")

    recording = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write("voice.wav", fs, recording)


def speech_to_text():
    with open("voice.wav", "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-large-v3"
        )

    return transcription.text.strip()


def ask_ai(question):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": f"{question}\nAnswer in about 5 concise sentences."
            }
        ]
    )

    return response.choices[0].message.content.strip()


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


while True:
    try:
        record_audio()

        text = speech_to_text()

        if len(text) < 3:
            print("No speech detected.")
            continue

        print(f"\nYou: {text}")

        if text.lower() in ["exit", "quit", "stop", "bye"]:
            speak("Goodbye")
            break

        answer = ask_ai(text)

        print(f"\nAI: {answer}\n")

        speak(answer)

        time.sleep(1)

        if os.path.exists("voice.wav"):
            os.remove("voice.wav")

    except KeyboardInterrupt:
        print("\nExiting...")
        break

    except Exception as e:
        print("Error:", e)
