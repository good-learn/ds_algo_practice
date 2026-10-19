

## Optimized aaproach
# TC: O(n)
# SC: O(n)
nums = [1, 2,3, 4]
def array_product_except_self(nums:list[int])->list[int]:
    
    n = len(nums)
    
    l_arr = [1] * n
    for i in range(1, n):
        l_arr[i] = l_arr[i-1] * nums[i-1]
    
    r_arr = [1] * n
    for i in range(n-2, -1, -1):
        r_arr[i] =r_arr[i+1] * nums[i+1]
    
    product_arr = [1]*len(nums)
    for i in range(len(nums)):
        product_arr[i] = l_arr[i] * r_arr[i]

    return product_arr


nums = [1, 2,3, 4]
nums = [-1,1,0,-3,3]
# [24, 12, 8, 6]
print(array_product_except_self(nums))


## Similar solution but solved with effeicnt Space complexity
def array_product_except_self(nums:list[int])->list[int]:
    product_arr = [1] * len(nums)
    l_arr = []
    
    # prepare l_arr
    l_arr.append(1)
    product=1
    for i in range(len(nums)-1):
        product *= nums[i]
        l_arr.append(product)

    
    
    product_arr[-1] = product_arr[-1] * l_arr[-1]
    product=1
    for j in range(len(nums)-1, 0, -1):
        product *= nums[j]
        product_arr[j-1] =product * l_arr[j-1]

    
    return product_arr

nums = [1, 2,3, 4]
nums = [-1,1,0,-3,3]
# [24, 12, 8, 6]
print(array_product_except_self(nums))
