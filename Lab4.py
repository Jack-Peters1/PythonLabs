import random

array1 = []
for i in range(10): #fill array
    array1.append(random.randint(1,20))

print(array1)
mean = 0
smallest = array1[0]
for x in array1: #calculate mean
    mean +=x
    if x<smallest: #get smallest
        smallest = x
print("The mean is ", mean/10, "\n","The smallest value is: ", smallest, "\n","The smallest value is at index: ", array1.index(smallest))


