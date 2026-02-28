from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # priority queue
        # O(n log n)
        counts = Counter(nums)

        pq = []
        for num, freq in counts.items():
            heapq.heappush(pq, (-freq, num))
        
        res = []
        for i in range(k):
            freq, num = heapq.heappop(pq)
            res.append(num)
        
        return res

        # bucket sort
        # O(n)
        if len(nums) <= k:
            return nums
        
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            buckets[freq].append(num)
        
        # flatten
        res = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res
        # res = [x for bucket in buckets for x in bucket]
        # return res[::-1][:k]








        if len(nums) == k:
            return nums
        
        buckets = [[] for _ in range(len(nums) + 1)] # 만약 다 같은 숫자여도 저장가능해야해서 +1
        counts = Counter(nums)
        for num, freq in counts.items():
            buckets[freq].append(num)
        
        flat_list = [x for bucket in buckets for x in bucket]
        return flat_list[::-1][:k]