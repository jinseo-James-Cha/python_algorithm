class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0

        while len(nums) > 1:
            flag = True
            min_sum = float('inf')
            target_idx = -1

            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i+1]
                if nums[i] > nums[i+1]:
                    flag = False
                
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    target_idx = i
            
            if flag:
                break
            
            res += 1
            nums[target_idx] = min_sum
            nums.pop(target_idx + 1)
        
        return res