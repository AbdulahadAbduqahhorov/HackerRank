

def marsExploration(s):
    t=0
    for i in range(len(s)):
        if i%3==1 and s[i]!='O':
            t+=1
        elif (i%3==2 or i%3==0 )and s[i]!='S':
            t+=1
    return t



if __name__ == '__main__':
    s = input()

    result = marsExploration(s)
    print(result)


