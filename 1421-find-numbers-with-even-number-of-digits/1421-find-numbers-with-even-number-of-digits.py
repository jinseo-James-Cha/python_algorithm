# 1 <= nums[i] <= 10^5
# cannot go with O(n^2)
# convert str and check len % 2 == 0 ? -> O(n)

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            s_n = str(n)
            if len(s_n) % 2 == 0:
                count += 1
        return count

        