class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        longest = 0
        for k, v in hashmap.items():
            plus_one = v + hashmap[k+1] if k+1 in hashmap else 0
            longest = max(longest, plus_one)
        return longest
        