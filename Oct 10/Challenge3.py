def count(str):
    """count = 0
    for i in range (len(str)):
        if str[i] == "-":
            count += 1

    return count"""

    return str.count("-") + 1

print(count("h-i-j"))