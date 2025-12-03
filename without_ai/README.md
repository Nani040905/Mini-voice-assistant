# 🤖 Mini Jarvis: AI Voice Assistant

Mini Jarvis is a modular Python-based voice assistant that can execute commands, retrieve information, and log all interaction history to a MongoDB database.

## ✨ Features

* **Voice Control:** Uses microphone input for commands.
* **Text-to-Speech:** Responds using a synthetic voice.
* **Web Automation:** Can open specified websites (Google, YouTube).
* **Information Retrieval:** Uses Wikipedia to answer general knowledge questions.
* **Time Inquiry:** Reports the current time.
* **Database Logging:** Stores all user commands and assistant responses in MongoDB.

## 🛠️ Requirements

1.  **Python 3.x**
2.  **A working microphone**
3.  **A running MongoDB instance** (local or cloud)

## 📦 Installation & Setup

1.  **Clone the Repository (if applicable) or create the folder structure.**

2.  **Install Python Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure MongoDB:**
    * Ensure your MongoDB server is running.
    * Open `database.py` and **update the `MONGO_URI`** with your specific connection string (e.g., if running on a different port or using authentication).

    ```python
    # Inside database.py
    MONGO_URI = "mongodb://localhost:27017/" 
    DATABASE_NAME = "mini_jarvis_db"
    ```

## ▶️ How to Run

1.  Navigate to the project directory in your terminal.
2.  Execute the main application file:
    ```bash
    python assistant.py
    ```
3.  The assistant will greet you. When you see **"Listening..."**, speak your command clearly.

## 🗣️ Supported Commands

| Category | Example Command | Notes |
| :--- | :--- | :--- |
| **Web** | "Open Google" | Opens the specified URL in your default browser. |
| **Info** | "Wikipedia, what is quantum physics" | Fetches and speaks the summary from Wikipedia. |
| **Time** | "What is the time" | Reports the current local time. |
| **Control** | "Stop" / "Exit" / "Bye" | Terminates the assistant program. |