class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        # distinct intergers in asceding order
        # arr[i] == i return i or -1

        # arr[i]


        for i, n in enumerate(arr):
            if n < 0:
                continue

            if i == n:
                return i


        return -1