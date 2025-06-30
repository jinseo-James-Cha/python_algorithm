from collections import Counter
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        def can_build(num_str, digit_counter):
            temp_counter = digit_counter.copy()  # Cheap shallow copy
            for ch in num_str:
                d = int(ch)
                if temp_counter[d] == 0:
                    return False
                temp_counter[d] -= 1
            return True

        digit_counter = Counter(int(d) for d in digits)  # Create once
        res = []
        for i in range(100, 1000, 2):  # Only 3-digit even numbers
            s_i = str(i)
            if can_build(s_i, digit_counter):
                res.append(i)
        return res

# from collections import Counter
# class Solution:
#     def findEvenNumbers(self, digits: List[int]) -> List[int]:
#         # may contain duplicates
        
#         # find all unique 
#         # 1. concatenation of three elements 
#         # 2. no leading zero
#         # 3. even number only
#         # return sorted array
        
#         # 1, "2", 3 -> 2 is only even, so 132 312 len == 2
#         # "2" 1 3 "0" -> [102,120,130,132,210,230,302,310,312,320] len == 10
#         # 3 7 5 -> [] 0
        
#         c = Counter(digits)   
#         res = []
#         for i in range(100, 999, 2):
#             s_i = str(i)
#             matching_count = 0
#             temp_c = c.copy()
#             for a in s_i:
#                 if int(a) not in temp_c:
#                     break
#                 else:
#                     if temp_c[int(a)] == 0:
#                         break

#                     matching_count += 1
#                     temp_c[int(a)] -= 1
#             if matching_count == 3:
#                 res.append(int(s_i))
#         return res
                

