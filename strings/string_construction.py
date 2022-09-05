def stringConstruction(s):
    l = []
    for i in s:
        if i not in l:
            l.append(i)
    return len(l)

if __name__ == '__main__':


    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        print(result)

