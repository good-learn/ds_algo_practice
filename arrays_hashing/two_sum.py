"""
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

# Optimized approach
## using hashset/dict, look up is O(1), insert is O(1)
## TC: O(n)
def twoSum(nums: list[int], target: int) -> list[int]:
    mydict = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        # if mydict.get(complement) - i used this earlier, but look in this example, it returns a 0 value, which evaluates the expression to be false, eventhough the expression return actual value.
        if complement in  mydict:
            return [mydict[complement], i]
        
        mydict[nums[i]] = i

# nums = [2,7,11,15]
# target = 9
nums = [3,2,4]
target = 6
print(twoSum(nums, target))



# Brute force - Using for loop
## Time complexity - O(n^2)
def twoSum(nums: list[int], target: int) -> list[int]:

    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# nums = [2,7,11,15]
# target = 9
nums = [3,2,4]
target = 6
print(twoSum(nums, target))