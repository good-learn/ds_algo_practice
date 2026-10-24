


## Optimized solution
# TC: O(n)
def topKFrequent(nums: list[int], k: int) -> list[int]:
    
    if len(nums) == 1:
        return [1]
    count = {}
    
    # count frequency
    for num in nums: #O(n)
        count[num] = count.get(num, 0) + 1
    
    
    #bucket = [[]]* len(nums) # dont do this mistake, all inner list points to same object, appending to one will append to all of them
    #create bucket using list comprehension, inner list will distinct
    bucket = [[] for _ in range(len(nums) + 1)] # =1 is an adjustment to have bucket index 1 refer to freq of 1
    
    # filling bucket    
    for key, val in count.items(): #O(n)
        bucket[val].append(key)        

    
    
    my_list = []

    for item in bucket[::-1]: #O(n)
        if item:
            for i in item:
                if (len(my_list)==k):
                    break
                my_list.append(i)
                
    return my_list


nums = [1,1,1,2,2,3, 3, 3, 3, 3, 5, 5,5 ,5] 
#nums = [1,1] 
#nums = [1,2,1,2,1,2,3,1,3,2]

k = 2
    
print(topKFrequent(nums, k))