

def reset_username():
    name2 = input("what is your new username")
    print(f'Welcome, {name2}')


def reset_password():
    newpas = input("what is your new pass")
    print(f"your new pass is {newpas}")


def manage_account_balance():

    money = input("1 get money ,2 remove money")

    add_money = input("how much money do you want to add")

    set_money = '100'

    if money == '1':

        new_money = int(add_money) + int(set_money)

        print(f'you havee ${new_money}')

    if money == '2':

        new_money = int(add_money) + int(set_money)

        remove_money = input('how much money do you want to remove')

        new_new_money = int(new_money) - int(remove_money)

        print(f'you now have ${new_new_money}')


name = input("what is your username")
print(f"Welcome, {name}")

pas = input("what is your password")

while True:

    if pas == '1234' and name == "kaleb":
        main_menu = input("(1) reset usr name, (2) reset pass, (3) acount ballence, (4)help/about, (5) logout")

        if main_menu == '1':
            reset_username()

        if main_menu == '2':
            reset_password()

        if main_menu == '3':
            manage_account_balance()

        if main_menu == '4':
            print("I have been working on this project for almmsot a year. I started in around 2024. The program is very buggy and some things dont even work.  ")
            print("When you remove money and it prompts you with 'how much money you want to add' you need to put in a 0 then prosead withe the removel of money from the acount")
            print("Also the password reset and username resat do not work and if you put in the wrong info it will forever say 'error' press ctrl+C")
        if main_menu == '5':
            print("logged out")
            break


    else:
        print("error") #not working#
