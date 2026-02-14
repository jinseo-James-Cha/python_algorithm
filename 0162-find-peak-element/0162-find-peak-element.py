class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # goal: return index of peak element
        # peak element is i < i+1 > i+2 and i+1 is the peak
        # -> save index is hashmap who has greater than left one
        # <- check index in hashmap who has greater than right one
        # return an element in hashmap

        greater_indices = set([0])
        # ->
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                greater_indices.add(i)

        # <-
        if len(nums)-1 in greater_indices:
            return len(nums) - 1

        for j in range(len(nums)-2, -1, -1):
            if nums[j] <= nums[j+1] and j in greater_indices:
                greater_indices.remove(j)
        
        return greater_indices.pop()














        """
        log n solution
        binary search

        1 2 1 3 5 6 4
        L
                    R
              M
        """
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left


        




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