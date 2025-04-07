import streamlit as st
import pickle
from nltk.stem.porter import PorterStemmer
import re
import random

intents = pickle.load(open('Training_data.pkl','rb'))
lr = pickle.load(open('model.pkl','rb'))
vector = pickle.load(open('Vector_data.pkl','rb'))

port_stem = PorterStemmer()
def noise_cleaning(noise):
    te = noise.lower()
    te = te.split()
    te = [port_stem.stem(word) for word in te]
    te = ' '.join(te)
    #te = re.sub('[^a-zA-Z]',' ',te)
    return te

def chatbot(text):
    text=noise_cleaning(text)
    text=vector.transform([text])
    predict=lr.predict(text)
    for i in intents:
        if i['tag'] == predict[0]:
            return random.choice(i['responses'])

st.title('SamGPT')
st.write('This is a simple web app that uses a machine learning model to Provide Chat Support')

messages = st.container(height=400)
messages.chat_message("assistant").write("Model: Enter any news to detect wether it is Fake or Not")
if prompt := st.chat_input("Say something"):
    messages.chat_message("user").write(f"User: {prompt}")
    news=chatbot(prompt)
    messages.chat_message("assistant").write(f"Model: {news}")

st.caption('Made by Shaniyaz')

