import requests
import re
import time
import os

def email_scrape(entered_url):

    url = 'entered_url'

    response = requests.get(url)
            
    emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', response.text)

    if emails:
        print("Found emails:")
        for email in set(emails):
            print(email)
    else:
        print("No emails found.")

def request(entered_url):
    x = requests.get(entered_url)
    print(x.text)

def character(word):
    for i in word:
        print(i)

def menu_1(title, option_1):
    print(f"\n   ---- {title.upper()} ----")
    print("******************************")
    print(f"   1. {option_1}")
    print("******************************")

def menu_2(title, option_1, option_2):
    print(f"\n   ---- {title.upper()} ----")
    print("******************************")
    print(f"   1. {option_1}")
    print(f"   2. {option_2}")
    print("******************************")


def menu_3(title, option_1, option_2, option_3):
    print(f"\n   ---- {title.upper()} ----")
    print("******************************")
    print(f"   1. {option_1}")
    print(f"   2. {option_2}")
    print(f"   3. {option_3}")
    print("******************************")


def menu_4(title, option_1, option_2, option_3, option_4):
    print(f"\n   ---- {title.upper()} ----")
    print("******************************")
    print(f"   1. {option_1}")
    print(f"   2. {option_2}")
    print(f"   3. {option_3}")
    print(f"   4. {option_4}")
    print("******************************")

def menu_5(title, option_1, option_2, option_3, option_4, option_5):
    print(f"\n   ---- {title.upper()} ----")
    print("******************************")
    print(f"   1. {option_1}")
    print(f"   2. {option_2}")
    print(f"   3. {option_3}")
    print(f"   4. {option_4}")
    print(f"   5. {option_5}")
    print("******************************")

def show_menu_6(title, option_1, option_2, option_3, option_4, option_5, option_6 ):
    print(f"\n   ---- {title.upper()} ----")
    print("******************************")
    print(f"   1. {option_1}")
    print(f"   2. {option_2}")
    print(f"   3. {option_3}")
    print(f"   4. {option_4}")
    print(f"   5. {option_5}")
    print(f"   6. {option_6}")
    print("******************************")

def get_int(prompt):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("** Please enter a number: ")
        else:
            return number


def get_positive_int(prompt):
    while True:
        number = get_int(prompt)

        if number < 0:
            print("\n** Usage error. Number must be positive.\n")
            pause_and_clear(3)

        else:
            return number


def get_float(prompt):
    while True:
        try:
            number = float(input(prompt))
        except ValueError:
            print("** Please enter a number: ")
        else:
            return number


def get_positive_float(prompt):
    while True:
        number = get_float(prompt)

        if number < 0:
            print("\n** Usage error. Please enter a positive number.\n")
            pause_and_clear(3)

        else:
            return number


def get_name():
    return input("\nWhat is your name? ")


def pause_and_clear(seconds_to_wait):
    
    time.sleep(seconds_to_wait)
    os.system('clear')

def clear():
    os.system('clear')


