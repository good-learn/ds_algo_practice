"""
Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.
"""

#nums = [1,2,3,1]
nums = [1,2,3,4]




# Optimized - using set 
## TC: O(n)
## SC: O(n)
def containsDuplicate(nums: list[int]) -> bool:
    
    myset = set()
    
    for num in nums:
        if num in myset: # O(1)
            return True
        myset.add(num)
    return False


print(containsDuplicate(nums))

# Optimized - using dictionary 
## Note set consumes less space than dictionary 
## TC: O(n)
## SC: O(n)
def containsDuplicate(nums: list[int]) -> bool:
    
    hashset = {}
    
    for num in nums:
        if num in hashset: # O(1)
            return True
        hashset[num] = hashset.get(num, 0) + 1
    return False


print(containsDuplicate(nums))


# Brute force - using for loops
# TC: O(n^2)
# SC: O(1)
def containsDuplicate(nums: list[int]) -> bool:
    
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

print(containsDuplicate(nums))