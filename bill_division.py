def bonAppetit(bill, k, b):
    sum = 0
    for i in bill:
        sum += i
    anna = (sum - bill[k]) // 2
    if anna == b:
        print("Bon Appetit")
    else:
        print(sum // 2 - anna)


bonAppetit([3, 10, 2, 9], 1, 12)
