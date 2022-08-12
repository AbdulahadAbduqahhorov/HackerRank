def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(0, n - 1):
        for j in range(i+1, n):
            sum = ar[i] + ar[j]
            if sum % k == 0:
                count += 1
    return count


print(divisibleSumPairs(6, 5, [1, 2, 3, 4, 5, 6]))
