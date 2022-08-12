def migratoryBirds(arr):
    map = {}
    count = 0
    value = 0

    for elem in arr:
        if elem in map:
            map[elem] += 1
        else:
            map[elem] = 1

    for l in map:

        if map[l] > count:
            value = l
            count = map[l]
        elif map[l] == count:
            if value > l:
                value = l
                count = map[l]
    print(value)


migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4])
