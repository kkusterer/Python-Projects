import time, os, platform

def tt (delay=2.0):
    time.sleep(delay)

os_name = os.name
release_date = platform.release()
system_name = platform.system()

file_path = "HACK.txt"

with open(file_path, "w") as file:
    tt
    file.write("I am you coumputer.\n")
    tt
    file.write(f"Your OS is{os_name} .\n")
    tt
    file.write(f"release date {release_date} . \n")
    tt
    file.write(f"system name {system_name} . \n")

print(f"Hack pulled off. File name:'{file_path}'")

