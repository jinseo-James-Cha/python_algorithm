from collections import defaultdict
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        """
        split nums into k length and each array is consecutive
        """
        # sort -> o(n log n)
        # edge case
        if len(nums) % k != 0:
            return False
        nums.sort()
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        total_left = len(nums)

        for num in nums:
            if counts[num] > 0:
                for curr in range(num, num + k):
                    if counts[curr] == 0:
                        return False
                    counts[curr] -= 1
        return True
        

        
        # Brute force -> O(n^2) -> TLE
        # edge case
        if len(nums) % k != 0:
            return False

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        total_left = len(nums)

        while total_left > 0:
            min_key = min(counts.keys())
            for i in range(k):
                if not counts.get(min_key + i):
                    return False
                
                counts[min_key+i] -= 1
                total_left -= 1
                if counts[min_key+i] == 0:
                    del counts[min_key+i]
        return True

            