# ChatBot

# Simple Machine Learning Chatbot

This is a simple chatbot built using machine learning techniques. It uses a basic intent classification model to understand user queries and respond accordingly. Great for beginners looking to explore NLP, machine learning, and chatbot development.

## Features

- Intent classification using ML
- Easy-to-edit intent dataset (`intents.json`)
- Predefined responses for each intent
- Simple and clean Python implementation
- Lightweight and easy to customize

## Tech Stack

- **Python 3.x**
- **scikit-learn** (or TensorFlow / PyTorch)
- **NLTK** for preprocessing
- Optionally: **Flask** for a web interface

## How It Works

1. The chatbot is trained on a dataset of intents.
2. When a user types a message, the model predicts the intent.
3. Based on the predicted intent, a suitable response is returned.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/Anonymous7722/ChatBot
    cd ChatBot
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the chatbot:
    ```bash
    python3 -m streamlit run app.py
    ```

## Dataset

The chatbot uses an `intents.json` with labeled data like this:

```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hi", "Hello", "Hey"],
      "responses": ["Hello!", "Hi there!", "Hey!"]
    },
  ]
}
