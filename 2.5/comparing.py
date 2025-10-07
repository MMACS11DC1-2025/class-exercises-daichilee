"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""




file = open("2.4/responses.csv")
file.readline()
data = file.readlines()
#i changed from sports to pet because like there is two sports in everybodys data 
print("This program is used to check if two people like the same pet")
firstPerson = input("What is the first person you want to input?")
firstPet = None
for line in data:
    info = line.strip().split(",")
    if info[1].strip().lower() == firstPerson.strip().lower():
        firstPet = info[3].strip()
        break

secondPerson = input("What is the second person you want to input?")
secondPet = None
for line in data:
    info = line.strip().split(",")
    if info[1].strip().lower() == secondPerson.strip().lower():
        secondPet = info[3].strip()
        break

if firstPet == secondPet:
    print("You guys like the same pet!")
else:
    print("You guys do not like the same pet!")

        



    
