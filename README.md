# SentraLink  🔗

A simple **Python + Flask** web app that checks whether a URL looks *safe* or *suspicious* using basic, rule‑based analysis.  
The goal is to teach safe browsing habits and introduce beginners to URL analysis concepts like length, symbols, and phishing‑related keywords.[web:14][web:32]

## ✨ Features

- Web form where users paste any URL.
- Validates URL format before analysis.
- Checks simple lexical features:
  - URL length (short vs very long).
  - Number of special characters (`@`, `?`, `%`, `=`, `&`, `$`).
  - Suspicious keywords such as `login`, `verify`, `update`, `free`, `win`, `bank`, etc.
  - Use of IP address instead of a domain.
  - Hyphens and look‑alike characters in the domain (e.g. `paypa1.com`).
- Calculates a simple risk score and labels the URL as **Safe** or **Suspicious**.
- Shows human‑readable reasons so users can learn what made the URL suspicious.


## 🚀 Getting Started (Local Setup)

### 1. Clone the repository


git clone https://github.com/<your-username>/url-safety-checker.git
cd url-safety-checker

### 2. Create and activate a virtual environment (Windows)
python -m venv venv
venv\Scripts\activate
Virtual environments help keep project dependencies isolated
3. Install dependencies
pip install -r requirements.txt
If you don’t have a requirements.txt yet, you can create one like:


flask
validators
and then run the install command.
4. Run the development server
Option 1 – simple:
python app.py
Option 2 – using flask run:
set FLASK_APP=app.py
set FLASK_ENV=development
flask run

Open the shown URL in your browser :
🔍 How the URL Analysis Works
Input: User submits a URL through the web form.

Validation: App checks if the string is a valid URL using validators.url. Invalid URLs are immediately marked suspicious with an explanation.[web:16]

Feature Extraction:

Full URL string

Domain (host) and path[web:34]

Rule‑based Checks:

Length thresholds (e.g. >54 chars, >80 chars).[web:34]

Count of special characters (@, ?, %, =, &, $).[web:35]

Whether the domain looks like an IP address.[web:30]

Occurrence of suspicious keywords in domain or path.[web:4][web:32]

Hyphens and look‑alike character patterns in domain.[web:33][web:35]

Scoring: Each suspicious sign adds to a risk score, inspired by common phishing‑URL feature engineering.[web:32][web:70]

Decision:

Score ≥ threshold → Suspicious

Score < threshold → Safe

Output: Flask renders a result page showing the label and a list of reasons so the user understands the decision.[web:32]










