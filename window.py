from click import getchar
from os import system

def execute(smth: str):
    print(f"Executing {smth}")

print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")
print("~")

def getesc():
    c = getchar()
    if c == '\033':
        print("escaped                 ")
        return True
    else:
        print("\rResuming input          ")

def autoclear(func):
    def inner(*args, **kwargs):
        func(*args, **kwargs)
        try:
            system('cls')
        except:
            system('clear')
    return inner

if __name__ == "__main__":
    while True:
        char = getchar().lower()
        match char:
            case ':':
                print("Command mode", end='\r')
                cmd = input(':')
                execute(cmd)
                esc = getesc()
                if esc: continue
            case 'p':
                print("Play mode", end='\r')
                esc = getesc()
                if esc: continue
            case 'h':
                print("Help mode", end='\r')
                esc = getesc()
                if esc: continue
            case 'c':
                print("Credits mode", end='\r')
                esc = getesc()
                if esc: continue
            case 'm':
                print("Menu mode", end='\r')
                esc = getesc()
                if esc: continue
            case 'b':
                    print("Breaking the law", end='\r')
                    break
            case _:
                print("Unknown command", end='\r')
