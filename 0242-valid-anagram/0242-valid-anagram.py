from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = Counter(s)
        for t_c in t:
            if t_c not in counts:
                return False
            
            counts[t_c] -= 1
            if counts[t_c] < 0:
                return False
        return True











        hashmap = {}
        for letter in s:
            hashmap[letter] = hashmap.get(letter, 0) + 1
        
        for char in t:
            if char not in hashmap:
                return False
            
            hashmap[char] -= 1
            if hashmap[char] < 0:
                return False
            
            if hashmap[char] == 0:
                del hashmap[char]

        return True if not hashmap else False