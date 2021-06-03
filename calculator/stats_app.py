import stats
from stats_menu import *

def main():

    printIntro()
    
    values = None
    quit = False

    while not quit:
        printMenu()
        choice = int(input())

        if choice == 1:
            values = getValues()
        elif choice == 2:
            showValues(values)
        elif choice == 3:
            print('Average is: ', stats.average(values))
        elif choice == 0:
            quit = True
        else:
            print('Unrecognized input, try again please')

    printOutro()

if __name__ == "__main__":
    main()
