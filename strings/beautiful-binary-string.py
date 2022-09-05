
def beautifulBinaryString(b):
    arr = list(b)
    count = 0
    for i in range(len(arr)-2):
        if arr[i]=="0" and arr[i+1]=="1" and arr[i+2]=="0":
            count+=1
            arr[i+2]="1"
    return count