import time, os

def pac(text, delay=0.4):
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
    pac("done")