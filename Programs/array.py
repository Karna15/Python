from array import *

array1 = array('i', [10,11,12,13,14,15])

for i in array1:
    print(i)

print("1st index = ", array1[0])

array1.insert(1,9)

print("1st index after insert = ", array1[1])


