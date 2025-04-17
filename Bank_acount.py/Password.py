jeff_username = "jeff123"
jeff_password = "idk123"
jack_username = "jacky"
jack_password = "thisisimp"

main_username = input("what is your username:   ")

if main_username == jeff_username:
    jeff_password_check = input("what is your password:   ")
    if jeff_password_check == jeff_password:
        print("Welcome, Jeff.")

if main_username == jack_username:
    jack_password_check = input("what is your password:   ")
    if jack_password_check == jack_password:
        print("Welcome, Jack.")