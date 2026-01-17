class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointers for nums[i] = nums[j] + nums[k]
        # target == nums[left] + nums[right]
        # 1 == -1 + 2
        def two_pointers(numbers, target):
            res = []
            left = 0
            right = len(numbers) - 1 
            while left < right:
                curr_num = numbers[left] + numbers[right]
                if curr_num + target == 0 :
                    res.append([target, numbers[left], numbers[right]])
                    right -= 1
                    left += 1
                elif  curr_num + target > 0:
                    right -= 1
                else:
                    left += 1
            return res

        res = []
        used = set()
        nums.sort()
        for i in range(len(nums) - 2):
            triplets = two_pointers(nums[i+1:], nums[i])
            if triplets:
                for tri in triplets:
                    if tuple(tri) not in used:
                        res.append(tri)
                        used.add(tuple(tri))
        return res
        # uhm i j k -> n^3 -> two pointers -> O(N^2)
        res = []

        # # make a standard from the beginning and using two pointer to match with 0
        # # but I need sorted array :D

        # # TLE issue cause for O(N^2)
        # # 3 <= nums.length <= 3000
        nums.sort()
        for i in range(len(nums)):
            standard = nums[i]
            left = i + 1 
            right = len(nums) - 1

            # to prevent standard cannot be positive value cuz its sorted
            if standard > 0:
                break

            # to prevent duplicate triplets
            # standard already done
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                if standard + nums[left] + nums[right] == 0:
                    res.append([standard, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # to prevent duplication skip left if tis the same 
                    # left dup
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # right dup
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] + standard > 0 :
                    right -= 1
                else:
                    left += 1        
        return res
        