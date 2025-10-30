class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # initial = [0] * len(target)
        # making the same integer array as target by minimum operation.
        # 1 operation -> +1 subarray elements

        # 1 2 3 2 1
        
        # 1 1 1 1 1 -> 0 1 2 1 0
        #   1 1 1   -> 0 0 1 0 0
        #     1     -> 0 0 0 0 0

        # 3 1 1 2
        # 1 1 1 1 -> 2 0 0 1
        # 1       -> 1 0 0 1
        # 1       -> 0 0 0 1
        #       1 -> 0 0 0 1

        # 3 1 5 4 2
        # 1 1 1 1 1 -> 2 0 4 3 2
        # 1         -> 1 0 4 3 2
        # 1         -> 0 0 4 3 2
        #     1 1 1 -> 0 0 3 2 1
        #     1 1 1 -> 0 0 2 1 0
        #     1 1   -> 0 0 1 0 0
        #     1     -> 0 0 0 0 0
        n = len(target)
        ans = target[0]
        for i in range(1, n):
            ans += max(target[i] - target[i-1], 0)
        return ans
        



        # brute force - TLE
        # 1 <= target.length <= 10**5
        n = len(target)
        initial = target[:]
        left = 0
        res = 0
        while left < n:
            if initial[left] == 0:
                left += 1
                continue
            
            res += 1
            i = left
            while i < n:
                if initial[i] == 0:
                    break
                initial[i] -= 1
                i += 1
        return res
