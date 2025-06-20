# v4 optimize from O(N^2)
# O(N) from solutions
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = 0
        curr = 1
        result = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                result += min(prev, curr)
                prev = curr
                curr = 1

        result += min(prev, curr)
        return result

# v3 optimize
# using dict it works till testcases 86/91 but TLE
# class Solution:
#     def countBinarySubstrings(self, s: str) -> int:
#         count = 0
#         for i in range(len(s) - 1):
#             d = {} # new dict for each loop
#             d[s[i]] = 1
#             switched = False
#             for j in range(i+1, len(s)):
#                 if s[i] == s[j]:
#                     if switched:
#                         break
#                     d[s[i]] += 1
#                 else:
#                     switched = True
#                     d[s[i]] -= 1
                
#                 if d[s[i]] == 0:
#                     count += 1
#                     break
#                 elif d[s[i]] < 0:
#                     break
#         return count


# v2 can be answer but it has TLE
# 1 <= s.length <= 10**5
# should be less than n**2

# class Solution:
#     def countBinarySubstrings(self, s: str) -> int:
#         count = 0
#         seen = set()
#         for i in range(len(s) - 1):
#             temp = s[i]
#             for j in range(i + 1, len(s)):
#                 if s[i] == s[j]: # 0 and 0 or 1 and 1
#                     temp += s[j]
#                 else:
#                     # if its differnent letter
#                     temp += s[j]
#                     if temp in seen or temp.count("0") == temp.count("1"):
#                         count += 1
#                         break
#         return count
        

# # this version something wrong.. keep getting wrong cases..
# class Solution:
#     def countBinarySubstrings(self, s: str) -> int:
#         # s has "0" or "1"
#         # these substrings are grouped consecutively.
#         # O(N**2)
#         # using nested loops
#         # i is the standard
#         # j can be temp[0] and flag = false
#         # j != i -> flag true and next j != i -> flag true is break
#         # break should be the smae number of 0 and 1 

#         # is will be ok with O(N**2)? for 1 <= s.length <= 10**5
#         # not sure but lets try

#         # we don't need what it is, so just count number 
#         count = 0
#         result = []

#         for i in range(len(s)):
#             temp = s[i]
#             flag = True
#             for j in range(i+1, len(s)):
#                 if temp[0] == s[j]:
#                     if flag:
#                         temp += s[j]
#                     else:
#                         break
#                 else:
#                     flag = False
#                     temp += s[j]
#             if not flag and len(temp) % 2 == 0:
#                 # gotta check count("0") == count("1")
#                 if temp.count("0") == temp.count("1"):
#                     count += 1
#                     result.append(temp)
#         print(result)
#         return count
                    

