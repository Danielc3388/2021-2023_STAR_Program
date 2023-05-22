def add_dots(str):
    """output=""
    for i in range (len(str)-1):
        output = output + str[i] + "."
    output = output + str[len(str)-1]
    return(output)"""

    """output = ""
    for char in str:
        output += char + "."
    return output[:-1]"""

    return ".".join(str)

def remove_dots(str):
    """output = ""
    for i in str:
        if i != ".":
            output += i
    return output"""

    return str.replace(".","")

print(add_dots("HI"))
print (remove_dots("h.a.p.p.y"))