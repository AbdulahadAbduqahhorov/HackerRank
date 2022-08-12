def find_gcd(x, y):
    while (y):
        x, y = y, x % y

    return x


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


def get_total(list1, list2):
    num1 = list2[0]
    num2 = list2[1]
    gcd = find_gcd(num1, num2)

    for i in range(2, len(list2)):
        gcd = find_gcd(gcd, list2[i])

    lcm = get_lcm(list1[0], list1[1])

    for i in range(2, len(list1)):
        lcm = get_lcm(lcm, list1[i])

    count = 0
    i=1
    t = lcm
    while t<=gcd:
        if gcd%t==0:
            count+=1
        i+=1
        t = lcm*i


    print(count)
get_total([2, 4], [16,32,96])
