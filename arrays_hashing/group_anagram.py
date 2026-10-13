
"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

strs = ["eat","tea","tan","ate","nat","bat"]

## optimized - using hash map
## TC: O(m * n) m:len(strs) and n is average word len 
## SC: O(m)
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = {}
    
    for word in strs:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1
        if tuple(count) not in res:
            res[tuple(count)] = []       
        res[tuple(count)].append(word)
    
    return list(res.values())
    
print(groupAnagrams(strs))



from collections import defaultdict

## optimized - using collection default dict - same as above
## TC: O(m * n) m:len(strs) and n is average word len 
## SC: O(m)
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = defaultdict(list)
    
    for word in strs:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord('a')] += 1
        #print(count)
        
        res[tuple(count)].append(word)
    
    return list(res.values())
    
print(groupAnagrams(strs))

## brute force - using sorting
## TC: O(m * nlogn)
## SC: O(m)
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res = {}
    
    for word in strs: # O(m)
        sorted_word = ''.join(sorted(word))  # O(nlogn)
        if sorted_word not in res:
            res[sorted_word] = []       
        res[sorted_word].append(word)
    
    return list(res.values())
    
print(groupAnagrams(strs))


