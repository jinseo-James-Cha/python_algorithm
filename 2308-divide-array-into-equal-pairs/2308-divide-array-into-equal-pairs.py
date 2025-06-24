from collections import defaultdict
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # 2 * n -> len
        # len(nums) / 2 ==> n
        # num of pairs == n -> true
        n = len(nums) / 2
        num_of_pairs = 0
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
            if hashmap[num] % 2 == 0:
                num_of_pairs += 1
        return num_of_pairs == n

        