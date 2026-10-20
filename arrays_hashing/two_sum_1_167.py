"""
You are given a 1-indexed array of integers numbers that is already sorted in non-decreasing order.
Find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers index1 and index2 as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
"""


## Two pointer approach. Note the array is sorted and hence we can make use of two pointer
# TC: O(n)
# SC: O(1)

def twoSum(nums:int, target:int)->list[int]:
    
    left, right = 0, len(nums)-1
    
    while left<=right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left+1, right+1]
        
        if current_sum > target:
            right -= 1
            
        if current_sum < target:
            left += 1
            
    return []


numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))

numbers = [2,3,4]
target = 6
print(twoSum(numbers, target))

numbers = [-1,0]
target = -1
print(twoSum(numbers, target))