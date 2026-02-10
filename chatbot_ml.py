import json
import pickle
import numpy as np

# Load trained ML model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Load vectorizer
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Load intents (UTF-8 FIX)
with open("intents.json", "r", encoding="utf-8") as file:
    intents = json.load(file)

def chatbot_response(user_input):
    input_vector = vectorizer.transform([user_input])
    predicted_tag = model.predict(input_vector)[0]

    for intent in intents["intents"]:
        if intent["tag"] == predicted_tag:
            return np.random.choice(intent["responses"])

    return "Sorry, I didn't understand that."
