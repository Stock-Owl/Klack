from click import getchar
from core import Screen, clr_ln, startup
from pickle import dumps, loads

def main():
    screen = Screen()
    startup(screen)
    while True:
        char = getchar()
        if char == ':':
            command = input(':')
            clr_ln()
            commands = command.split(' ')
            match commands[0]:
                case 'esc':
                    continue
                case 'wq':
                    with open('./test.save', 'wb', encoding='utf-8') as f:
                        f.write(pickle.dumps("smth"))
                    break
                case "w":
                    with open('./test.save', 'wb', encoding='utf-8') as f:
                        f.write(pickle.dumps("smth"))
                case 'q!':
                    print("force quit", end='\r')
                    break
                case 'x':
                    print(f"Deleted {commands[1]} save file", end='\r')
                case 'l':
                    with open('./test.save', 'rb', encoding='utf-8') as f:
                        pickle.loads(f.read)
                    print(f"Loaded {commands[1]} save file", end='\r')
                case 'n':
                    with open(f'./{commands[1]}.save', 'wb', encoding='utf-8') as f:
                        pass
                case _:
                    print("Invalid option", end='')
        elif char == 'h' or '?':
            clr_ln()
            print('Help mode', end='\r')
        elif char == 'p':
            clr_ln()
            print('Play mode', end='\r')
        elif char == 's':
            clr_ln()
            print('Settings mode', end='\r')
        elif char == 'c':
            clr_ln()
            print('Credits', end='\r')
        else:
            clr_ln()
            print('Unknown', end='\r')

if __name__ == '__main__':
    main()
