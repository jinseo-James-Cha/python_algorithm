class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        # problem
        # -1 point: T < lower
        # +1 point: T > upper

        # 1. intuition
        # calories[:k] -> sliding window

        # 2. complexity
        # O(n)

        # 3. data structure
        # res: int

        res = 0
        sliding_window = sum(calories[:k])
        if sliding_window < lower:
            res -= 1
        elif sliding_window > upper:
            res += 1
        
        for i in range(k, len(calories)):
            sliding_window += calories[i] - calories[i - k]
            if sliding_window < lower:
                res -= 1
            elif sliding_window > upper:
                res += 1
        return res