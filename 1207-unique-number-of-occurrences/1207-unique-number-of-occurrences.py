from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_count = defaultdict(int)
        for num in arr:
            num_count[num] += 1
        
        count_set = set()
        for v in num_count.values():
            if v in count_set:
                return False
            count_set.add(v)
        return True