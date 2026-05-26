from flask import Flask, render_template_string
import json

app = Flask(__name__)


def load_data():
    try:
        with open("report.json", "r") as f:
            return json.load(f)
    except:
        return []


@app.route("/")
def home():

    data = load_data()

    # ---------------- METRICS ----------------
    total_events = len(data)
    unique_ips = len(set(d["ip"] for d in data))
    high_risk = len([d for d in data if d["severity"] == "HIGH"])

    # ---------------- TOP ATTACKERS ----------------
    scores = {}

    for d in data:
        ip = d["ip"]
        scores[ip] = scores.get(ip, 0) + d["risk_score"]

    top_attackers = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    labels = [x[0] for x in top_attackers]
    values = [x[1] for x in top_attackers]

    # ---------------- SEVERITY ----------------
    severity_count = {
        "LOW": len([d for d in data if d["severity"] == "LOW"]),
        "MEDIUM": len([d for d in data if d["severity"] == "MEDIUM"]),
        "HIGH": len([d for d in data if d["severity"] == "HIGH"])
    }

    html = """
    <html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

        <style>
            body {
                font-family: Arial;
                background: #0b1220;
                color: white;
                padding: 25px;
            }

            h1 {
                font-size: 28px;
                margin-bottom: 20px;
            }

            .grid {
                display: flex;
                gap: 15px;
                margin-bottom: 20px;
            }

            .card {
                background: #1e293b;
                padding: 15px;
                border-radius: 10px;
                flex: 1;
                text-align: center;
            }

            .chart-box {
                background: #111827;
                padding: 18px;
                margin-top: 20px;
                border-radius: 10px;
            }

            canvas {
                max-width: 100%;
                height: 280px !important;
            }

            .desc {
                color: #94a3b8;
                margin-bottom: 8px;
                font-size: 13px;
                line-height: 1.6;
            }

            hr {
                border: none;
                border-top: 1px solid #334155;
                margin: 15px 0;
            }

        </style>
    </head>

    <body>

    <h1>🛡 SOC SECURITY ANALYTICS DASHBOARD</h1>

    <!-- METRICS -->
    <div class="grid">
        <div class="card">📊 Total Events<br><h2>{{total}}</h2></div>
        <div class="card">🌐 Unique IPs<br><h2>{{ips}}</h2></div>
        <div class="card">🚨 High Risk<br><h2>{{high}}</h2></div>
    </div>

    <!-- PIE CHART -->
    <div class="chart-box">
        <h3>📈 Attack Severity Distribution</h3>
        <div class="desc">
            LOW / MEDIUM / HIGH saldırı yoğunluk dağılımı
        </div>

        <canvas id="pie"></canvas>
    </div>

    <!-- BAR CHART -->
    <div class="chart-box">
        <h3>🔥 Top Attackers by Risk Score</h3>
        <div class="desc">
            En yüksek risk skoruna sahip IP adresleri
        </div>

        <canvas id="bar"></canvas>
    </div>

    <!-- INSIGHT PANEL -->
    <div class="chart-box">
        <h3>🧠 SOC Advanced Analysis Engine</h3>

        <div class="desc">

            {% if high > 0 %}
            🚨 <b>CRITICAL SECURITY ALERT</b><br>
            Multiple high-severity attack patterns detected.<br>
            Immediate investigation required on top attacker IPs.<br><br>
            {% endif %}

            {% if medium > 2 %}
            ⚠️ <b>BEHAVIORAL ANOMALY WARNING</b><br>
            Elevated medium-risk activity suggests reconnaissance or brute-force scanning.<br><br>
            {% endif %}

            {% if medium > 0 and high == 0 %}
            🟡 <b>SUSPICIOUS ACTIVITY DETECTED</b><br>
            Early-stage probing behavior detected across network services.<br><br>
            {% endif %}

            {% if high == 0 and medium == 0 %}
            🟢 <b>NORMAL SECURITY STATE</b><br>
            No significant threats detected in current dataset.<br><br>
            {% endif %}

            <hr>

            📊 <b>Threat Intelligence Summary</b><br><br>

            • Total Events: <b>{{total}}</b><br>
            • Unique Attack Sources: <b>{{ips}}</b><br>
            • High Risk Events: <b>{{high}}</b><br>
            • Medium Risk Events: <b>{{medium}}</b><br>
            • Attack Activity Ratio: <b>{{ ((high + medium) / total * 100) if total > 0 else 0 }}%</b><br><br>

            🧬 <b>Security Interpretation:</b><br>

            {% if high > medium %}
            The system is under <b>exploit-level attack activity</b> (active compromise attempts).
            {% elif medium > high %}
            The system shows <b>reconnaissance behavior</b> (scanning / probing activity).
            {% else %}
            No dominant attack pattern detected.
            {% endif %}

        </div>
    </div>

    <script>

    // PIE CHART
    new Chart(document.getElementById('pie'), {
        type: 'pie',
        data: {
            labels: ['LOW','MEDIUM','HIGH'],
            datasets: [{
                data: [{{low}}, {{medium}}, {{high}}],
                backgroundColor: [
                    '#22c55e',
                    '#f59e0b',
                    '#ef4444'
                ]
            }]
        }
    });

    // BAR CHART
    new Chart(document.getElementById('bar'), {
        type: 'bar',
        data: {
            labels: {{ labels | tojson }},
            datasets: [{
                label: 'Risk Score',
                data: {{ values | tojson }},
                backgroundColor: '#ef4444'
            }]
        },
        options: {
            scales: {
                x: { ticks: { color: 'white' } },
                y: { ticks: { color: 'white' } }
            }
        }
    });

    </script>

    </body>
    </html>
    """

    return render_template_string(
        html,
        total=total_events,
        ips=unique_ips,
        high=high_risk,
        low=severity_count["LOW"],
        medium=severity_count["MEDIUM"],
        labels=labels,
        values=values,

    )


if __name__ == "__main__":
    app.run(debug=True)