# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# lab1
salary = float(input("Please input your salary "))
if salary <= 0.0: # if the salary isnt valid
    print("Error, salary must be positive")
    exit()
hours = float(input("Please enter your hours"))
if hours <= 0.0: # if the hours arent valid
    print("Error, salary must be positive")
    exit()
if hours <= 40.0: # if there are regular hours
    print('You made', (hours * salary), "dollars")
elif hours >= 40.0: # if there are overtime hours
    print("You made" , (40*salary)+((hours-40)*(salary*1.5)) , "dollars")
