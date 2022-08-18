def findDigits(n):
    count = 0
    for i in str(n):
        if i != '0' and n % int(i) == 0:
            count += 1
    return count


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        print(result)
