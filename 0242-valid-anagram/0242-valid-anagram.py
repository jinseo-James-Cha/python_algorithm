# first
# return Counter(s) == Counter(t) will work without algorithm

# s converts to Hashmap by letter = key, freq = value
# deduct freq by t by letter and if it meets 0, it returns False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {} # hashmap
        for l in s:
            counter[l] = counter.get(l, 0) + 1
        
        for l in t:
            if l not in counter or counter[l] == 0:
                return False
            else:
                counter[l] -= 1
        
        return True



# my poor answer
# from collections import Counter

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if not len(s) == len(t):
#             return False

#         s_c = Counter(s)
#         t_c = Counter(t)

#         for k, v in s_c.items():
#             if not k in t_c:
#                 return False
#             elif not s_c[k] == t_c[k]:
#                 return False
        
#         return True