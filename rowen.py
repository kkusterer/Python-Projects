import os
import time
class rowen:
    class brain:
        smart = 'smart 1/100'
        creative = "creative 5/100"
        weird = 'wierd is 100/100'
    class person:
        race = "Race is british" 
        color = "wite" 
        hair = 'hair is yellow'
while True:
    start = input("1 findout what is happening is rowens brain, 2 what he looks like")
    if start == '1':
        print(rowen.brain.smart)
        print(rowen.brain.creative)
        print(rowen.brain.weird)
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')

    if start == '2':
        print(rowen.person.race)
        print(rowen.person.color)
        print(rowen.person.hair)
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
