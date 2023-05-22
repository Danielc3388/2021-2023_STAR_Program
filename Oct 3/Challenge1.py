def capital_indexes(x):
    outputList = []
    for index in range(len(x)):
        if x[index].isupper():
            outputList.append(index)

    return outputList

while True:
    print(capital_indexes(input("Input String ")))
    if (input("Enter exit to end code") == "exit"):
        break