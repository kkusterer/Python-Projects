import socket
import os
import time
port = 65535
i = 0

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('0.0.0.0', port))


while True:
    user_user = input("enter username: ")
    client_socket.send(user_user.encode())
    response = client_socket.recv(1024).decode()
    if response == '1':
        i += 1
        break
    else:
        print("enter correct username")

while True:
    user_pass = input("enter password: ")
    client_socket.send(user_pass.encode())
    response = client_socket.recv(1024).decode()
    if response == '1':
        i += 1
        break
    else:
        print("enter correct password")

if i == 2:
    
    # ==========================
    # Globals
    # ==========================
    running = True

    MAX_CONTENT = 256

    # ==========================
    # File system classes
    # ==========================
    class Node:
        def __init__(self, name, is_dir):
            self.name = name
            self.is_dir = is_dir
            self.content = ""
            self.parent = None
            self.children = []

    root = Node("", True)
    current_dir = root

    # ==========================
    # Helpers
    # ==========================
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    def shutdown_os():
        clear_screen()
        print("Shutting down KalebOS...")
        time.sleep(5)
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

    # ==========================
    # Commands
    # ==========================
    def cmd_exit(args):
        global running
        shutdown_os()
        running = False

    def cmd_clear(args):
        clear_screen()

    def cmd_test(args):
        while True:
            choice = input("encode(1), decode(2), quit(0): ")
            if choice not in ["0", "1", "2"]:
                print("Please choose 1, 2, or 0.")
                continue
            if choice == "0":
                break
            key = int(input("Enter key: "))
            text = input("Enter string: ")
            result = ""
            if choice == "1":  # encode
                for c in text:
                    if c.isupper():
                        result += chr((ord(c) - ord('A') + key) % 26 + ord('A'))
                    elif c.islower():
                        result += chr((ord(c) - ord('a') + key) % 26 + ord('a'))
                    else:
                        result += c
                print("Encoded string:", result)
            else:  # decode
                for c in text:
                    if c.isupper():
                        result += chr((ord(c) - ord('A') - key + 26) % 26 + ord('A'))
                    elif c.islower():
                        result += chr((ord(c) - ord('a') - key + 26) % 26 + ord('a'))
                    else:
                        result += c
                print("Decoded string:", result)

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
        print("----------------------------------------")
        print("Commands:                               ")
        print("  ls             - list files           ")
        print("  cd DIR         - change directory     ")
        print("  mkdir DIR      - create directory     ")
        print("  touch FILE     - create file          ")
        print("  echo TEXT > F  - write to file        ")
        print("  cat FILE       - show file contents   ")
        print("  pwd            - show current path    ")
        print("  help           - show this menu       ")
        print("  exit           - quit KalebOS         ")
        print("  clear          - clears the screen    ")
        print("  test           - dev stuff rn         ")
        print("----------------------------------------")

    # ==========================
    # Command dispatcher
    # ==========================
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
        "test": cmd_test,
        "clear": cmd_clear,
    }

    def handle_command(input_line):
        parts = input_line.strip().split(" ", 1)
        cmd = parts[0]
        args = parts[1] if len(parts) > 1 else ""
        if cmd in commands:
            commands[cmd](args)
        else:
            print(f"Unknown command: {cmd}")

    # ==========================
    # Main loop
    # ==========================
    def main():
        global current_dir
        clear_screen()
        print("Welcome to KalebOS")
        print("Type 'help' for a list of commands.\n")

        while running:
            input_line = input("KalebOS> ")
            handle_command(input_line)



else:
    print("wrong username or password")

if __name__ == "__main__":
    main()
