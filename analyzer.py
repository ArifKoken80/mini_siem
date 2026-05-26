def parse_log(line):
    parts = line.strip().split(" - ")

    if len(parts) == 3:
        ip = parts[0]
        service = parts[1]
        message = parts[2]

        return ip, service, message

    return None, None, None