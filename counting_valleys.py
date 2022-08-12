def countingValleys(steps, path):
    sum = 0
    count = 0
    for i in range(0, steps):

        if path[i] == 'U':
            sum+=1
        elif path[i] == 'D':
            sum = sum - 1
        if sum == 0 and path[i] == 'U':
            count+=1

    return count



print(countingValleys(8,'UDDDUDUU'))
