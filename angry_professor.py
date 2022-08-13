def angryProfessor(k, a):
    count = 0
    for i in a:
        if i <= 0:
            count += 1
    return "YES" if count < k else "NO"


print(angryProfessor(3, [-2, -1, 0, 1, 2]))
