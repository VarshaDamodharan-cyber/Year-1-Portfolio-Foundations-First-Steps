import socket

def port_scanner(host, ports):
    print(f"Scanning {host}...")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            s.connect((host, port))
            print(f"Port {port} is OPEN ✅")
        except:
            pass
        s.close()

target = input("Enter host (e.g., scanme.nmap.org): ")
common_ports = [21, 22, 23, 25, 53, 80, 110, 443]
port_scanner(target, common_ports)
