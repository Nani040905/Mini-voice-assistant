# listener.py

import speech_recognition as sr
from speaker import speak

def take_command():
    """
    Listens to the microphone input and returns the recognized text string.
    """
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        r.energy_threshold = 300 
        
        try:
            r.adjust_for_ambient_noise(source, duration=0.5) 
            audio = r.listen(source)

        except sr.WaitTimeoutError:
             print("No speech detected within the time limit.")
             return "none"
        
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}\n")

    except Exception:
        speak("Sorry, I didn't quite catch that. Could you say that again?")  
        return "none"
    
    return query.lower()

if __name__ == '__main__':
    speak("Please say something.")
    command = take_command()
    if command != "none":
        speak(f"You said: {command}")