# 🧠 Minds DB Chatbot

A simple CLI chatbot that uses the 'mistral-7b' model to chat with users.

## 📋 Requirements

- 🛠️ **MindsDB** setup on your PC: [MindsDB Setup Guide](https://docs.mindsdb.com/setup/self-hosted/docker-desktop)
- 🐍 **Python** installed on your PC
- 🔑 **API Key**: Get your API key from [MindsDB](https://mdb.ai/)

## 🚀 Steps to Run

1. **Clone this repository:**

   ```bash
   git clone https://github.com/kom-senapati/minds_db_chatbot
   ```

2. **Navigate to the project directory:**

   ```bash
   cd minds_db_chatbot
   ```

3. **Create a `.env` file and fill it following the example of `.env.example`.**

4. **Create a Python environment using `venv` named `.venv`:**

   ```bash
   python -m venv .venv
   ```

5. **Activate the virtual environment:**

   - On **Windows**:

     ```bash
     .venv\Scripts\activate
     ```

   - On **macOS/Linux**:

     ```bash
     source .venv/bin/activate
     ```

6. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

7. **Run the setup script (ensure MindsDB is running):**

   ```bash
   python setup.py
   ```

8. **Run the main script to start chatting with the chatbot:**

   ```bash
   python main.py
   ```

Now, you're all set to chat with your MindsDB chatbot! 💬✨

## 📞 Contact the Author

- **GitHub:** [kom-senapati](https://github.com/kom-senapati)
- **X:** [@kom_senapati](https://X.com/kom_senapati)
