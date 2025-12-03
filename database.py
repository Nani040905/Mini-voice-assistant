# database.py

from pymongo import MongoClient
import datetime

# --- Configuration ---
# !!! IMPORTANT: Replace this connection string with your actual MongoDB URI !!!
MONGO_URI = "mongodb://localhost:27017/" 
DATABASE_NAME = "mini_jarvis_db"
COLLECTION_NAME = "command_history"
# ---------------------

def init_db():
    """Initializes the MongoDB client and returns the history collection."""
    try:
        client = MongoClient(MONGO_URI)
        # The following line will raise an exception if the server is unreachable
        client.admin.command('ping') 
        db = client[DATABASE_NAME]
        history_collection = db[COLLECTION_NAME]
        print("MongoDB connection successful.")
        return history_collection
    except Exception as e:
        print(f"Error connecting to MongoDB. History logging disabled. Details: {e}")
        return None

def log_command(user_input, assistant_output, collection):
    """
    Logs the command and response to the specified MongoDB collection.
    """
    if collection is None:
        return

    history_record = {
        "timestamp": datetime.datetime.now(),
        "user_command": user_input,
        "assistant_response": assistant_output,
        "success": True if assistant_output not in ["I'm not programmed to do that yet. Try asking me the time, or to open a website.", "Sorry, I didn't quite catch that. Could you say that again?", "Unrecognized command."] else False
    }

    try:
        collection.insert_one(history_record)
    except Exception as e:
        print(f"Error inserting record into MongoDB: {e}")

# Initialize the collection object upon import
HISTORY_COLLECTION = init_db()