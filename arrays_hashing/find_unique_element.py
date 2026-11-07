## Brute force would be O(n^2), verifing status of uniqueness for each element traversing through remaining list


## Using a Hash Map (Dictionary) to find elements that appear exactly once in the array
# TC: went over array twice O(n + m) ~ O(N)
# SC: O(n)
def finding_unique(nums:list[int]) -> int:
    counts = dict()
    
    for num in nums:
        counts[num] = 1 + counts.get(num, 0)
        
    for num in counts:
        if counts[num] == 1:
            return num
        
    return -1




nums = [1, 2, 7, 9, 0, 1, 6, 7, 8, 9, 8, 0, 2]
print(finding_unique(nums))