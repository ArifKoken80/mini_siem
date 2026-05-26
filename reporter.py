import json
from collections import defaultdict
from datetime import datetime


class Reporter:

    def __init__(self):

        self.events = []

        # IP risk score
        self.ip_scores = defaultdict(int)

        # Hangi IP hangi servislere saldırdı
        self.ip_services = defaultdict(set)

    # Risk puanı hesaplama
    def calculate_score(self, message):

        message = message.lower()

        if "sql injection" in message:
            return 40

        elif "brute force" in message:
            return 30

        elif "exploit" in message:
            return 50

        elif "failed" in message:
            return 10

        return 0

    # Severity belirleme
    def get_severity(self, score):

        if score >= 80:
            return "HIGH"

        elif score >= 40:
            return "MEDIUM"

        return "LOW"

    # Event ekleme
    def add_event(self, ip, service, message):

        score = self.calculate_score(message)

        self.ip_scores[ip] += score

        self.ip_services[ip].add(service)

        severity = self.get_severity(self.ip_scores[ip])

        event = {

            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            "ip": ip,

            "service": service,

            "message": message,

            "risk_score": self.ip_scores[ip],

            "severity": severity
        }

        self.events.append(event)

    # Risk raporu
    def print_risk_report(self):

        print("\n" + "=" * 60)
        print("🚨 RISK ANALYSIS REPORT")
        print("=" * 60)

        for ip, score in self.ip_scores.items():

            severity = self.get_severity(score)

            services = ", ".join(self.ip_services[ip])

            print(f"\n🌐 IP: {ip}")
            print(f"🎯 Targeted Services: {services}")
            print(f"📊 Risk Score: {score}")
            print(f"⚠ Threat Level: {severity}")

    # Top attackers
    def print_top_attackers(self):

        print("\n" + "=" * 40)
        print("🔥 TOP ATTACKERS")
        print("=" * 40)

        sorted_attackers = sorted(
            self.ip_scores.items(),
            key=lambda x: x[1],
            reverse=True
        )

        for index, (ip, score) in enumerate(sorted_attackers, start=1):

            severity = self.get_severity(score)

            print(f"\n{index}. {ip}")
            print(f"   Risk Score: {score}")
            print(f"   Threat Level: {severity}")

    # JSON export
    def export_json(self, filename="report.json"):

        with open(filename, "w") as f:
            json.dump(self.events, f, indent=4)

        print(f"\n[+] JSON exported: {filename}")