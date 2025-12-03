# speaker.py

import pyttsx3

def speak(audio):
    """
    Function to make the assistant speak the given audio string by 
    (re)initializing the engine for each call to ensure reliability.
    Returns the audio string for logging.
    """
    try:
        # Initialize the TTS engine for the current speech
        # Using 'sapi5' for Windows, but it defaults if not specified
        engine = pyttsx3.init('sapi5') 

        print(f"Assistant: {audio}")
        
        # Queue the audio text
        engine.say(audio)
        
        # Run the speech and wait for it to complete
        engine.runAndWait()
        
        # Crucial step: Stops the current utterance and clears the event queue.
        # This prevents the hang-up in subsequent calls.
        engine.stop() 
        
    except Exception as e:
        print(f"Error during TTS: {e}")
        
    return audio 

if __name__ == '__main__':
    # Example usage:
    print("Testing multi-line speech...")
    speak("This is the first sentence. It should speak correctly.")
    speak("This is the second sentence. It should not hang.")
    print("Test complete.")