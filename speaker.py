# speaker.py

import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init('sapi5') 

def speak(audio):
    """
    Function to make the assistant speak the given audio string.
    Returns the audio string.
    """
    print(f"Assistant: {audio}")
    engine.say(audio)
    engine.runAndWait()
    return audio 

if __name__ == '__main__':
    speak("Hello, I am your Mini Jarvis assistant.")