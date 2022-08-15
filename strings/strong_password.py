def minimumNumber(n, password):
    special_characters = "!@#$%^&*()-+"
    nu = 0
    l = 0
    u = 0
    s = 0
    for i in password:
        if i.isnumeric():
            nu = 1
        elif i.islower():
            l = 1
        elif i.isupper():
            u = 1
        elif i in special_characters:
            s = 1

    count = 4 - l - u - s - nu
    if n + count < 6:
        return 6 - n
    else:
        return count


if __name__ == '__main__':
    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)
    print(answer)
