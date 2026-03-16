
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in frequency.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res

        # priority queue
        # O(n log n)
        counts = Counter(nums)

        pq = []
        for num, freq in counts.items():
            heapq.heappush(pq, (-freq, num))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(pq)[1])
        
        return res