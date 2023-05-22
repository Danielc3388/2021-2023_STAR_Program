def format_number(int):
    """
    reverse = str(int)[::-1]
    if len(reverse) == 1:
        return reverse
    list1 = []
    list2 = []
    temp = ""
    for i in reverse:
        list1.insert(0,i)
        if len(list1) == 3:
            temp = "".join(list1)
            list2.insert(0, temp)
            list1.clear()
    if len(reverse) % 3 != 0:
        temp = "".join(list1)
        list2.insert(0, temp)
    list2 = ",".join(list2)
    return list2
    """

    """
    result = ""
    for i, digit in enumerate(str(int)[::-1]):
        if i != 0 and (i%3) == 0:
            result += ','
        result += digit
    return result[::-1]
    """

    return "{:,}".format(int)


print(format_number(231467))