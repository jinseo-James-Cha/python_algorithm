class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        hashmap = {}
        registered = set()
        s_arr = s.split()
        if len(pattern) != len(s_arr):
            return False
            
        for p, word in zip(pattern, s_arr):
            if p in hashmap:
                if hashmap[p] != word:
                    return False
            elif word in registered:
                return False

            registered.add(word)
            hashmap[p] = word        
        return True







        # s follows the same pattern
        
        # follow -> full match
        # Each letter in pattern maps to exactly one unique word in s.
        # Each unique word in s maps to exactly one letter in pattern.

        # hashmap ? hashmap[pattern[i]] = s[i]

        # hashmap = {}
        # registered = set()
        # s_array = s.split(" ")
        # if len(pattern) != len(s_array):
        #     return False
        
        # for i, p in enumerate(pattern):
        #     if p not in hashmap:
        #         if s_array[i] not in registered:
        #             registered.add(s_array[i])
        #             hashmap[p] = s_array[i]
        #         else:
        #             return False
        #     # already registered? compare with previous
        #     elif hashmap[p] != s_array[i]:
        #         return False
        # return True
