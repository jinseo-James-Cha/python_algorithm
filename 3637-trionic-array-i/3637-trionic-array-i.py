class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        """
        n = len(nums)

        indices 0 < p < q < n - 1
        nums[0~p] -> increasing
        nums[p~q] -> decreasing
        nums[q~n-1] -> increasing

        up -> down -> up

        1 3 5 4 2 2 6
            P   Q
        """

        p, q = -1, -1

        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                p = i
                break
            elif nums[i] == nums[i+1]:
                return False
        
        for j in range(n-1, 0, -1):
            if nums[j-1] > nums[j]:
                q = j
                break
            elif nums[j-1] == nums[j]:
                return False
        
        for k in range(p, q):
            if nums[k] < nums[k+1]:
                return False
        
        return 0 < p < q < n - 1


