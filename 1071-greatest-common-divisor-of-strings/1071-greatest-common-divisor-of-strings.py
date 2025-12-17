class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
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


        # t divides s 
        # s = t + t + t ....     
        # if len(str2) > len(str1):
        #     str1, str2 = str2, str1

        # res = ""
        # for i in range(len(str2), 0, -1): # 4, 3, 2, 1
        #     if len(str1) % i == 0: # 6 % 2 == 0:
        #         flag = True
        #         for j in range(0, len(str1), i): # 0, 6, 2
        #             if str1[j:j+i] != str2[:i]:
        #                 flag = False
        #         if flag:
        #             return str2[:i]
        # return ""
