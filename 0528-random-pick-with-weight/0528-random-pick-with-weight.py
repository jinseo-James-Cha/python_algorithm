class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for num in w:
            prefix_sum += num
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        # random.random() => 0.0 <= x < 1.0
        # 0 <= x < total_sum
        target = self.total_sum * random.random()
        
        left, right = 0, len(self.prefix_sums)
        while left < right:
            mid = (left + right) // 2
            if  self.prefix_sums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()