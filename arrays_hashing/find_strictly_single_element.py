## Brute force would be O(n^2), verifing status of uniqueness for each element traversing through remaining list


## Using a Hash Map (Dictionary) to find elements that appear exactly once in the array
# TC: went over array twice O(n + m) ~ O(N)
# SC: O(n)
def finding__strictly_single_elements(nums:list[int]) -> list[int]:
    counts = dict()
    
    single_elements = []
    
    for num in nums:
        counts[num] = 1 + counts.get(num, 0)
    
    print(counts)    
    for num in counts:
        if counts[num] == 1:
            single_elements.append(num)
    return single_elements




nums = [1, 2, 7, 9, 0, 1, 6, 7, 8, 9, 8, 0, 2]
print(finding_unique(nums))