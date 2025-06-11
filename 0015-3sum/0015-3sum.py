class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # uhm i j k -> n^3 -> two pointers -> O(N^2)
        res = []

        # make a standard from the beginning and using two pointer to match with 0
        # but I need sorted array :D

        # TLE issue cause for O(N^2)
        # 3 <= nums.length <= 3000
        nums.sort()
        for i in range(len(nums)):
            standard = nums[i]
            left = i + 1 
            right = len(nums) - 1

            # TLE
            # to prevent standard cannot be positive value cuz its sorted
            if standard > 0:
                break

            # TLE 
            # to prevent duplicate triplets
            # standard already done
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                if standard + nums[left] + nums[right] == 0:
                    
                    # TLE
                    # THIS IS MAKING O(N^3) !!!!!
                    # if not [standard, nums[left], nums[right]] in res:
                    res.append([standard, nums[left], nums[right]])
                    left += 1
                    # right -= 1
                    
                    # TLE
                    # to prevent duplication skip left if tis the same 
                    # left dup
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # # right dup
                    # while left < right and nums[right] == nums[right + 1]:
                    #     right -= 1
                elif nums[left] + nums[right] + standard > 0 :
                    right -= 1
                else:
                    left += 1        
        return res
        