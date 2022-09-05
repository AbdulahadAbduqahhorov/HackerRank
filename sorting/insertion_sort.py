def insertionSort1(n, arr):
    value = arr[-1]
    for i in range(len(arr)-2,-1,-1):
        
        if value<arr[i]:
            arr[i+1]=arr[i]
            print(" ".join(map(str,arr)))
        else:
            arr[i+1]=value
            print(" ".join(map(str,arr)))
            break
        if i==0:
            arr[0]=value
            print(" ".join(map(str,arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
