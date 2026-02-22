class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
       
        """
        sum(i~j) = prefix[j] - prefix[i-1]
        k = prefix[j] - prefix[i-1]
        prefix[i-1] = prefix[j] - k
        check in the past
        -> yes? i - j
        """
        max_len = 0
        prefix_sum = 0
        indices = {}
        for i,num in enumerate(nums):
            prefix_sum += num
            
            if prefix_sum == k:
                max_len = i + 1               

            if prefix_sum - k in indices:
                max_len = max(max_len, i - indices[prefix_sum - k])
            
            if prefix_sum not in indices:
                indices[prefix_sum] = i
        
        return max_len




        """
        brute force 
        loop check by size from n ~ 1
        if it makes -> return the size
        
        Time = O(n**3)
        Space = O(1)
        """
        n = len(nums)
        for size in range(n, 0, -1):
            for i in range(0, n - size + 1):
                curr_sum = sum(nums[i:i+size]) # o(n)
                if curr_sum == k:
                    return size
        
        return 0