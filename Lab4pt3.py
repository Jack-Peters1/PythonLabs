import random
array1 = []
array2 = []
array3 = []
for i in range(10): # fill arrays
    array1.append(random.randint(1,20))
    array2.append(random.randint(1,20))
array1.sort()
array2.sort()
i = 0
j = 0
print(array1)
print(array2)
while len(array1)>0 and len(array2)>0 : # while arrays are not full
    if(array1[i]<=array2[j]): # if element from array 1 is smaller then array 2, add it
        array3.append(array1[i])
        if(len(array1)>0):#out-of-bounds check
            array1.pop(i)
    elif(array2[j]<=array1[i]): # if element from array 2 is smaller then array 1, add it
        array3.append(array2[j])
        if(len(array2)>0): #out-of-bounds check
            array2.pop(j)
if(len(array1)>0): #check for any leftover values
    for x in range(len(array1)):
        array3.append(array1[x])
elif(len(array2)>0): #check for any leftover values
    for x in range(len(array2)):
        array3.append(array2[x])
print(array3)
