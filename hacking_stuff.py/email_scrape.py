import requests
import re

# The contact page of the university
url = 'https://www.svsu.edu/about/offices/'

# Send a GET request to the page
response = requests.get(url)

# Find emails using regex             
emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', response.text)

# Print out the found emails
if emails:
    print("Found emails:")
    for email in set(emails):
        print(email)
else:
    print("No emails found.")

