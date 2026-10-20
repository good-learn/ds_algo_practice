"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
"""
# Approaches and tips
## you can use reversing the string and then compare it
## use two pointer method to compare char by char
## for filtering string - you can use regex(TC: close to linear, worst is exponential) or if condtionals(linear)
## remember to lower case before comparison

## Optimized approach - Two pointer and conditional
# TC: O(n)
# SC: O(1)
def validate_palindrome(s:str)->bool:
    
    left = 0
    right = len(s) -1
    
    while left<=right:
        
        while left<right and (not s[left].isalnum()):
            left += 1
        
        while left < right and (not s[right].isalnum()):
            right -= 1
            
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    return True
            



s = "racecar"
s = "A man, a plan, a canal: Panama"
print(validate_palindrome(s))



## using regex for filtering out non alpha nums

import re
def isPalindrome(s: str) -> bool:

        if len(s)==0 or len(s)==1:
            return True

        s = s.lower()
        s = re.sub(r"[^A-Za-z0-9]", "", s)


        left, right = 0, len(s)-1

        while left<=right:
            if s[left]!=s[right]:
                return False
            left += 1
            right -= 1
        
        return True


s = "racecar"
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))


## using reverse concept:

def isPalindrome(s: str) -> bool:

        if len(s)==0 or len(s)==1:
            return True

        s = s.lower()
        s = re.sub(r"[^A-Za-z0-9]", "", s) # O(n)
        
        return s == s[::-1] # O(n)



s = "racecar"
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))