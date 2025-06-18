# v2 : with simpler code
# fixed sliding window
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s = len(s)
        len_p = len(p)

        array_p = [0] * 26
        for a in p:
            array_p[ord(a) - ord("a")] += 1

        window = [0] * 26 # cuz lowercase alphabets only
        res = []
        left = 0
        for right in range(len_s):
            window[ord(s[right]) - ord("a")] += 1
            
            if right - left + 1 == len_p:
                if window == array_p:
                    res.append(left)
                
                # removing current value
                window[ord(s[left]) - ord("a")] -= 1
                # move left
                left +=1
            right +=1
        return res


# from collections import defaultdict
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         # fixed sliding window !
#         res = []     

#         # edge case
#         if len(p) > len(s):
#             return res

#         # check characters from p
#         # I will use dict == sliding window dict -> True
#         dict_p = defaultdict(int)
#         for a in p:
#             dict_p[a] += 1
        
#         # initial sliding window
#         sliding_window = defaultdict(int)
#         for i in range(len(p)):
#             sliding_window[s[i]] += 1
        
#         if dict_p == sliding_window:
#             res.append(0)

#         # start loop for sliding window without initial setting
#         left = 0
#         for right in range(len(p), len(s)): # left 1, right 3
#             # move window 
#             # move sliding window
#             if sliding_window[s[left]] == 1:
#                 # Remove left letter
#                 # 0 -> removed
#                 # cannot remove without number check cuz can have duplicates
#                 # that is why using dict and its count numbers
#                 del sliding_window[s[left]]
#             else:
#                 sliding_window[s[left]] -= 1
#             # remove previous value and move right
#             left += 1

#             # add right value into window   
#             sliding_window[s[right]] += 1

#             if sliding_window == dict_p:
#                 res.append(left)
            
#         return res
                    
