
numberOne = float(input("Please enter a number"))
operator = str(input("Please enter an operator"))
numberTwo = float(input("Please enter a number"))

thisdict = {
    "+": numberOne + numberTwo,
    "-": numberOne - numberTwo,
    "*": numberOne * numberTwo,
    "/": numberOne / numberTwo,
    "^": numberOne ** numberTwo,
    "%": numberOne % numberTwo,
}
if thisdict.get(operator) == None: # if the operator is invalid print and exit
    print("ERROR," , operator , "is not a valid operator")
    exit()
answer = thisdict.get(operator)
print(numberOne, operator ,numberTwo, " = ", answer)


