# This code makes a file called HACK.txt and puts info in the file.#

import time, os, platform

def tt (delay=2.0):
    time.sleep(delay)

os_name = os.name
release_date = platform.release()
system_name = platform.system()
processor_name = platform.processor()
architecture_details = platform.architecture()

file_name = input("Name of file( only name not [.txt]) :")

file = file_name + '.txt'

mode ="w"

with open(file, mode) as file:
    file.write("I am you coumputer.\n")
    file.write(f"Your OS is {os_name}.\n")
    file.write(f"release date {release_date}. \n")
    file.write(f"processor {processor_name}. \n")
    file.write(f"architecture {architecture_details}. \n")


print(f"Hack pulled off. File name:'{file_name + '.txt'}'")

