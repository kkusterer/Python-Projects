import time, os

def pac(text, delay=0.4):
    print(text)
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')

def pac_dot(text, delay=0.2):
    print(text)
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')

def pac_end(text, delay=1.0):
    print(text)
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')

y_o_n_main = input("Do you wnat to download y or n")
if y_o_n_main == 'y':
    pac("")
    for i in range(3):
        pac("[]")
        pac("[][]")
        pac("[][][]")
        pac("[][][][]")
        pac("[][][][][]")
        pac("[][][][][][]")
        pac("[][][][][][][]")
    for x in range(1):
        pac_dot("[.][][][][][][]") 
        pac_dot("[.][.][][][][][]")
        pac_dot("[.][.][.][][][][]")
        pac_dot("[.][.][.][.][][][]") 
        pac_dot("[.][.][.][.][.][][]")
        pac_dot("[.][.][.][.][.][.][]")
        pac_dot("[.][.][.][.][.][.][.]")
        pac("done")

if y_o_n_main == "n":
    pac_end("DOWNLOAD FAILED")