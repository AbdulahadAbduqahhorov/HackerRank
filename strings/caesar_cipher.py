def caesarCipher(s, k):
    r = ""
    for i in s:

        if i.isupper():
            r += chr((ord(i) - 65 + k) % 26 + 65).upper()
        elif i.islower():
            r += chr((ord(i) - 97 + k) % 26 + 97)

        else:
            r += i
    return r



if __name__ == '__main__':
    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)
