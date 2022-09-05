def alternate(s):
    s = list(s)
    t = set(s)
    l = []
    for i in range(len(t)-1):
        for j in range(i+1,len(t)):
          print(list(t)[i],list(t)[j])
s = input()
alternate(s)
