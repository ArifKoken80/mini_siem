# 🛡 Mini SIEM / SOC Log Analysis System

This project is a Python-based lightweight Security Information and Event Management (SIEM) simulation system.

It analyzes system logs, detects suspicious activities, calculates risk scores, and visualizes security insights through a Flask-based SOC dashboard.

---

## 🚀 Features

- 🔍 Log parsing and structured analysis
- ⚠️ Threat detection (brute force, SQL injection, exploit attempts)
- 📊 Risk scoring system per IP
- 🚨 Severity classification (LOW / MEDIUM / HIGH)
- 🔥 Top attacker ranking system
- 📈 Interactive SOC dashboard (Flask + Chart.js)
- 🧠 Advanced security insight engine
- 📄 JSON report export (report.json)

---

## 🧠 How It Works

1. Logs are read from `logs/sample.log`
2. Each line is parsed into:
   - IP address
   - Service
   - Message
3. Detector analyzes suspicious behavior
4. Reporter calculates:
   - Risk score per IP
   - Severity level
   - Aggregated statistics
5. Results are saved into `report.json`
6. Flask dashboard visualizes everything in a SOC-style panel

---

## 📊 Dashboard Includes

- 📈 Attack severity distribution (Pie Chart)
- 🔥 Top attacker IP ranking (Bar Chart)
- 🧠 SOC intelligence insight panel
- 📊 System summary metrics

---

## 🛠 Technologies Used

- Python 3
- Flask
- Chart.js
- JSON
- Collections (defaultdict)
- HTML/CSS (dark SOC theme)

---


## 📂 Project Structure

```text
mini-siem/
│
├── analyzer.py
├── detector.py
├── reporter.py
├── main.py
├── dashboard.py
├── logs/
│   └── sample.log
└── report.json
```


---

## 🚀 How to Run

### Step 1 - Run log analyzer
```bash
python main.py
```
Step 2 - Start dashboard
```bash
python dashboard.py
```
Then open in browser:
http://127.0.0.1:5000

📌 Purpose
This project simulates a simplified SOC (Security Operations Center) system.
It demonstrates:
Log monitoring
Threat detection
Risk scoring
Security visualization
It is inspired by real-world SIEM tools like Splunk and ELK Stack.

👨‍💻 Author
Arif Köken