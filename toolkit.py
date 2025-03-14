from port_scanner import port_scanner
from brute_forcer import brute_force

def main():
    print("\n=== Penetration Testing Toolkit ===")
    print("1. Port Scanner")
    print("2. Brute-Force Attack")
    
    choice = input("\nChoose an option: ")
    
    if choice == "1":
        target = input("\nEnter target IP: ")
        ports = range(20, 1025)
        port_scanner(target, ports)
    elif choice == "2":
        target_url = input("\nEnter target URL: ")
        username = input("Enter username: ")
        password_file = input("Enter path to password list: ")
        brute_force(target_url, username, password_file)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
