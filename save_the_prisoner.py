def saveThePrisoner(n, m, s):
    re = m%n
    if (re+s-1)%n==0:
        return n
    else:
        return (re+s-1)%n


print(saveThePrisoner(530, 533048047, 529))
