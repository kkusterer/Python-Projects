import requests
import re
url = 'https://www.svsu.edu/about/offices/'

response = requests.get(url)
           
emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', response.text)

if emails:
    print("Found emails:")
    for email in set(emails):
        print(email)
else:
    print("No emails found.")

