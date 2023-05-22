def mid(str):

    if (len(str)%2 == 0):
        return ""
    else:
        return str[(len(str)-1)//2]
        #  or return str[int(len(str)-1)/2]

print(mid(input("Input a string")))