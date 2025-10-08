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
print("This program is used to check if two people like the same pet and if they like the same subject")
firstPerson = input("What is the first person you want to input?")
firstPet = None
firstSubject = None
for line in data:
    info = line.strip().split(",")
    if info[1].strip().lower() == firstPerson.strip().lower():
        firstPet = info[3].strip()
        firstSubject = info[4].strip()
        break


secondPerson = input("What is the second person you want to input?")
secondPet = None
secondSubject = None
for line in data:
    info = line.strip().split(",")
    if info[1].strip().lower() == secondPerson.strip().lower():
        secondPet = info[3].strip()
        secondSubject = info[4].strip()
        break

if firstPet == None or secondPet == None:
    print("You did not input a valid name please try again.")

elif firstPet == secondPet and firstSubject == secondSubject:
    print("You guys like the same pet and the same subject!")

elif firstPet == secondPet and not firstSubject == secondSubject:
    print("You guys like the same pet but not the same subject subject!")

elif not firstPet == secondPet and firstSubject == secondSubject:
    print("You guys do not like the same pet but like the same subject!")

elif not firstPet == secondPet and not firstSubject == secondSubject:
    print("You guys do not like the same pet and do not like the same subject!")




#Input 1: Daichi Lee
#Input 2: Theo Shim
#Output: You guys like the same pet!

#This code is used to determine if two different people you have inputted like the same pet and same subject through the data from the survey.
#1.Start by stripping out the first header line in responses.csv
#2.Then make a for loop to keep looping until it finds first inputted name
#3.Strip out the pet(index 3) and subject(index 4) make it first persons pet and subject
#4.Repeat the same steps for person two
#5.Make if statements to see if they are equal or not and print depending on results



    
