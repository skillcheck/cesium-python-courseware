def printIntro():
    print(
        'This program calculates the average of a list of numbers. Follow '
        'the instructions on the menu'
    )

def printMenu():
    print(
        '\n\nSelect from the following:\n'
        '1) Enter values\n'
        '2) Show values\n'
        '3) Calculate average of values\n'
        '0) Exit'
    )

def getValues():
    print('Enter numeric values separated by a space:')
    return input().split()

def showValues(values):
    print('Current input values are: ', values)

def printOutro():
    print('Thanks for using the stats calculator. Come back soon!')
  