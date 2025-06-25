class Solution:
    def check(self, nums: List[int]) -> bool:
        # true -> ASC order and rotate some number of positions
        # binary search to find x > x + 1
        # B[i] == A[(i+x) % A.length]
        # 1 2 3 4 5 / 0~4
        # 0:5 + 0:0 -> 12345 + ""
        # 1:5 + 0:1 -> 2345 + 1
        A = sorted(nums)
        for i in range(len(nums)):
            B = nums[i:] + nums[:i] 
            if B == A:
                return True
        return False
