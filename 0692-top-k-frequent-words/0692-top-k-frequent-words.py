from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs = Counter(words)
        
        max_heap = [(-freq, word) for word, freq in freqs.items()]
        
        print(max_heap)

        heapq.heapify(max_heap)

        print(max_heap)

        return [heapq.heappop(max_heap)[1] for _ in range(k)]
    