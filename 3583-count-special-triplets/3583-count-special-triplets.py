from collections import defaultdict
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        d = defaultdict(list)
        for i,num in enumerate(nums):
            d[num].append(i)

        def binary_search(index_list, index_target):
            left = 0
            right = len(index_list)
            while left < right:
                mid = (left + right) // 2
                if index_list[mid] < index_target:
                    left = mid +1
                else:
                    right = mid
            
            return left

        res = 0
        for k, v in d.items():
            # only even nums
            if k % 2 != 0:
                continue
            # cannot be i and k
            if len(v) < 2:
                continue            
            
            # not found j value
            if d.get(k // 2, []) == []:
                continue

            # binary search
            for j in d[k//2]:
                count_i = binary_search(v, j)
                
                k_start = binary_search(v, j + 1)
                count_k = len(v) - k_start
                
                res = (res + count_i * count_k) % MOD
        return res
        



        
        # TLE -> O(N**3)
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] == nums[j] * 2 and nums[k] == nums[j] * 2:
                        res += 1
        return res