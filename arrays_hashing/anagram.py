
# Optimized approach - Using hashmap
## TC: O(n + m)
## SC: O(1)


def is_anagram(str1: str, str2: str) -> bool:
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    
    # create list to hold counts
    counts = [0] * 26
    
    
    for char in str1:
        counts[ord(char) - ord('a')] +=1
    
    for char in str2:
        counts[ord(char) - ord('a')] -=1
        
    for count in counts:
        if count != 0:
            return False
    
    return True

# Bruteforce approach: Using sort
## TC: O(nlogn)
def is_anagram(str1: str, str2: str) -> bool:
    
        str1 = str1.lower()
        str2 = str2.lower()
        
        str1 = str1.replace(" ", "")
        str2 = str2.replace(" ", "")
        
        str1 = sorted(str1)
        str2 = sorted(str1)
        
        if str1 == str2:
            return True
        return False
