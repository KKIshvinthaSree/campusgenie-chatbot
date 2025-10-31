from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "").lower()
    genie_responses = {
        "admission": "✨ Admissions are open! Apply online or visit our campus helpdesk.",
        "clubs": "🎭 We have tech clubs, drama, music, and even a robotics guild!",
        "hostel": "🏠 Hostels are cozy and secure, with 24/7 Wi-Fi and mess facilities.",
        "library": "📚 Our library is open till 10 PM and offers digital access too."
    }
    reply = genie_responses.get(user_input, "Hmm... I’m not sure about that. Try asking about 'admission', 'clubs', 'hostel', or 'library'.")
    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)