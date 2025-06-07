class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = []
        for ch in s:
            if ch == '-':
                continue
            chars.append(ch.upper())

        result = []
        count = 0
        for ch in reversed(chars): #reverse chars
            if count == k:
                result.append('-')
                count = 0
            result.append(ch)
            count += 1
        return ''.join(reversed(result))

# class Solution:
#     def licenseKeyFormatting(self, s: str, k: int) -> str:
#         # s license key alphanumeric and -
#         # split("-") 
#         # first group can be <= k
#         # if more than k, we need to put - and next group
#         # ABCD-E k 2 -> AB CD E
#         # 
#         # AB-C-DE k 2 -> AB CD E
#         # 5F3Z-2e-9-w k 3 -> 5F3 - Z2e 9w

#         # 5F3-Z-2e-9-w k 3
#         # 5F3Z-2e-9-w k 4 -> 

#         # 2-4A0r7-4k k 4 -> 24A0-R74K

#         # index = 0
#         # res = ""

#         # firstDashIndex = s.index("-")
#         # if firstDashIndex <= k:
#         #     index = firstDashIndex
#         #     res += s[:index]

#         # s = s[:index] + s[index:].replace("-", "")
#         # for i in range(index, len(s), k):
#         #     res += "-" + s[i:i+k]
#         # return res.upper()


#         # s_s = s.split("-")
#         # res = ""
#         # i = 0
#         # if len(s_s[0]) <= k:
#         #     res += s_s[0].upper() + "-"
#         #     i = k + 1
        
#         # while i < len(s):

#         # had wrong idea.
#         # starting again with new concept
#         # remove all -
#         # divide by k and check the rest
#         # if rest is there it could be the len of first group
#         # if not, all same len in the group
#         res = ""
#         s = s.replace("-", "")
#         sLen = len(s)

#         firstGroupLen = sLen % k
#         if firstGroupLen:
#             res += s[:firstGroupLen]

#         for i in range(firstGroupLen, len(s), k):
#             res += "-" + s[i: i + k]
        
#         if res and res[0] == "-":
#             res = res[1:]

#         return res.upper()


        