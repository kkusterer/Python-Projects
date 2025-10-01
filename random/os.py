import os
import time
import webbrowser
import platform
import datetime
from datetime import datetime

running = True

MAX_CONTENT = 256

class Node:
    def __init__(self, name, is_dir):
        self.name = name
        self.is_dir = is_dir
        self.content = ""
        self.parent = None
        self.children = []

def cmd_search(args):
    if not args:
        print("Usage: search <query>")
        return
    
    query = args.replace(" ", "+")
    url = "https://www.google.com/search?q=" + query

    webbrowser.open(url)
    print(f"Searching the web for: {args}")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def cmd_calc(agu):
    def calculator():
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        while True:
            choice = input("Enter choice (1/2/3/4): ")

            if choice in ['1', '2', '3', '4']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Invalid input")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() != 'yes':
                break

    calculator()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def shutdown_os():
    clear_screen()
    print("Shutting down KalebOS...")
    time.sleep(3)
    clear_screen()

def find_child(dir_node, name):
    for child in dir_node.children:
        if child.name == name:
            return child
    return None

def add_child(parent, child):
    if len(parent.children) < 16:
        parent.children.append(child)
        child.parent = parent
    else:
        print(f"Error: too many children in {parent.name}")


root = Node("", True)
current_dir = root

readme = Node("readme.txt", False)
readme.content = "Welcome to KalebOS \nType 'help' to see commands"
add_child(root, readme)

authors = Node("authors.txt", False)
authors.content = "The authors shall be listed as such:\nName, Email, what thay did\nKaleb Kusterer, kkusterer@students.vlhs.com, main devloper"
add_child(root, authors)


def cmd_exit(args):
    global running
    shutdown_os()
    running = False

def cmd_clear(args):
    clear_screen()


def cmd_encode(args):
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


def cmd_info(arg):
    os_name = os.name
    release_date = platform.release()
    system_name = platform.system()
    processor_name = platform.processor()
    architecture_details = platform.architecture()

    print(f"OS name: {os_name}")
    print(f"Release date: {release_date}")
    print(f"system: {system_name}")
    print(f"processor: {processor_name}")
    print(f"architecture details: {architecture_details}")

def cmd_ls(args):
    for c in current_dir.children:
        print(c.name + ("/" if c.is_dir else ""), end="  ")
    print()

def cmd_cd(args):
    global current_dir
    if not args:
        current_dir = root
        return
    if args == "..":
        if current_dir.parent:
            current_dir = current_dir.parent
        return
    next_dir = find_child(current_dir, args)
    if next_dir and next_dir.is_dir:
        current_dir = next_dir
    else:
        print(f"cd: no such directory: {args}")

def cmd_cat(args):
    if not args:
        print("Usage: cat <file>")
        return
    f = find_child(current_dir, args)
    if f and not f.is_dir:
        print(f.content)
    else:
        print(f"cat: no such file: {args}")

def cmd_touch(args):
    if not args:
        print("Usage: touch <filename>")
        return
    if find_child(current_dir, args):
        print("touch: file already exists")
        return
    add_child(current_dir, Node(args, False))

def cmd_mkdir(args):
    if not args:
        print("Usage: mkdir <dirname>")
        return
    if find_child(current_dir, args):
        print("mkdir: directory already exists")
        return
    add_child(current_dir, Node(args, True))

def cmd_echo(args):
    if not args:
        print("Usage: echo <text> > <file>")
        return
    if ">" not in args:
        print(args)
        return
    text, filename = args.split(">", 1)
    text = text.strip()
    filename = filename.strip()
    f = find_child(current_dir, filename)
    if not f:
        f = Node(filename, False)
        add_child(current_dir, f)
    f.content = text

def cmd_pwd(args):
    path = ""
    n = current_dir
    while n:
        path = "/" + n.name + path
        n = n.parent
    print(path if path != "/" else "/")

def cmd_help(args):
    print("----------------------------------------------------------------------")
    print("KalebOS Command Guide:")
    print("----------------------------------------------------------------------")
    print("File/Folder Commands:")
    print("  ls                 - List files and folders in current directory")
    print("  cd DIR             - Change directory to DIR (use '..' to go up)")
    print("  mkdir DIR          - Create a new folder named DIR")
    print("  touch FILE         - Create a new empty file named FILE")
    print("  echo TEXT > FILE   - Write TEXT into FILE (creates if missing)")
    print("  cat FILE           - Show contents of FILE")
    print("  pwd                - Show the current folder path")
    print("----------------------------------------------------------------------")
    print("Utility Commands:")
    print("  clear              - Clear the terminal screen")
    print("  exit               - Exit the os")
    print("  help               - Shows help menu")
    print("----------------------------------------------------------------------")
    print("Experimental Commands:")
    print("  encode             - Encode or decode a string using a Caesar cipher")
    print("  search QUERY       - Open your browser and search QUERY on the web")
    print("  info               - Gives information of you machine and cpu")
    print("  calc               - opens calaulator")
    print("----------------------------------------------------------------------")
    print("Usage Examples:")
    print("  ls")
    print("  cd docs")
    print("  mkdir new_folder")
    print("  touch notes.txt")
    print("  echo Hello World > notes.txt")
    print("  cat notes.txt")
    print("  search Python tutorials")
    print("----------------------------------------------------------------------")


commands = {
    "ls": cmd_ls,
    "cd": cmd_cd,
    "mkdir": cmd_mkdir,
    "touch": cmd_touch,
    "echo": cmd_echo,
    "cat": cmd_cat,
    "pwd": cmd_pwd,
    "help": cmd_help,
    "exit": cmd_exit,
    "encode": cmd_encode,
    "clear": cmd_clear,
    "search": cmd_search,
    "info": cmd_info,
    "calc": cmd_calc,
    
}

def handle_command(input_line):
    parts = input_line.strip().split(" ", 1)
    cmd = parts[0]
    args = parts[1] if len(parts) > 1 else ""
    if cmd in commands:
        commands[cmd](args)
    else:
        print(f"Unknown command: {cmd}")

def main():
    global current_dir
    clear_screen()
    print("Welcome to KalebOS")
    print("Type 'help' for a list of commands.\n")

    while running:
        input_line = input("KalebOS> ")
        handle_command(input_line)

if __name__ == "__main__":
    main()
