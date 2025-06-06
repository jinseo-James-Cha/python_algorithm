class Solution:

    def __init__(self, nums: List[int]):
        self.arr=nums[:] # deep copy
        self.n=len(nums)

    def reset(self) -> List[int]:
        return self.arr 

    def shuffle(self) -> List[int]:
        ans=self.arr[:] # deep copy
        for i in range(self.n-1):
            j=randint(i, self.n-1)
            ans[i], ans[j]=ans[j], ans[i]
        return ans
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()