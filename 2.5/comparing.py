"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""


#comments at bottom

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
elif firstPet != secondPet:
    print("You guys do not like the same pet!")

else:
    print("You did not input a valid name. Please try again.")


#Input 1: Daichi Lee
#Input 2: Theo Shim
#Output: You guys like the same pet!

#This code is used to determine if two different people you have inputted like the same pet through the data from the survey.
#1.Start by stripping out the first header line in responses.csv
#2.Then make a for loop to keep looping until it finds first inputted name
#3.Strip out the pet(index 3) and make it first persons pet
#4.Repeat the same steps for person two
#5.Make if statements to see if they are equal or not and print depending on results



    
