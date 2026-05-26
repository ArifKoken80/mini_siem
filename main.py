from analyzer import parse_log
from detector import detect
from reporter import Reporter

LOG_FILE = "logs/sample.log"


def main():

    reporter = Reporter()

    print("[*] ADVANCED SIEM ANALYZER STARTED\n")

    with open(LOG_FILE, "r") as file:

        for line in file:

            ip, service, message = parse_log(line)

            if ip:
                detect(ip, service, message, reporter)

    # RAPORLAR
    reporter.print_risk_report()

    reporter.print_top_attackers()

    reporter.export_json()


if __name__ == "__main__":
    main()