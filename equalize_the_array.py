from collections import Counter
def equalizeArray(arr):
    c = Counter(arr)
    max = 0

    for i in c:
        if c[i]>max:
           max = c[i]

    return len(arr)-max



if __name__ == '__main__':


    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(result)
