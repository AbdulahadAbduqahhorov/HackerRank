from collections import Counter
def gameOfThrones(s):
    count = 0
    c = Counter(s)
    for i in c:
        if c[i]%2==1:
            count+=1
    return 'YES' if count<=1 else 'NO'

if __name__ == '__main__':


    s = input()

    result = gameOfThrones(s)


