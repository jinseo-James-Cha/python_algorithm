from collections import defaultdict
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        abs(nums[i] - nums[j]) = k

        nums[i] = nums[j] + k


        hashmap[nums[i] - k] = i

        3 1 4 1 5 , k 2
        
        1:0
       -1: 1,3
        2: 2
        3: 4


        """
        nums.sort()
        left = 0
        right = 1
        result = 0
        while left < len(nums) and right < len(nums):
            if left == right or nums[right] - nums[left] < k:
                right += 1
            elif nums[right] - nums[left] > k:
                left += 1
            else:
                left += 1
                result += 1
                while left < len(nums) and nums[left] == nums[left-1]:
                    left += 1
        return result


        counter = defaultdict(int)
        for i, num in enumerate(nums):
            counter[num] += 1
        
        res = 0
        for x in counter:
            if k > 0 and x + k in counter:
                res += 1
            elif k == 0 and counter[x] > 1:
                res += 1
        return res


        nums.sort()
        left = 0
        right = 1
        result = 0
        while left < len(nums) and right < len(nums):
            if left == right or nums[right] - nums[left] < k:
                right += 1
            elif nums[right] - nums[left] > k:
                left += 1
            else:
                left += 1
                result += 1
                while left < len(nums) and nums[left] == nums[left-1]:
                    left += 1
        return result
        