# Exercise 8: Palindrome Checker
# 1.Create a function named is_palindrome that takes a string as a parameter and
#  returns True if it's a palindrome, otherwise False.
#  A palindrome is a word, phrase, number, or other sequence of characters 
# that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.
# 2.Demonstrate the usage of this function by checking whether the strings "radar" and "Python" are palindromes.


def  is_palindrome(word):
     if word[::-1]==word:
       print("true")
     else:
        print("false")
is_palindrome("radar")
is_palindrome("python")