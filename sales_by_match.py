def sockMerchant(n, ar):
    count = 0
    dic = {}
    for i in ar:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for l in dic:

        count+=dic[l]//2
    return count
print(sockMerchant(2,[10, 20, 20, 10, 10, 30, 50, 10, 20]))