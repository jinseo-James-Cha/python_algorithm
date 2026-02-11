class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        peak element

        1 2 1 3 5 6 4
          _       _

        answer will be one of the indices that has a greater than its neighbors
        -> one pass and save the indices which have greater than left one
        <- one pass and check the indices which are already in set and return that index

        time = o(n)
        """
        # -> one pass
        # first index 0 is always greater than out of bound
        found = set([0])
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                found.add(i)
        
        res = []
        # the last index n-1 is always greater than out of bound
        if n-1 in found:
            res.append(n-1)
        
        for i in range(n-2, -1, -1):
            if nums[i] > nums[i+1] and i in found:
                res.append(i)
        
        return res[0]