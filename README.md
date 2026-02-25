# SentraLink  🔗

A simple **Python + Flask** web app that checks whether a URL looks *safe* or *suspicious* using basic, rule‑based analysis.  
The goal is to teach safe browsing habits and introduce beginners to URL analysis concepts like length, symbols, and phishing‑related keywords.

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


## 🚀 Getting Started 
### 1. Open the shown URL in your browser :  https://sentralink.onrender.com/


🔍 How the URL Analysis Works
1. Input: User submits a URL through the web form.

2. Validation: App checks if the string is a valid URL using validators.url. Invalid URLs are immediately marked suspicious with an explanation.

3. Feature Extraction:
  Full URL string
  Domain (host) and path

4. Rule‑based Checks:
  Length thresholds (e.g. >54 chars, >80 chars).
  Count of special characters (@, ?, %, =, &, $).
  Whether the domain looks like an IP address.
  Occurrence of suspicious keywords in domain or path.
  Hyphens and look‑alike character patterns in domain.

5. Scoring: Each suspicious sign adds to a risk score, inspired by common phishing‑URL feature engineering.

6. Decision:
  Score ≥ threshold → Suspicious
  Score < threshold → Safe

7. Output: Flask renders a result page showing the label and a list of reasons so the user understands the decision.










