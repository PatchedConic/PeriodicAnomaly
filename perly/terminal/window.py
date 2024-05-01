import curses
from curses import wrapper
import time

def main(stdscr):
    stdscr.clear()
    time.sleep(5)

if __name__ == "__main__":
    wrapper(main)