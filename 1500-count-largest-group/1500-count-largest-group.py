class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashMap = {}
        for i in range(1, n + 1):
            key = sum([int(x) for x in str(i)])
            hashMap[key] = hashMap.get(key, 0) + 1
        maxValue = max(hashMap.values())

        # this is the kick
        # sum(1 for v in hashMap.values() if v == maxValue)
        count = sum(1 for v in hashMap.values() if v == maxValue)
        return count

# class Solution:
#     def countLargestGroup(self, n: int) -> int:
#         # according to the sum of its digits -> group 1 ~ n
#         ans = {}

#         for i in range(1, n+1):
#             size = 0
#             temp = 0
#             while i > 0:
#                 temp += i % 10
#                 i //= 10
#                 size +=1
#             ans[size] = ans.get(size, 0) + 1
        
#         k, v = max(ans.items(), key= lambda x:x[0])
#         return v


