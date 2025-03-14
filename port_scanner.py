import socket

def port_scanner(target, ports):
    print(f"\n[+] Scanning {target}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            print(f"[-] Port {port} is CLOSED")
        sock.close()

if __name__ == "__main__":
    target = input("Enter target IP: ")
    ports = range(20, 1025)  # Scanning ports from 20 to 1024
    port_scanner(target, ports)
