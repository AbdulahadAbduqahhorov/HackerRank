def makingAnagrams(s1, s2):
    alp = {}

    for i in s1:
        if i in alp:
            alp[i] += 1
        else:
            alp[i] = 1

    for j in s2:
        if j in alp:
            alp[j] -= 1
        else :
            alp[j] = -1
    sum = 0
    for t in alp:
        sum+=abs(alp[t])

    return sum

if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    print(result)
