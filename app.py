from flask import Flask, request, jsonify, render_template
from chatbot_ml import chatbot_response

app = Flask(__name__,template_folder='template')

# Home page (Frontend)
@app.route("/")
def home():
    return render_template("index.html")

# Chat API
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    bot_reply = chatbot_response(user_message)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
