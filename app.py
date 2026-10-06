from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

questions = [
    "Tell me about yourself.",
    "What are your strengths and weaknesses?",
    "Why should we hire you?",
    "Tell me about your academic project.",
    "Where do you see yourself in 5 years?"
]


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/style.css")
def css():
    return send_from_directory(".", "style.css")


@app.route("/get_question/<int:number>")
def get_question(number):

    if number < len(questions):
        return jsonify({
            "question": questions[number],
            "number": number + 1
        })

    return jsonify({
        "question": "Interview completed!",
        "number": len(questions)
    })


@app.route("/evaluate", methods=["POST"])
def evaluate():

    data = request.get_json()
    answer = data.get("answer", "").strip()

    if not answer:
        return jsonify({
            "score": 0,
            "feedback": "Please enter an answer."
        })

    words = len(answer.split())

    if words < 10:
        score = 5
        feedback = "Your answer is too short. Try adding more details."

    elif words < 30:
        score = 7
        feedback = "Good answer. Try adding a specific example."

    else:
        score = 9
        feedback = "Excellent answer! Your response is detailed and clear."

    return jsonify({
        "score": score,
        "feedback": feedback
    })


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False,
        use_reloader=False
    )