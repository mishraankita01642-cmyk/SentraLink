from flask import Flask, render_template, request
import re
from urllib.parse import urlparse

app = Flask(__name__)

SUSPICIOUS_KEYWORDS = [
    "login", "verify", "update", "bank", "secure",
    "account", "free", "bonus", "paypal", "signin"
]

def analyze_url(url):
    score = 0
    reasons = []

    if len(url) > 75:
        score += 1
        reasons.append("URL is too long")

    if "@" in url:
        score += 2
        reasons.append("Contains '@' symbol")

    if url.count("-") > 3:
        score += 1
        reasons.append("Too many hyphens")

    for word in SUSPICIOUS_KEYWORDS:
        if word in url.lower():
            score += 1
            reasons.append(f"Contains suspicious word: {word}")

    parsed = urlparse(url)
    if re.match(r"^\d+\.\d+\.\d+\.\d+$", parsed.netloc):
        score += 2
        reasons.append("Uses IP address instead of domain")

    if score >= 3:
        return "Suspicious", reasons
    else:
        return "Safe", reasons


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    reasons = []
    url = ""

    if request.method == "POST":
        url = request.form["url"]
        result, reasons = analyze_url(url)

    return render_template("index.html", result=result, reasons=reasons, url=url)


if __name__ == "__main__":
    app.run(debug=True)