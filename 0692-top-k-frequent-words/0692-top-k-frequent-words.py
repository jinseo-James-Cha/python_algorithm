from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # get frequence by word
        frequency = {}
        for word in words:
            frequency[word] = frequency.get(word, 0) + 1
        
        bucket = [[] for _ in range(len(words) + 1)]
        for word, freq in frequency.items():
            heapq.heappush(bucket[freq], word)

        res = []
        for i in range(len(bucket) - 1, -1, -1):
            while bucket[i]:
                res.append(heapq.heappop(bucket[i]))

                if len(res) == k:
                    return res
        return res