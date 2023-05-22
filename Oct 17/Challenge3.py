def list_xor(n,list1,list2):
    """
    if (n in list1) & (n not in list2):
        return True
    elif (n not in list1) & (n in list2):
        return True
    else:
        return False
    """
    return (n in list1) + (n in list2) ==1

if list_xor(1, [1,2,3], [4,5,6]):
    print("True")
else:
    print("False")