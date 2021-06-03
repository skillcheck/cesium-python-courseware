import stats

def main():

    print('This program calculates the average of a list of numbers')
    print('Enter a list of numeric values separated by spaces: ')
    str = input()
    values = str.split()
    
    print('The average is: ', stats.average(values))

if __name__ == "__main__":
    main()
