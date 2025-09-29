import time, os

def pac(text, delay=0.3):
    print(text)
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')
for i in range(5):
    
    os.system("clear")
    pac("|")
    pac("/")
    pac("-")
    pac("\\")
    