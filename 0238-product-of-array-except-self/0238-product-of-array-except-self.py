class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1 2 3 4

        1: 2 * 3 * 4 all from right
        2: 1 * 3 * 4 1 left 2 right
        3: 1 * 2 * 4 2 left 1 right
        4: 1 * 2 * 3 all from left

        -> 
        prev = nums[0]
        
        """
        # two pass o(n)
        # product -> way and then <- way
        
        answer = [1] * len(nums)
        
        # ->
        prev = nums[0]
        for i in range(1, len(nums)):
            answer[i] = prev
            prev *= nums[i]

        # <- 
        prev = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            answer[i] *= prev
            prev *= nums[i]
        
        return answer


        # naive solution - brute force
        # time complexity - O(n^2)
        answer = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    answer[i] *= nums[j]
        
        return answer