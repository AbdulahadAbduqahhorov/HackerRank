def utopianTree(n):
    h = 1
    for i in range(n):
        if i%2==1:
            h = h+1
        else:
            h = h*2
    return h

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)
        print(result)
