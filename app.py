from flask import Flask, request, render_template, jsonify
from textblob import TextBlob

app = Flask(__name__)


# Sentiment analysis function
def analyze_sentiment(text):
    sentiment_score = TextBlob(text).sentiment.polarity
    if sentiment_score > 0:
        return "Happy 😀"
    elif sentiment_score < 0:
        return "Sad 😢"
    else:
        return "Neutral 😐"


# Homepage route (for rendering the web form)
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form["text"]
        result = analyze_sentiment(text)  # Use our function
        return render_template("index.html", result=result)
    return render_template("index.html", result="")


# API route for JSON requests
@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400  # Error if no text

    text = data["text"]
    sentiment = analyze_sentiment(text)  # Use our function

    return jsonify({"sentiment": sentiment})  # Return JSON response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)  # Running with debug mode

