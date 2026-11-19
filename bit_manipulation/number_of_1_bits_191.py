


## Approach:Can we have the operations run for only the 1's in the 32 bit 
# instaed of checking every bit
# TC: O(1) 
def hammingWeight(n: int) -> int:
    res = 0

    while n:
        n = n & (n-1)
        res += 1

    return res

## Optimized Approach: bit manipulation
# TC: O(32) ~ O(1)
def hammingWeight(n: int) -> int:
    res = 0

    while n:
        res += n%2
        n = n >> 1

    return res

## Approach: String conversion
# TC: O(log n)
def hammingWeight(n: int) -> int:
    n = bin(n)[2:] # decimal to binary O(log n)
    res=0

    for c in n: #O(1) - upper limit is fixed 32 bit
        res += c=='1'
        
    return res


        