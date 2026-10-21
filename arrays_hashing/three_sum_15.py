"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""

## Approach - two pointer
# TC: O(n^2)
# SC: O(1)
def three_sum(nums: list[int])->list[list[int]]:
    if len(nums)<3:
        return []
    
    nums.sort()
    
    result = set()
    
    
    for i in range(len(nums)-2):
        
        left = i+1
        right = len(nums) - 1
        
        while left < right:
            
            target = nums[i] + nums[left] + nums[right]
            
            if target==0:
                result.add(( nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
                
            elif target < 0:
                left += 1
                
            elif target > 0:
                right -= 1
        
    return list(map(list, result))
    
nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))