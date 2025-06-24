# v2 : O(logN)
# the sorted input should ring the bell -> Binary Search
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2

            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid - 1

        return left + k

# O(N)
# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:
#         # create res and fill up with missing num

#         res = []
#         for i in range(1, 2001):
#             if i not in arr:
#                 res.append(i)
#         return res[k-1]