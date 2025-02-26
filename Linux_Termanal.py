
while True:
    commandinhome = input('~$ (Home)')

    if commandinhome == 'exit':
        break

    if commandinhome == 'help':
        print("cd [target location] example of target location: Documents,Downloads,ect.")
        print("ls: opens slected folder you are in Example: ~$(Downloads) ls ")
        print('ping: this command does not work yet')

    if commandinhome == "ping 8.8.8.8":
        print("ping works")


    if commandinhome == 'ls':
        print("Documents")
        print('Downloads')
        print('Misk')
        print('work in progress')

    if commandinhome == "cd":
        print("error 'cd [target location]'")

    if commandinhome == "cd Documents":
        command_inCD_documents = input("~$ (Documents)")

        if command_inCD_documents == 'cd random test1':
            print("this is test 1")
        if command_inCD_documents == 'cd random test2':
            print("this is test 2")
        if command_inCD_documents == 'cd random test3':
            print("this is test 3")
        if command_inCD_documents == 'cd random test4':
            print("this is test 4")

        if command_inCD_documents == 'ls':
            print("random test1")

            print("random test2")

            print("random test3")

            print("random test4")

    if commandinhome == "cd Downloads":

        command_inCD_downloads = input("~$ (Downloads)")
        if command_inCD_downloads == 'cd random test1 down':
            print("this is test 1 down")
        if command_inCD_downloads == 'cd random test2 down':
            print("this is test 2 down")
        if command_inCD_downloads == 'cd random test3 down':
            print("this is test 3 down")
        if command_inCD_downloads == 'cd random test4 down':
            print("this is test 4 down")

        if command_inCD_downloads == 'ls':
            print("random test1 down")

            print("random test2 down")

            print("random test3 down")

            print("random test4 down")

    if commandinhome == "cd Misk":
        command_inCD_misk = input("~$ (Misk)")

        if command_inCD_misk == 'cd random test1 misk':
            print("this is test 1 misk")
        if command_inCD_misk == 'cd random test2 misk':
            print("this is test 2 misk")
        if command_inCD_misk == 'cd random test3 misk':
            print("this is test 3 misk")
        if command_inCD_misk == 'cd random test4 misk':
            print("this is test 4 misk")

        if command_inCD_misk == 'ls':
            print("random test1 misk")

            print("random test2 misk")

            print("random test3 misk")

            print("random test4 misk")
