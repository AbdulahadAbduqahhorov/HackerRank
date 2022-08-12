def birthday(s, d, m):
        t=0
        for i in range(0,len(s)-m+1):
            sum = 0
            for j in range(i,i+m):
                sum+=s[j]
            if sum==d:
                t+=1
        print(t)


birthday([2,2,1,3,2],4,2)