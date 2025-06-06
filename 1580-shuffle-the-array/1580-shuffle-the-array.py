class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        left = 0
        right = n
        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(nums[left])
                left += 1
            else:
                res.append(nums[right])
                right += 1
        return res
