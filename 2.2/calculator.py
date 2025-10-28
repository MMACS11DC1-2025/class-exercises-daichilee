#Daichi Lee 
#Calculates addition and subtraction of two numbers
print("This is a tool to calculate the addition or subtraction of two numbers.")
print("Please enter the first number")
numberOne = input()
print("Please enter the second number")
numberTwo = input()
print("Please enter the operation you want(type addition or subtraction)")
operation = input()

if operation == "addition":
    calc = float(numberOne) + float(numberTwo)
    print(str(calc))
elif operation == "subtraction":
    calc = float(numberOne) - float (numberTwo)
    print(str(calc))
else:
    print("Error")
