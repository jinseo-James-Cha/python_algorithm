
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in frequency.items():
            bucket[freq].append(num)
        print(bucket)
        res = []
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i]:
                for num in bucket[i]:
                    res.append(num)
                    if len(res) == k:
                        return res
        return res