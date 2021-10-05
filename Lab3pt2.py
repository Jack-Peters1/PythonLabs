
def positiveYears(population): #calculate for population in future
    years = 1990
    startingPopulation = 89.2
    while startingPopulation<population:
        startingPopulation = startingPopulation * 1.023
        years+=1
    return years, startingPopulation


def negativeYears(population): #calculate for population in past
    years = 1990
    startingPopulation = 89.2
    while startingPopulation>population:
        startingPopulation = startingPopulation / (1.023)
        years-=1
    return years, startingPopulation

population = int(input("Please enter population"))

if population<89.2: # if population is in the past
    year, pop = negativeYears(population)
    print("Pop in year:", year, "is equal to: ", pop, " million")
elif population>89.2: # if population is in future
    year, pop = positiveYears(population)
    print("Pop in year:", year, "is equal to: ", pop,  " million")