def repeatedString(s, n):
    return n // len(s) * s.count('a') + s[:n % len(s)].count('a')


if __name__ == '__main__':
    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    print(result)
