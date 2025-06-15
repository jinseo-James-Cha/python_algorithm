# I think its sliding window!!
# lets go with it

from collections import deque
class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        loop_combination = deque(nums[:k])
        max_combination = nums[:k]
        for i in range(k,len(nums)):
            loop_combination.popleft()
            loop_combination.append(nums[i])
            for j in range(k):
                if loop_combination[j] < max_combination[j]:
                    break
                elif loop_combination[j] == max_combination[j]:
                    continue
                else:
                    max_combination = nums[i-k+1:i+1]
                    break
        return max_combination

