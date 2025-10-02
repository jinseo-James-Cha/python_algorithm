class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        # radix sort -> counting sort -> bucket
        
        n = len(nums)
        m = len(nums[0])
        
        def countingSortByDigit(nums, digit):
            buckets = [[] for _ in range(10)]
            for num, i in nums:
                bucket_idx = int(num[digit])
                buckets[bucket_idx].append([num, i])
            
            return [x for bucket in buckets for x in bucket]
        
        base_nums = [[num, i] for i, num in enumerate(nums)]
        trimmed_sorted_list = {0: base_nums}
        
        trimmed_list = base_nums
        for trim in range(1, m+1):
            trimmed_list = countingSortByDigit(trimmed_list, m-trim)
            trimmed_sorted_list[trim] = trimmed_list
            
        
        res = []
        for k, trim in queries:
            res.append(trimmed_sorted_list[trim][k-1][1])
        return res