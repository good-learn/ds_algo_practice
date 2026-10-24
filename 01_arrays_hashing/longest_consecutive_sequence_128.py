"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

# Using set
## TC : O(n) 
## SC: O(1)
def longestConsecutive(nums: list[int]) -> int:
    nums_set = set(nums)
    max_len = 0
    
    for num in nums_set:
        
        
        if num -1 not in nums_set:
            cur_len = 1
            
            while num + cur_len in nums_set:
                cur_len+=1
            
            max_len = max(cur_len, max_len)
    
    return max_len


nums = [100,4,200,1,3,2]       
nums = [1, 7, 24, 8, 12, 0, 9]
print(longestConsecutive(nums))        
    



# Using hashmap - in this approach, we tracking in both forward and backward direction. the first set approach is simple
## TC : O(n) 
## SC: O(1)
def longestConsecutive(nums: list[int]) -> int:
    
    num_dict = {}
    
    for num in nums:
        num_dict[num] = False
        
    max_len = 0
        
    for num in nums:
        cur_len = 1
        
        next = num + 1
        while next in num_dict and not num_dict[next]:
            cur_len +=1
            num_dict[next] = True
            next += 1
        
        prev = num - 1
        while prev in num_dict and not num_dict[prev]:
            cur_len += 1
            num_dict[prev] = True
            prev -= 1
            
        
        max_len = max(cur_len, max_len)
    
    return max_len       
            
        

print(longestConsecutive(nums))
        