from collections import defaultdict
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # return "maximized" point
        # pick any nums[1] delete 
        # and then res += nums[1]

        # and then delete the both nums[1] + 1 or nums[1] - 1

        # seems like I have to check all the possibilities...
        # one remove and remove if there is one..

        # top down
        hashmap = defaultdict(int)
        max_number = 0
        for num in nums:
            hashmap[num] += num
            max_number = max(max_number, num)
        

        def dp(num):
            if num == 0:
                return 0
            if num == 1:
                return hashmap[1]
            
            if num not in memo:
                memo[num] = max(dp(num-1), dp(num-2) + hashmap[num])
            return memo[num]

        memo = {}
        return dp(max_number)

