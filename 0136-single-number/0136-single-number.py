# O(N) time
# O(1) space
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        
        return xor        
        # if len(nums) <= 2:
        #     return nums[0]

        # for n in nums:
        #     index_n = nums.index(n)
        #     if not n in nums[index_n+1:]:
        #         return n

        # return nums[-1]
            
        