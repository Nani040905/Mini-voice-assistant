# listener.py

import speech_recognition as sr
from speaker import speak

def take_command():
    """
    Listens to the microphone input and returns the recognized text string.
    """
    # Initialize the Recognizer
    r = sr.Recognizer()

    # Use PyAudio via sr.Microphone()
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust recognizer settings
        r.pause_threshold = 1 
        r.energy_threshold = 300 
        
        try:
            # Adjusts for ambient noise to set an appropriate threshold
            r.adjust_for_ambient_noise(source, duration=0.5) 
            audio = r.listen(source)

        except sr.WaitTimeoutError:
             print("No speech detected within the time limit.")
             return "none"
        
    try:
        print("Recognizing...")    
        # Use Google's speech recognition service
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}\n")

    except Exception:
        # This catches errors like silence or poor audio quality
        speak("Sorry, I didn't quite catch that. Could you say that again?")  
        return "none"
    
    return query.lower()