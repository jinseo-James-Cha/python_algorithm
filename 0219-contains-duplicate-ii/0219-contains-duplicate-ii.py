class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for i, num in enumerate(nums):
            if num not in hashmap:
                hashmap[num] = i
            else:
                if abs(hashmap[num] - i) <= k:
                    return True
                hashmap[num] = i
        return False

        
        # Time Limit Exceeded
        for i in range(1, k+1):
            for slow, fast in zip(nums, nums[i:]):
                if slow == fast:
                    return True
        return False