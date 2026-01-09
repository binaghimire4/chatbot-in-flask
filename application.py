from flask import Flask, render_template, request
app = Flask(__name__, template_folder="templates")

FAQ = {
    "covid symptoms": "Common symptoms: fever, cough, fatigue, loss of taste/smell.",
    "prevent covid": "Mask, hand hygiene, ventilation, and vaccination.",
    "diabetes": "A condition where the body has trouble regulating blood sugar.",
    "healthy bp": "About 120/80 mmHg is considered normal for most adults.",
    "fever": "Temperature above ~100.4°F (38°C).",
    "reduce fever": "Rest, fluids, and acetaminophen/paracetamol as directed."
}

def get_answer(q: str) -> str:
    q = (q or "").lower().strip()
    for k, v in FAQ.items():
        if k in q:
            return v
    return "Sorry, I don’t have an answer to that. Please consult a healthcare professional."

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    user_question = ""
    if request.method == "POST":
        user_question = request.form.get("question", "")
        answer = get_answer(user_question)
    return render_template("index.html", question=user_question, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
