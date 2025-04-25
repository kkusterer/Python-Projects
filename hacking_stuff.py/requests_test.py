# pip install requests to run if not installed already also do not name the file "requests.py" 
# it will resault in an error.
import requests

x = requests.get('https://www.google.com/?safe=active&ssui=on')

print(x.text)