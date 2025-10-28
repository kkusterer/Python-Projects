import curses
import time

def main(stdscr):
    #curses.curs_set(0)  # cursor
    stdscr.nodelay(True)  # instant input
    stdscr.timeout(1000)   # refresh 1000ms

    # size
    height, width = stdscr.getmaxyx()

    #position of ball
    x, y = width // 2, height // 2
    speed = 1

    while True:
        stdscr.clear()

        speed_text = f"Speed: {speed}"

        stdscr.addstr(0, 0, speed_text)


        random_text = f"Speed: {speed}"

        stdscr.addstr(0, 100, speed_text)

        stdscr.addstr(y, x, obj)  # make object

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_LEFT:
            x = max(0, x - speed)
        elif key == curses.KEY_RIGHT:
            x = min(width - len(obj), x + speed)
        elif key == curses.KEY_UP:
            y = max(0, y - speed)
        elif key == curses.KEY_DOWN:
            y = min(height - 1, y + speed)

        elif key == ord('r'):  # reset
            x, y = width // 2, height // 2
        elif key == ord('f'):  # faster
            speed += 1
        elif key == ord('s'):  # slower
            speed = max(1, speed - 1)
        elif key == ord('q'):  # quit
            break

        time.sleep(0.05)

while True:
    obj = input("enter custom object or type /exit/ to exit: ")

    if obj == "/exit/":
        break

    print(obj)
    if obj.strip() == "": #.strip() removes exrta spaces
        obj = "O"
    curses.wrapper(main)