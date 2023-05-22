def palindrome (str):
    """
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True
    """

    """
    list1[]
    list2[]
    for i in range(led(str)):
        list1.appent(str[1])
        list2.insert(0,str[i])
    return list1 == list2
    """

    return str == str[::-1]

if palindrome("fwishdvn"):
    print("true")
else:
    print("false")