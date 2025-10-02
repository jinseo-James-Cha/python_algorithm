class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        # equal length, only digits str
        # queries = [k, trim] rightmost trim digit

        # version2 - radix sort
        n = len(nums)
        m = len(nums[0])
        
        def countingSortByDigit(nums, digit):
            buckets = [[] for _ in range(10)]
            for num, idx in nums:
                val = int(num[digit])
                buckets[val].append([num, idx])
            return [x for bucket in buckets for x in bucket]

        base_nums = [[num, i] for i, num in enumerate(nums)]

        sorted_by_trim = {0: base_nums} 

        for trim in range(1, m+1):
            arr = sorted_by_trim[trim-1][:]
            arr = countingSortByDigit(arr, m - trim)
            sorted_by_trim[trim] = arr

        res = []
        for k, trim in queries:
            res.append(sorted_by_trim[trim][k-1][1])
        
        return res










        # version1 
        answer = []
        for k, trim in queries:
            trimmed = [(num[-trim:], i) for i, num in enumerate(nums)]
            # trimmed.sort(key=lambda x: (x[0], x[1]))
            trimmed.sort()
            answer.append(trimmed[k-1][1])
        return answer


