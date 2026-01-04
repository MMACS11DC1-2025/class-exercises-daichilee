"""
Palindrome Checker
20 October 2025
Jordan Chin
"""

################################################
# Part 1 - Palindrome checker as single-use code
################################################
word = "racecar"
isPalindrome = True
for i in range(int(len(word) / 2)): # i gets a value from 0 to (len(word) / 2) - 1
    start_index = i
    # the last index is length of input minus one. Subtract i to get the ending index of where we are currently checking
    end_index = len(word) - 1 - i
    if word[start_index] != word[end_index]:
        # We found "evidence" that the word is not a palindrome, so 
        isPalindrome = False
        break
print("Is " + word + " a palindrome? " + str(isPalindrome))

################################################
# Part 2 - Palindrome checker as a function
################################################

def checkPalindrome(word):
    # Assume the word is a palindrome. Check the start and end characters.
    # If they don't match, we know it's not a palindrome
    # Otherwise, we need to continue, checking the second character and second last character, etc
    # Once we reach halfway through the list, we can stop checking, since we're looking at letters in pairs (sets of 2)
    for i in range(int(len(word) / 2)):
        if word[i] != word[len(word) - 1 - i]:
            # We found "evidence" that the word is not a palindrome, so we can return the result immediately
            return False
    return True

# 2) Using the palindromeCheck() function
# Run the function on various words, a mix of palindromes and non-palindromes
for word in ["pop", "racecar", "peep", "peep", "PEPPER", "palindrome"]:
    print("Is " + word + " a palindrome? " + str(checkPalindrome(word)))