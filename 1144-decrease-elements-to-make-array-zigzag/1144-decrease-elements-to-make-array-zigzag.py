class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:

        moves_even_peaks = 0
        moves_odd_peaks = 0
        n = len(nums)

        for i in range(n):
            left = nums[i - 1] if i - 1 >= 0 else float('inf')
            right = nums[i + 1] if i + 1 < n else float('inf')
            need = max(0, nums[i] - min(left, right) + 1)
            if i % 2 == 0:
                moves_even_peaks += need
            else:
                moves_odd_peaks += need

        return min(moves_even_peaks, moves_odd_peaks)
        


        
        nums = [float('inf')] + nums + [float('inf')]

        n = len(nums)
        minimum_even_greater = 0
        minimum_odd_greater = 0

        for i in range(1, n-1, 2):
            if nums[i] >= min(nums[i-1], nums[i+1]):
                minimum_even_greater += nums[i] - min(nums[i-1], nums[i+1]) + 1
        
        for i in range(2, n-1, 2):
            if nums[i] >= min(nums[i-1], nums[i+1]):
                minimum_odd_greater += nums[i] - min(nums[i-1], nums[i+1]) + 1
        
        return min(minimum_even_greater, minimum_odd_greater)

