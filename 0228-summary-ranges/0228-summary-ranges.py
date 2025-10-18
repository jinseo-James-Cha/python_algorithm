class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        ranges = []
        num_set = set(nums)
        for num in nums:
            if num - 1 not in num_set:
                current_num = num
                current_range = [current_num, current_num]
                while current_num + 1 in num_set:
                    current_num += 1
                    current_range[-1] = current_num
                ranges.append(current_range)
        
        res = []
        for a, b in ranges:
            if a != b:
                res.append(str(a) + "->" + str(b))
            else:
                res.append(str(a))
        return res
