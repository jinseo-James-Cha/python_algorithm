class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""

        len1 = len(str1)
        len2 = len(str2)

        def valid(k):
            if len1 % k or len2 % k:
                return False
            n1, n2 = len1 // k, len2 // k
            base = str1[:k]
            return str1 == n1 * base and str2 == n2 * base
        
        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""


# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
        # # str1 = t + t ....
        # # str2 = t + t....
        # # get minimum len str and compare full letters and reduce -1
        # def getGcd(lessStr: str, moreStr: str) -> str:
        #     gcd = ""

        #     # ABC 3
        #     # 3 2 1
        #     for i in range(len(lessStr) + 1, 0, -1): # 4 3 2 1 
        #         ls = lessStr[0:i]

        #         if len(moreStr) % len(ls) != 0: 
        #             continue
                
        #         updated = True
        #         for j in range(0, len(moreStr), len(ls)):
        #             if moreStr[j:j+len(ls)] != ls:
        #                 updated = False
                
        #         if updated:
        #             gcd = ls
                        
        #     return gcd

        # res = ""
        # if len(str1) > len(str2):
        #     res = getGcd(str2, str1)
        #     if res and len(str2) % len(res) == 0:
        #         res = getGcd(res, str2)
        # else:
        #     res = getGcd(str1, str2)
        #     if res and len(str1) % len(res) == 0:
        #         res = getGcd(res, str1)
        
        # return res

        

# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         # str1 = t + t ....
#         # str2 = t + t....
#         x = ""
#         i = 0
#         while len(str1) > i and len(str2) > i:
#             if str1[i] == str2[i]:
#                 x += str1[i]
#                 i += 1
#             else:
#                 break
        
#         while len(x) > 0:


#         return x