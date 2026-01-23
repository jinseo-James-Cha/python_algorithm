class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap
        hashmap = {}
        res = []
        for i, num in enumerate(nums):
            if num in hashmap:
                res = [hashmap[num], i]
                break
            else:
                hashmap[target - num] = i
        
        return res






        # naive solution
        # 2 loop

        n = len(nums)
        res = []
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    break
        return res