def pangrams(s):
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    for i in alphabet:
        if i not in s.lower():
            return 'not pangram'

    return 'pangram'



if __name__ == '__main__':
    s = input()

    result = pangrams(s)

    print(result)
