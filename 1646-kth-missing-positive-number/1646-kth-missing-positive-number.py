class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # create res and fill up with missing num

        res = []
        for i in range(1, 2001):
            if i not in arr:
                res.append(i)
        return res[k-1]