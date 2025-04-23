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

while True:
    main =input("Download bar(1) or loading text (2)")
    if main =='1':
        y_o_n_mainB = input("Do you wnat to download y or n")
        if y_o_n_mainB == 'y':
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

        if y_o_n_mainB == "n":
            pac_end("DOWNLOAD FAILED")
        else:
            break

    if main =='2':
        y_o_n_mainT = input("Do you wnat to download y or n")
    if y_o_n_mainT == 'y':
        for ii in range(1,5):
            pac("loading.")
            pac("loading..")
            pac("loading...")
            pac("loading....") 
        pac("done")
    if y_o_n_mainT == "n":
        pac_end("DOWNLOAD FAILED")
    else:
        break