# THIS CODE WRIGHTS TO 
import time, os, platform

def tt (delay=2.0):
    time.sleep(delay)

os_name = os.name
release_date = platform.release()
system_name = platform.system()

file_path = "HACK.txt"

with open(file_path, "w") as file:
    file.write("I am you coumputer.\n")
    file.write(f"Your OS is{os_name} .\n")
    file.write(f"release date {release_date} . \n")
    file.write(f"system name {system_name} . \n")

print(f"Hack pulled off. File name:'{file_path}'")

