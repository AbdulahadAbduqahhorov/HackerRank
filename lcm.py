def get_lcm(a, b):
    if a >= b:
        greater = a
    else:
        greater = b
    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1
    return lcm


arr = [2, 4, 7, 9]
lcm = get_lcm(arr[0], arr[1])

for i in range(2, len(arr)):
    lcm = get_lcm(lcm, arr[i])

print(lcm)
