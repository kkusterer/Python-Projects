import requests
import re

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
