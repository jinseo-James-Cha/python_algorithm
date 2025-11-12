import math
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # need to use index..
        # which index first and gcd with right one. so candidates 0 ~ n-2
        
        # each time save index and its gcd
        # each index should change at least once if not return -1
        n = len(nums)
        total_gcd = nums[0]
        for num in nums:
            total_gcd = math.gcd(total_gcd, num)
        
        if total_gcd != 1:
            return -1
        
        count_ones = nums.count(1)
        if count_ones > 0:
            return n - count_ones
        
        # 1이 없으면, gcd 1을 만들기 위한 최소 구간 찾기
        res = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    res = min(res, j - i)
                    break
        
        return res + n - 1 if res != float('inf') else -1