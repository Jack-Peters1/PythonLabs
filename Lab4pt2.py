number = (int)(input("Please enter a number"))
numberArray = []

while number !=0: #while number is not 0
    numberArray.append(int(number%10))
    number -= number%10
    number /= 10

numberArray.reverse()
print("Your array is ", numberArray)
