def consecutive_zeros(str):
    """
    currentZero = 0
    Max = 0
    for i in range(len(str)):
        if str[i] == '0':
            currentZero +=1
            if currentZero > Max:
                Max = currentZero

        else:
            currentZero = 0
    return Max
    """
    return max([len(zero) for zero in str.split("1")])

print (consecutive_zeros("900000001000000001001000000000"))