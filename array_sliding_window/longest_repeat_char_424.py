import string


## Approach: sliding window
# TC: O(n)
# SC: O(1) at max 26 char hashmap
def characterReplacement(s: str, k: int) -> int:
    l = 0
    max_len = 0
    freq_count = {}
    maxf = 0
    
    for r in range(len(s)):
        freq_count[s[r]] = freq_count.get(s[r], 0) + 1
        maxf = max(maxf, freq_count[s[r]])    

        while (r-l+1)- maxf > k:
            freq_count[s[l]] -= 1
            l += 1
        
        win_size = r-l+1    
        max_len = max(max_len, win_size)
    
    return max_len
        
        
   
        


s = "ABAB"
k = 2
s = "AABABBA"
k = 1
print(characterReplacement(s,k))