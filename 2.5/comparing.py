"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""




file = open("2.4/responses.csv")
data = file.readlines()

print("This program is used to check if two people like the same sport")
firstPerson = input("What is the first person you want to input?")
firstSport = None
for line in data[1:]:
    info = line.strip().split(",")
    if info[1].strip().lower() == firstPerson.strip().lower():
        firstSport = info[4].strip()
        break

secondPerson = input("What is the second person you want to input?")
secondSport = None
for line in data[1:]:
    info = line.strip().split(",")
    if info[1].strip().lower() == secondPerson.strip().lower():
        secondSport = info[4].strip()
        break

if firstSport == secondSport:
    print("You guys like the same sport!")
else:
    print("You guys do not like the same sport!")

        



    
