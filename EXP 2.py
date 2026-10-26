import socket

target = "127.0.0.1"

# Common ports and their services
ports = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL"
}

print("Target Host:", target)
print("Starting Port Scan...\n")

for port, service in ports.items():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} ({service}): OPEN")
    else:
        print(f"Port {port} ({service}): CLOSED or FILTERED")

    sock.close()

print("\nPort scan completed.")