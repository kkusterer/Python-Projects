while True:
    print("1 varable")
    print("2 varable")
    print("3 varable")
    print("4 varable")
    print("5 varable")

    choice = input("Choose an option (1 2 3 4 5): ")

    print("+0")
    print("+1")
    print("+2")
    print("+3")

    choice2 = input("Choose an option (0 1 2 3): ")

    if choice == '1' and choice2 == '0':
        x1 = input("Choose a # for x: ")
        sum = int(x1) + 0
        print(sum)

    if choice == '1' and choice2 == '1':
        x1 = input("Choose a # for x: ")
        sum = int(x1) + 1
        print(sum)

    if choice == '1' and choice2 == '2':
        x1 = input("Choose a # for x: ")
        sum = int(x1) + 2
        print(sum)

    if choice == '1' and choice2 == '3':
        x1 = input("Choose a # for x: ")
        sum = int(x1) + 3
        print(sum)

    if choice == '2' and choice2 == '0':
        x1 = input("Choose a # for x: ")
        x2 = input("Choose a # for x: ")
        sum = int(x1) + int(x2) + 0
        print(sum)

    if choice == '2' and choice2 == '1':
        x1 = input("Choose a # for x: ")
        x2 = input("Choose a # for x: ")
        sum = int(x1) + int(x2) + 1
        print(sum)

    if choice == '2' and choice2 == '2':
        x1 = input("Choose a # for x: ")
        x2 = input("Choose a # for x: ")
        sum = int(x1) + int(x2) + 2
        print(sum)

    if choice == '2' and choice2 == '3':
        x1 = input("Choose a # for x: ")
        x2 = input("Choose a # for x: ")
        sum = int(x1) + int(x2) + 3
        print(sum)

    if choice == '3' and choice2 == '0':
        x1 = input("Choose a # for x: ")
        x2 = input("Choose a # for x: ")
        x3 = input("Choose a # for x: ")
        sum = int(x1) + int(x2) + int(x3) + 0
        print(sum)

    if choice == '3' and choice2 == '1':
        x1 = input("Choose a # for x: ")
        x2 = input("Choose a # for x: ")
        x3 = input("Choose a # for x: ")
        sum = int(x1) + int(x2) + int(x3) + 1
        print(sum)

    if choice == '3' and choice2 == '2':
        x1 = input("Choose a # for x: ")
        x2 = input("Choose a # for x: ")
        x3 = input("Choose a # for x: ")
        sum = int(x1) + int(x2) + int(x3) + 2
        print(sum)

    if choice == '3' and choice2 == '3':
        x1 = input("Choose a # for x: ")
        x2 = input("Choose a # for x: ")
        x3 = input("Choose a # for x: ")
        sum = int(x1) + int(x2) + int(x3) + 3
        print(sum)

    if choice == '4' and choice2 == '0':
        x1 = input("Choose a # for x: ")
        x2 = input("Choose a # for x: ")
        x3 = input("Choose a # for x: ")
        x4 = input("Choose a # for x: ")
        sum = int(x1) + int(x2) + int(x3) + int(x4) + 0
        print(sum)

    if choice == '4' and choice2 == '1':
        x1 = input("Choose a # for x: ")
        x2 = input("Choose a # for x: ")
        x3 = input("Choose a # for x: ")
        x4 = input("Choose a # for x: ")
        sum = int(x1) + int(x2) + int(x3) + int(x4) + 1
        print(sum)

    if choice == '4' and choice2 == '2':
        x1 = input("Choose a # for x: ")
        x2 = input("Choose a # for x: ")
        x3 = input("Choose a # for x: ")
        x4 = input("Choose a # for x: ")
        sum = int(x1) + int(x2) + int(x3) + int(x4) + 2
        print(sum)

    if choice == '4' and choice2 == '3':
        x1 = input("Choose a # for x: ")
        x2 = input("Choose a # for x: ")
        x3 = input("Choose a # for x: ")
        x4 = input("Choose a # for x: ")
        sum = int(x1) + int(x2) + int(x3) + int(x4) + 3
        print(sum)

    if choice == '5' and choice2 == '0':
        x1 = input("Choose a # for x: ")
        x2 = input("Choose a # for x: ")
        x3 = input("Choose a # for x: ")
        x4 = input("Choose a # for x: ")
        x5 = input("Choose a # for x: ")
        sum = int(x1) + int(x2) + int(x3) + int(x4) + int(x5) + 0
        print(sum)

    if choice == '5' and choice2 == '1':
        x1 = input("Choose a # for x: ")
        x2 = input("Choose a # for x: ")
        x3 = input("Choose a # for x: ")
        x4 = input("Choose a # for x: ")
        x5 = input("Choose a # for x: ")
        sum = int(x1) + int(x2) + int(x3) + int(x4) + int(x5) + 1
        print(sum)

    if choice == '5' and choice2 == '2':
        x1 = input("Choose a # for x: ")
        x2 = input("Choose a # for x: ")
        x3 = input("Choose a # for x: ")
        x4 = input("Choose a # for x: ")
        x5 = input("Choose a # for x: ")
        sum = int(x1) + int(x2) + int(x3) + int(x4) + int(x5) + 2
        print(sum)

    if choice == '5' and choice2 == '3':
        x1 = input("Choose a # for x: ")
        x2 = input("Choose a # for x: ")
        x3 = input("Choose a # for x: ")
        x4 = input("Choose a # for x: ")
        x5 = input("Choose a # for x: ")
        sum = int(x1) + int(x2) + int(x3) + int(x4) + int(x5) + 3
        print(sum)

    else:
        print("error")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if next_calculation.lower() != 'yes':
        break
