def flatten (list):
    empty = []
    for i in list:
        for j in i:
            empty.append(j)
    return empty


print(flatten([[1,2,3],[4,5,6]]))