"""Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted."""


## Using hashset
# TC: O(n)

def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
  
    seen = set(nums1)
    result = []
    
    for num in nums2:
        if num in seen: 
            result.append(num)
            seen.remove(num) 
    return result


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))



# Using hashset
# TC: n:len(nums1), m:len(nums2), if n<m then O(n), else O(m)
def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    
    nums = set()
        
    if len(nums1)<len(nums2):
        for num in nums1:
            if num in nums2: nums.add(num)
    else:
        for num in nums2:
            if num in nums1: nums.add(num)
        
    return list(nums)

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))





