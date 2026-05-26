from colorama import Fore, init

init(autoreset=True)

def detect(ip, service, message, reporter):

    # Event'i reporter'a gönder
    reporter.add_event(ip, service, message)

    # Güncel risk score
    score = reporter.ip_scores[ip]

    # Severity hesapla
    severity = reporter.get_severity(score)

    # Terminal output
    if severity == "HIGH":
        print(Fore.RED + f"[HIGH] {ip} attacking {service}")

    elif severity == "MEDIUM":
        print(Fore.YELLOW + f"[MEDIUM] Suspicious activity from {ip}")

    else:
        print(Fore.GREEN + f"[LOW] {ip} event detected")