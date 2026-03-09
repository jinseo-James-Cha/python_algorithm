class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """
        in-place -> swapping the nums

        [1,2,3] -> 1 passed, and 2 <-> 3 => [1,3,2]

        [3,2,1] -> 3is the max, 2 is the max and 1 is the end -> this is the maximum permutation => return minimum permutation


        1   3   5   4   2
            i-1 i   i+1
        
        1. find front changing value
        from 5(i) to 2(n-1)... is descending order -> maximum number
        3(i-1) is the first element which breaks the descending order from the back
        => 3(i-1) is the front changing value


        2. find back changing value
        find the least greater value than front changing value(3)
        => 4(i+1) is the back changing value

        3. swap those two values
        => 1 4 5 3 2

        4. reverse the part to minimim permutation after the front changing value
        => 5 3 2 => 2 3 5
        """

        n = len(nums)
        front_idx = n - 2

        # 1
        while front_idx >= 0 and nums[front_idx] >= nums[front_idx + 1]:
            front_idx -= 1

        if front_idx >= 0:
            back_idx = n - 1
            # 2
            while nums[back_idx] <= nums[front_idx]:
                back_idx -= 1
            
            # 3
            nums[front_idx], nums[back_idx] = nums[back_idx], nums[front_idx]
        
        # 4
        left, right = front_idx + 1, n - 1
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1