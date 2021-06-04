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
