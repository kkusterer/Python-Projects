import random
import string

def gen_pass_lowercase():
    
    char1 = random.choice(string.ascii_lowercase)
    char2 = random.choice(string.ascii_lowercase)
    char3 = random.choice(string.ascii_lowercase)
    char4 = random.choice(string.ascii_lowercase)
    char5 = random.choice(string.ascii_lowercase)
    char6 = random.choice(string.ascii_lowercase)

    password = char1 + char2 + char3 + char4 + char5 + char6
    print(password)

def gen_pass_uppercase():
    
    char1 = random.choice(string.ascii_uppercase)
    char2 = random.choice(string.ascii_uppercase)
    char3 = random.choice(string.ascii_uppercase)
    char4 = random.choice(string.ascii_uppercase)
    char5 = random.choice(string.ascii_uppercase)
    char6 = random.choice(string.ascii_uppercase)

    password = char1 + char2 + char3 + char4 + char5 + char6
    print(password)

def gen_pass_mixed():
    
    char1 = random.choice(string.ascii_uppercase)
    char2 = random.choice(string.ascii_lowercase)
    char3 = random.choice(string.ascii_uppercase)
    char4 = random.choice(string.ascii_uppercase)
    char5 = random.choice(string.ascii_lowercase)
    char6 = random.choice(string.ascii_uppercase)

    password = char1 + char2 + char3 + char4 + char5 + char6
    print(password)

def gen_pass_num():
    
    char1 = str(random.randint(0, 100))
    char2 = str(random.randint(0, 100))
    char3 = str(random.randint(0, 100))
    char4 = str(random.randint(0, 100))
    char5 = str(random.randint(0, 100))
    char6 = str(random.randint(0, 100))

    password = char1 + char2 + char3 + char4 + char5 + char6
    print(password)

def gen_pass_all():
    
    char1 = random.choice(string.ascii_lowercase)
    char2 = str(random.randint(0, 100))
    char3 = random.choice(string.ascii_uppercase)
    char4 = str(random.randint(0, 100))
    char5 = random.choice(string.ascii_lowercase)
    char6 = random.choice(string.ascii_uppercase)

    password = char1 + char2 + char3 + char4 + char5 + char6
    print(password)
def gen_very_secure_password():
    char1 = random.choice(string.ascii_lowercase)
    char2 = str(random.randint(0, 100))
    char3 = random.choice(string.ascii_uppercase)
    char4 = str(random.randint(0, 160))
    char5 = random.choice(string.ascii_lowercase)
    char6 = random.choice(string.ascii_uppercase)
    char7 = random.choice(string.ascii_lowercase)
    char8 = str(random.randint(0, 1060))
    char9 = random.choice(string.ascii_uppercase)
    char10 = str(random.randint(0, 500))
    char11 = random.choice(string.ascii_lowercase)
    char12 = random.choice(string.ascii_uppercase)
    char13 = random.choice(string.ascii_lowercase)
    char14 = str(random.randint(4, 100))
    char15 = random.choice(string.ascii_uppercase)
    char16 = str(random.randint(44, 104))
    char17 = random.choice(string.ascii_lowercase)
    char18 = random.choice(string.ascii_uppercase)
    char19 = str(random.randint(66, 150))
    char20 = random.choice(string.ascii_uppercase)

    password = char1 + char2 + char3 + char4 + char5 + char6 + char8 + char8 + char9 + char10 + char11 + char12+ char13 + char14 + char15 + char16 + char17 + char18 + char19 +char20
    print(password)


while True:
    user = input("random password genrator. lowercase(1), uppercase(2), mixed letters(3), numbers(4), all(5), very secure(6), exit(7)")
    if user == "1":
        gen_pass_lowercase()
    if user == "2":
        gen_pass_uppercase()
    if user == "3":
        gen_pass_mixed()
    if user == "4":
        gen_pass_num()
    if user == "5":
        gen_pass_all()
    if user == "6":
        gen_very_secure_password()
    if user == "7":
        break