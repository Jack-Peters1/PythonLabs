
def positiveYears(finalPopulation): # calculate if the years are in the future
    for x in range(years):
        finalPopulation = finalPopulation * 1.023
    return finalPopulation


def negativeYears(finalPopulation): # calculate if the years are in the past
    for x in range(years * -1):
        finalPopulation = finalPopulation / (1.023)
    return finalPopulation

years = int(input("Please enter number of years:"))
finalPopulation = 89.2

if years < 0: #if years are negative, calculate else then go positive
    print("The population of mexico in year: ", 1990+years, "was ", negativeYears(finalPopulation), " million")
elif years >= 0:
    print("The population of mexico in year: ", 1990+years, "is ", positiveYears(finalPopulation), " million")


