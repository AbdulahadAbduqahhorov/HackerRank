
def pageCount(n, p):
    # Write your code here
    f = p//2
    if n%2==0:
        if (n - p) % 2 == 0:
            l = (n - p) / 2
        else:
            l = (n - p + 1) / 2
    else:
        l = (n-p)//2
    if l>=f:
        return f
    else:
        return l
print(pageCount(4,4))