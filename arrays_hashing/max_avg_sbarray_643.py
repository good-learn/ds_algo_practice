"""You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value 
and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75"""

## SLiding window (two pointer)
# TC: O(n)
# SC: O(1)
def max_avg_subarray(nums:list[int], k:int)->float:
    sum, max_sum = 0, 0
    
    for i in range(k):
        sum += nums[i]
    
    max_sum = sum
    
    left = 0
    right = k
    
    while right < len(nums):
        
        sum -= nums[left]
        left +=1
        
        sum += nums[right]
        right+=1
        
        max_sum = max(sum, max_sum)
    
    return max_sum/k


nums = [1, 12, -5, -6, 50, 3]
print(max_avg_subarray(nums, k=4))