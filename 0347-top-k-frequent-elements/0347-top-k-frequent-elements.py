from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        buckets = [[] for _ in range(len(nums) + 1)]
        counts = Counter(nums)
        for num, freq in counts.items():
            buckets[freq].append(num)
        
        flat_list = [item for sublist in buckets for item in sublist]
        return flat_list[::-1][:k]




        # if k == len(nums):
        #     return nums
        
        # counts = defaultdict(int)
        # for num in nums:
        #     counts[num] += 1
        
        # return heapq.nlargest(k, counts.keys(), key=counts.get)
        
        