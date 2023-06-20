from TTS.api import TTS
import speech_recognition as sr
import os
from playsound import playsound

# List available 🐸TTS models and choose the first one
model_name = 'tts_models/en/ljspeech/tacotron2-DDC'
# Init TTS
tts = TTS(model_name)

# Create a recognizer object
r = sr.Recognizer()

# Prompt the user to speak
print("Please speak now...")
with sr.Microphone() as source:
    audio = r.listen(source, timeout=10)
print("Processing...")

try:
    # Convert speech to text
    text = r.recognize_google(audio)

except sr.UnknownValueError:
    text = "Sorry, I wasn't able to understand that."
    
if text == "Sorry, I wasn't able to understand that.":
    tts.tts_to_file(text, file_path='output.wav')
    playsound('output.wav')
    exit()
else:
    print("test")
    exit()        
