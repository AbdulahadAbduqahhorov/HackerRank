
def quickSort(arr):
    pivot = arr[0]
    i = 0
    for j in range(1,len(arr)):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[0],arr[i] = arr[i],arr[0]
    return arr

        

if __name__ == '__main__':
  

    result = quickSort([4,5,3,7,2])

    print(result)