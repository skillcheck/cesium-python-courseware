from cesium.stats import math
from cesium.stats import menu

def main():

    menu.printIntro()
    
    values = None
    quit = False

    while not quit:
        menu.printMenu()
        choice = int(input())

        if choice == 1:
            values = menu.getValues()
        elif choice == 2:
            menu.showValues(values)
        elif choice == 3:
            print('Average is: ', math.average(values))
        elif choice == 0:
            quit = True
        else:
            print('Unrecognized input, try again please')

    menu.printOutro()

if __name__ == "__main__":
    main()
