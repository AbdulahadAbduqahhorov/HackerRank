from array import array
from logging.config import valid_ident
from operator import le


arr = [3,4,7,5,6,2,1]

for i in range(1,len(arr)):
    value = arr[i]
    hole = i
    while hole>0 and value<arr[hole-1]:
        arr[hole]=arr[hole-1]
        hole = hole-1
    arr[hole] = value
    print(arr) 

