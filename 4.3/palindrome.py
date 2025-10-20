"""
Palindrome Checker (recursive)
20 October 2025
Jordan Chin
"""

def palindromeHelper(word, start, end):
    # If our left bound is at or past the right bound, we know we checked everything and
    # therefore we have a palindrome
    if start >= end:
        return True
    # If our characters don't match, we have proof we don't have a palindrome
    if word[start] != word[end]:
        return False
    # If we found characters that matched, we have to check the next characters inwards
    return palindromeHelper(word, start + 1, end - 1)

def isPalindrome(word):
    # Check whether word is a palindrome, starting by comparing
    # first character and last character
    return palindromeHelper(word, 0, len(word) - 1)

# Run the function on various words, a mix of palindromes and non-palindromes
for word in ["pop", "racecar", "peep", "peep", "PEPPER", "palindrome"]:
    print("Is " + word + " a palindrome? " + str(isPalindrome(word)))

import turtle

def draw_tree(level, branch_length):
    if level > 0:
        turtle.forward(branch_length)

        turtle.left(40)
        draw_tree(level-1, branch_length/1.61)

        turtle.right(80)
        draw_tree(level-1, branch_length/1.61)

        turtle.left(40)
        turtle.back(branch_length)

    else:
        turtle.color("green")
        turtle.stamp()
        turtle.color("brown")

turtle.speed(0)
turtle.penup()
turtle.goto(0, -180)
turtle.left(90)
turtle.pendown()

turtle.color("brown")
turtle.width(3)
turtle.shape("triangle")

drawTree(2, 120)


