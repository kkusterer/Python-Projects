while True:
        choice = input("encode(1), decode(2), quit(0): ")
        if choice not in ["0", "1", "2"]:
            print("Please choose 1, 2, or 0.")
            continue
        if choice == "0":
            break

        try:
            key = int(input("Enter key: "))
        except ValueError:
            print("key must be a number")
            continue

        text = input("Enter string: ")
        result = ""

        if choice == "1":
            for c in text:
                if c == " ":
                    result += " "
                elif c.isupper():
                    result += chr((ord(c) - ord('A') + key) % 26 + ord('A'))
                elif c.islower():
                    result += chr((ord(c) - ord('a') + key) % 26 + ord('a'))
                else:
                    result += c
            print("Encoded string:", result)
        else:
            for c in text:
                if c == " ":
                    result += " "
                elif c.isupper():
                    result += chr((ord(c) - ord('A') - key + 26) % 26 + ord('A'))
                elif c.islower():
                    result += chr((ord(c) - ord('a') - key + 26) % 26 + ord('a'))
                else:
                    result += c
            print("Decoded string:", result)