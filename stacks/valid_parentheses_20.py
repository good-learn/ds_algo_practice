"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true"""


## Approach: Using stack (last in first out) thats the way we follow valid brackets
# TC: O(n)
# SC: O(n)
def isValid(s: str) -> bool:
    stack = []

    # map of closing bracktes
    bracket_map = {')':'(', '}':'{', ']':'['}

    # loop over the expression or characters
    for c in s:
        if c in bracket_map:
            if stack and stack[-1] == bracket_map[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return not stack

s = "()"
s = "()[]{}"
s = "(]"
print(isValid(s))
        