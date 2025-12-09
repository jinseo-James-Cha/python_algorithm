from collections import defaultdict
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        # o(n)
        # MOD = 10**9 + 7
        # num_cnt = defaultdict(int)
        # num_partial_cnt = defaultdict(int)

        # for num in nums:
        #     num_cnt[num] += 1
        
        # res = 0
        # for num in nums:
        #     target = num * 2
        #     left_cnt = num_partial_cnt.get(target, 0)
            
        #     num_partial_cnt[num] += 1

        #     right_cnt = num_cnt.get(target, 0) - num_partial_cnt.get(target, 0)

        #     res = (res + left_cnt * right_cnt) % MOD
        # return res





        # # O(n**2)
        # MOD = 10**9 + 7
        # res = 0
        # for j in range(1, len(nums)-1): # j range 
        #     i = j - 1
        #     k = j + 1

        #     # count left
        #     count_left = 0
        #     while i >= 0:
        #         if nums[i] == nums[j] * 2:
        #             count_left += 1
        #         i -= 1
            
        #     if count_left == 0:
        #         continue

        #     # count right
        #     count_right = 0
        #     while k < len(nums):
        #         if nums[k] == nums[j] * 2:
        #             count_right += 1
        #         k += 1
            
        #     if count_right == 0:
        #         continue
                        
        #     res = (res + count_left * count_right) % MOD
        # return res


        # O(n log n)
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