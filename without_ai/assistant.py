# assistant.py

import datetime
import webbrowser
import wikipedia
from speaker import speak
from listener import take_command
from database import log_command, HISTORY_COLLECTION

def process_command(query):
    """
    Processes the user's command, executes the action, and returns the 
    assistant's final spoken output and stop signal.
    """
    output_text = ""
    stop_signal = False

    # 1. Open Websites
    if 'open youtube' in query:
        output_text = "Opening YouTube."
        webbrowser.open("https://www.youtube.com")
        
    elif 'open google' in query:
        output_text = "Opening Google."
        webbrowser.open("https://www.google.com")

    # 2. Tell Time
    elif 'the time' in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        output_text = f"Sir, the current time is {current_time}"

    # 3. Answer Questions (using Wikipedia)
    elif 'wikipedia' in query:
        try:
            # We speak "Searching Wikipedia" separately, but only the final result is logged
            speak('Searching Wikipedia...') 
            search_query = query.replace("wikipedia", "").strip() 
            results = wikipedia.summary(search_query, sentences=2, auto_suggest=False)
            
            output_text = f"According to Wikipedia: {results}"
            
        except wikipedia.exceptions.PageError:
            output_text = f"Sorry, I couldn't find a Wikipedia page for {search_query}"
        except wikipedia.exceptions.DisambiguationError as e:
            output_text = f"I found a few options. Could you be more specific about: {e.options[:3]}?"
        
    # 4. Exit/Stop Command
    elif 'stop' in query or 'exit' in query or 'bye' in query:
        output_text = "Goodbye, Sir. Have a great day!"
        stop_signal = True
    
    # 5. Default/Unrecognized Command
    else:
        output_text = "I'm not programmed to do that yet. Try asking me the time, or to open a website."
    
    # Speak the final determined response and capture the text for logging
    final_response = speak(output_text) 
    
    return final_response, stop_signal

def main():
    """
    The main execution function for the AI Voice Assistant.
    """
    
    speak("Initializing Mini Jarvis...")
    
    # Greeting based on time of day
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
        
    speak("I am ready. Please tell me what to do.")

    while True:
        user_command = take_command()
        
        if user_command != "none":
            # Process the command, get the response and the stop signal
            assistant_response, stop_program = process_command(user_command)
            
            # LOG THE HISTORY TO MONGODB
            log_command(user_command, assistant_response, HISTORY_COLLECTION)
            
            if stop_program:
                break

if __name__ == "__main__":
    main()