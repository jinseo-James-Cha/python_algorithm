class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        # distinct intergers in asceding order
        # arr[i] == i return i or -1

        # v2 Binary search
        left = 0
        right = len(arr) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == mid:
                res = mid
                right = mid - 1
            elif arr[mid] < mid:
                left = mid + 1
            else:
                right = mid - 1

        return res
        # v1
        # for i, n in enumerate(arr):
        #     if n < 0:
        #         continue
        #     if i == n:
        #         return i
        # return -1