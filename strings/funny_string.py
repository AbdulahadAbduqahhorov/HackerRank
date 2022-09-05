s = input()


def funnyString(s):
    r = s[::-1]

    t1 = []
    t2 = []

    for i in range(len(s) - 1):
        t1.append(abs(ord(s[i]) - ord(s[i + 1])))
        t2.append(abs(ord(r[i]) - ord(r[i + 1])))

    return "Funny" if t1 == t2 else "Not Funny"


print(funnyString(s))
