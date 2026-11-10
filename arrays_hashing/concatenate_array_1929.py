"""Given an integer array nums of length n, 
you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] 
for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.

Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]"""


## Brute force - for loop, new list created
## TC: O(2n) ~ O(n)
## SC: O(2n)
def getConcatenation(nums: list[int]) -> list[int]:
    
    ans = []
    
    for _ in range(2):
        for i in nums:
            ans.append(i)
            
    return ans

nums = [1,2,1]
print(getConcatenation(nums))


## Brute force - new list created
## TC: O(n * k) k is the times
def getConcatenation(nums: list[int]) -> list[int]:           
    return nums * 2

nums = [1,2,1]
print(getConcatenation(nums))

## Brute force - extend does inplace, no new list created so only SC is the extended
## TC: O(n) k is the times
def getConcatenation(nums: list[int]) -> list[int]: 
    nums.extend(nums) # or nums += nums
    return nums
nums = [1,2,1]
print(getConcatenation(nums))