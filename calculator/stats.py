def average(values):
    '''
    Calculates the average of provided list of values.
    '''
    if values is None:
        return 0
    numValues = len(values)
    if numValues == 0:
        return 0

    sum = 0
    for value in values:
        sum += float(value)

    return sum / numValues

def main():

    print('This program calculates the average of a list of numbers')
    print('Enter a list of numeric values separated by spaces: ')
    str = input()
    values = str.split()
    
    print('The average is: ', average(values))

if __name__ == "__main__":
    main()
