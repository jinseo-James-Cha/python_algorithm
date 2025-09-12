class Solution:
    def jump(self, nums: List[int]) -> int:
        near, far = 0,0
        i, n = 0, len(nums)
        res = 0
        while i < n-1:
            far = max(far, i + nums[i]) # 2
            if near == i:
                res += 1
                near = far            
            i += 1
        return res