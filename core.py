import math
from keyboard import wait as k_wait
from keyboard import read_key as k_read
from keyboard import on_release as k_on_release
from keyboard import KeyboardEvent
from time import sleep

class Screen:
    
    def __init__(self, row_len: int = 50):
        self.row_len = row_len
        self.scale = math.ceil(self.row_len / 25)
        self.line_count: int = 0

    def put(self, *values: str, row_len: int | None = None, preset: bool = False, **kwargs):
        if row_len is None:
            row_len = self.row_len
            scale = math.ceil(row_len / 25)
        else:
            scale = math.ceil(row_len / 25)
            row_len = 50
        if preset:
            self.line_count += values.count('\n')
            for value in values:
                print(value, **kwargs)
            # need to adjust that shit
        else:
            for val in values:
                val = str(val)
                self.line_count += val.count('\n')
                self.line_count += len(val) // (scale * 25)
                counter = 0
                for char in val:
                    if counter % (scale * 25) == 0 and counter != 0:
                        print()
                    print(char, end='')
                    counter += 1
            self.line_count += 1
            print()
    
    def clear(self, extra: int = 0):
        line_count = self.line_count + extra
        print(f'\033[{line_count}A', end='')  # move cursor up N times (\033[<N>A)
        for i in range(self.line_count):
            print(' ' * self.row_len)
        print(f'\033[{line_count}A', end='')  # move cursor up N times (\033[<N>A)s
        self.line_count = 0

def clr_ln():
    print('\033[2K', end='\r')

class Menu():
    def Menu(screen: Screen, options: list[str]) -> str:
        selected: int = 0
        while True:
            sleep(0.25)
            for i in range(len(options)):
                if i == (selected % len(options)):
                    screen.put(f">{options[i]}")
                else:
                    screen.put(f" {options[i]}")
            key = k_read()
            if key == 'esc':
                break
            elif key == 'enter':
                return options[selected]
            elif key == 'up':
                selected -= 1
            elif key == 'down':
                selected += 1
            else:
                pass
            screen.clear(())
    
    def InfoMenu(screen: Screen, options: dict[str, str | int | float]) -> None:
        keys = list(options.keys())
        selected = 0
        while True:
            sleep(0.25)
            screen.clear()
            for i in range(len(options)):
                if i == (selected % len(options)):
                    screen.put(f">{keys[i]}")
                else:
                    screen.put(f" {keys[i]}")
            key = k_read()
            if key == "enter":
                screen.clear()
                screen.put(f"{options[keys[i]]}\npress [SPACE] to continue")
                k_wait('space')
            elif key == 'esc':
                break
            elif key == 'up':
                selected -= 1
            elif key == 'down':
                selected += 1
            else:
                pass

def startup(screen: Screen) -> None:
    from random import randint
    from pickle import load
    rand = randint(1, 10)
    if rand == 5:
        path = './vscredits.pkl'
    else:
        path = 'vslogo.pkl'
    with open(path, mode='rb') as f:
        unpickled = load(f)
        # print(unpickled)
        screen.put(unpickled, preset=True)

options: dict = \
{
    "fruit": "apple",
    "number": 100,
    "Boolean": True,
    "Something else": "TRAZSADZEGMDEV",
    "SOmething again": "something"
}
# screen = Screen()
# selection = Menu.InfoMenu(screen, options)
