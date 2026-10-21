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

## Approach - two pointer, optimizing it by avoiding unnecessary iterations
# TC: O(n^2)
# SC: O(1)
def three_sum(nums: list[int])->list[list[int]]:
    if len(nums)<3:
        return []
    
    nums.sort()
    print(nums)
    
    result = []
    
    
    for i, a in enumerate(nums):
        if a>0:
            print(f"i am out with i as{i} and a as {a}")
            break
        elif i>0 and a==nums[i-1]:
            continue
        
        left = i+1
        right = len(nums) - 1
        
        while left < right:
            
            target = nums[i] + nums[left] + nums[right]
            
            if target==0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left-1] and left<right:
                    left += 1
                
            elif target < 0:
                left += 1
                
            elif target > 0:
                right -= 1
        
    return result
    
nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))