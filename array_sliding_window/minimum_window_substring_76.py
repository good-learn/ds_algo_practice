"""Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t (including duplicates) 
is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.


Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
"""



## Approach: sliding window, hashmaps
# TC: O(n)
def min_win_sbstring(s:str, t:str)->str:
    if t=="": return ""
    
    char_counts_t, window = {}, {}
    
    for c in t:
        char_counts_t[c] = char_counts_t.get(c, 0) + 1
        
    actual, expected = 0, len(char_counts_t)
    l = 0
    res_idx, res_len = [-1, -1], float("infinity")
    
    for r in range(len(s)):
        c = s[r]
        window[c] = window.get(c, 0) + 1
        
        if c in char_counts_t and window[c] == char_counts_t[c]:
            actual += 1
            
        while actual == expected:
            if(r - l +1) < res_len:
                res_idx = [l, r]
                res_len = r-l +1
            window[s[l]] -=1
            if s[l] in char_counts_t and window[s[l]] <char_counts_t[s[l]]:
                actual -= 1
            l+=1
    
    l, r = res_idx
    
    return s[l:r+1] if res_len != float("infinity") else ""
                
                
s = "ADOBECODEBANC"
t = "ABC"
print(min_win_sbstring(s, t))