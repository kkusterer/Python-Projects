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

    while True:
        stdscr.clear()
        stdscr.addstr(y, x, "O")  # make ball
        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_LEFT:
            x = max(0, x - 1)

        elif key == curses.KEY_RIGHT:
            x = min(width - 1, x + 1)

        elif key == curses.KEY_UP:
            y = max(0, y - 1)

        elif key == curses.KEY_DOWN:
            y = min(height - 1, y + 1)
            
        elif key == ord('q'):
            break

        #time.sleep(0.05)

curses.wrapper(main)
