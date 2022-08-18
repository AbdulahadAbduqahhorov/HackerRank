def viralAdvertising(n):
    shared = 5
    cumulative = 0
    for i in range(n):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3

    return cumulative


if __name__ == '__main__':

    n = int(input().strip())

    result = viralAdvertising(n)

    print(result)

