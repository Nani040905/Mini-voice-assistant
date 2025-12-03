# speaker.py

import pyttsx3

# Initialize the TTS engine once
engine = pyttsx3.init('sapi5') 

def speak(audio):
    """
    Function to make the assistant speak the given audio string.
    Returns the audio string for logging.
    """
    print(f"Assistant: {audio}")
    engine.say(audio)
    engine.runAndWait()
    return audio