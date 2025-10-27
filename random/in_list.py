names = []

while True:

    add_names = input("enter name in to the system:")

    names.append(add_names)

    print(names)

    main = input("name: ")

    if main in names:

        print(main)

    else:

        print("error")
        