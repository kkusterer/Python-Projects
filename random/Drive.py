#pip install keyboard
import keyboard

class drive:
    right = "right"
    left = "left"
    forward = "forward"
    back = "back"

while True:

    if keyboard.is_pressed('w'):
        print(drive.forward)

    if keyboard.is_pressed('s'):
        print(drive.back)

    if keyboard.is_pressed('a'):
        print(drive.left)
    
    if keyboard.is_pressed('d'):
        print(drive.left)
    
    else:
        print("error")
    