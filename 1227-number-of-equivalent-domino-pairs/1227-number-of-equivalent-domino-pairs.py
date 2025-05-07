# Pair Map : O(n)
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        m = [0] * 100
        count = 0
        for a, b in dominoes:
            key = a * 10 + b if a <= b else b * 10 + a
            count += m[key]
            m[key] += 1
        return count

# O(n^2) - Brute Force
# TLE - 1 <= dominoes.length <= 4 * 10^4

# class Solution:
#     def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
#         count = 0
#         for i in range(len(dominoes) - 1):
#             a,b = dominoes[i]
#             for j in range(i+1,len(dominoes)):
#                 c,d = dominoes[j]
#                 if (a == c and b == d) or (a == d) and (b == c):
#                     count += 1
#         return count

        