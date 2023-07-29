from click import getchar
from core import Screen, clr_ln

def main():
    screen = Screen()
    screen.put('This is where the game goes')
    while True:
        char = getchar()
        match char:
            case ':':
                command = input(':')
                clr_ln()
                commands = command.split(' ')
                match commands[0]:
                    case 'esc':
                        continue
                    case 'wq':
                        with open('./test.save', 'w', encoding='utf-8') as f:
                            f.write("saved and quit")
                        break
                    case "w":
                        with open('./test.save', 'w', encoding='utf-8') as f:
                            f.write("saved")
                    case 'q!':
                        print("force quit", end='\r')
                        break
                    case 'x':
                        print(f"Deleted {commands[1]} save file", end='\r')
                    case 'l':
                        print(f"Loaded {commands[1]} save file", end='\r')
                    case 'n':
                        print(f"New save file was created with name: {commands[1]}", end='\r')
                    case _:
                        print("Invalid option", end='')
            case 'h':
                clr_ln()
                print('Help mode', end='\r')
            case 'p':
                clr_ln()
                print('Play mode', end='\r')
            case 's':
                clr_ln()
                print('Settings mode', end='\r')
            case 'c':
                clr_ln()
                print('Credits', end='\r')
            case '\033':
                clr_ln()
                break
            case _:
                clr_ln()
                print('Unknown', end='\r')

if __name__ == '__main__':
    main()
