def getMoneySpent(keyboards, drives, b):
    t = 0
    for i in keyboards:
        for j in drives:
            r = i + j
            if b >= r > t:
                t = r

    if t == 0:
        return -1
    return t


print(getMoneySpent([5], [4], 5))
