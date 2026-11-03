def longest_sbstring(s: str) -> int:
    max_len = l = 0
    charSet = set()

    
    #expanding right to increase the window size
    for r in range(len(s)):
        
        # shrinking left to get rid of duplicate
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
            
        charSet.add(s[r])
        max_len = max(max_len, r-l +1)

    return max_len



## Optimize with use of enumerator - With enumerate(), Python uses the iterator protocol (__next__). 
# It simply asks the underlying iterator for the next element, 
# which avoids index-based lookup overhead entirely.
# TC:O(n)
# SC:O(n)
def longest_sbstring(s: str) -> int:
    max_len = l = 0
    charSet = set()

    
    #expanding right to increase the window size
    for r, c in enumerate(s):
        
        # shrinking left to get rid of duplicate
        while c in charSet:
            charSet.remove(s[l])
            l+=1
            
        charSet.add(c)
        max_len = max(max_len, r-l +1)

    return max_len



## Using while loop 
# TC: O(n)
# SC: O(n)
def longest_sbstring(s: str) -> int:
    max_len = l = r = 0
    charSet = set()
   
    while r<len(s):  
        #expanding right to increase the window size
        if s[r] not in charSet:
             charSet.add(s[r])
             max_len = max(max_len, r-l +1)
             r += 1
        else:  # shrinking left to get rid of duplicate
            charSet.remove(s[l])
            l+=1        
        
    return max_len





            

s = "abcweccbdf"
s = "abcabcbb"
s = "pwwkew"
print(longest_sbstring(s))