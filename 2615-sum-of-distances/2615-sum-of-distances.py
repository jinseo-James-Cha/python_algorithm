from collections import deque
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        """
        arr[i] = sum of |i - j|
        nums[j] == nums[i] and j != i

        1 3 1 1 2
        
        1 : 0, 2, 3
        2 : 4
        3 : 1        
        """
        # hashmap
        groups = defaultdict(list)
        for i, num in enumerate(nums):
            groups[num].append(i)

        res = [0] * len(nums)
        
        for group in groups.values():
            total = sum(group)
            prefix_total = 0
            
            size = len(group)
            for i, idx in enumerate(group):
                res[idx] = total - prefix_total * 2 + idx * (2 * i - size)
                prefix_total += idx
        return res






        # brute force -> o(n^2) -> TLE
        # each element and check the same? and to the sum
        res = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    res[i] += abs(i - j)
        return res