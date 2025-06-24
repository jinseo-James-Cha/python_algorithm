from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs = Counter(words)
        
        # using tuple (1priority to compare, 2priority if 1st is the same value)
        # using -freq to take "minimum" first but actually maximum
        max_heap = [(-freq, word) for word, freq in freqs.items()]

        # transform list -> heapq by tuple elements
        heapq.heapify(max_heap)
        return [heapq.heappop(max_heap)[1] for _ in range(k)]
    