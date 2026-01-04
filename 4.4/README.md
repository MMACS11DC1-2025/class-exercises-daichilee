I started this code trying to make recursive patterns using function draw_square that uses a simple for loop to rotate a line 90 degrees 4 times.

I also made a user input num_squares to get how many squares between 1-1000 the user would want to draw. There is also other cases supported EG: not a number or ""

Next, I made a recursive function called recursive that keeps calling function draw square but instead increase its size every time until it stops at base case 0.

Next is I made a list of colors the user can input to change color of the design. There are other cases set in place. EG: user inputs a color not supported it will keep asking them to re-enter a valid color.

Lastly, I added variable numRecursion that adds one every time it is ran in the function recursive so total recursion calls can be printed at the end of the program.

Changed numRecursion logic to match criteria of returning value. Adds 1+ recursive call to do the same thing

Changed settings into a dictionary to make it easier to read and fufill criteria. also made it non case sensitive for color inputs
EXAMPLE CASES:

How many squares to draw? Default is 1:  12
You inputted 12
What color do you want the squares? Default is blue:  turquoise
('Invalid color! Valid colors are:', ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'black', 'white'])
What color do you want the squares? Default is blue:  blue
DRAWING:
Total recursive calls: 12

How many squares to draw? Default is 1:  10234
You inputted 1000
What color do you want the squares? Default is blue:  orange
DRAWING:
Total recursive calls: 1000

How many squares to draw? Default is 1:  -1
You inputted 1
What color do you want the squares? Default is blue:  yellow
DRAWING:
Total recursive calls: 1

Thoughts:
Minimum depth should be atleast greater than 50 recursions to see a meaningful design. However my minimum is set to 1 and max is set to 1000 if user wants to play around.
Peer review done by Marko.
