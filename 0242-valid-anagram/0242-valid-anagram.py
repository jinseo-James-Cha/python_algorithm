class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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