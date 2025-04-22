list_passwords = ['1','2','3']
while True:
    main_pass = input("what is your pass")
    if main_pass == list_passwords[0-2]:
        print('this was a success')
    if main_pass =='e':
        break
    else:
        print("error")