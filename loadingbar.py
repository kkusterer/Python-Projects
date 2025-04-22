import time, os

def pac(text, delay=0.5):
    print(text)
    time.sleep(delay)
    os.system('clear')

def pac_end(text, delay=1.0):
    print(text)
    time.sleep(delay)
    os.system('clear') 

y_o_n_main = input("Do you wnat to download y or n")
if y_o_n_main == 'y':
    for i in range(1,5):
        pac("loading.")
        pac("loading..")
        pac("loading...")
        pac("loading....") 
    pac("done")
if y_o_n_main == "n":
    pac_end("DOWNLOAD FAILED")