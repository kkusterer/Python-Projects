dic = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
}

while True:
    number = input("Input a number (or 'exit' to quit): ")

    if number.lower() == "exit":
        break

    if number.isdigit():
        number = int(number) 

        if number in dic:
            print(dic[number])
        else:
            print("not in dic")
    else:
        print("Please enter a valid number.")
