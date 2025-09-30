class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # bubble sort - optimized
        copied = heights[:]
        has_swapped = True
        while has_swapped:
            has_swapped = False
            for i in range(len(copied) - 1):
                if copied[i] > copied[i+1]:
                    copied[i+1], copied[i] = copied[i], copied[i+1]
                    has_swapped = True
        
        res = 0
        for a, b in zip(heights, copied):
            if a != b:
                res += 1
        return res