def narcissistic(value):
    stringValue = str(value)
    sum = 0

    for num in stringValue:
        sum += pow((int(num) % 10), len(stringValue))

    if sum == value:
        return True

    return False
    # Code away


print(narcissistic(7))
