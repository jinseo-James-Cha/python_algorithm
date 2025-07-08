class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            self.prefixSum.append(self.prefixSum[i-1] + nums[i])
        print(self.prefixSum)
        

    def sumRange(self, left: int, right: int) -> int:
        # 0 ~ 2 -> prefixsum[2]
        if left == 0 :
            return self.prefixSum[right]
        
        # 2 ~ 5 -> prefixSum[5] - prefixSum[2 - 1] => -3 - -2 == -1
        return self.prefixSum[right] - self.prefixSum[left - 1]
        
        

# prefix sum?!
# sum[i:j] = prefix_sum[j] - prefix_sum[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)