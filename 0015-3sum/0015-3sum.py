class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        nums[i] + nums[j] + nums[k] == 0
        a + b + c = 0
        a = -b -c
        -a = b + c
        
        loop each nums until n - 2 cuz of triplet
            target is the each num with -c and check two sums sets
        
        using sets not to have duplicates
        """
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]

            left = i + 1
            right = n - 1

            while left < right:
                curr = nums[left] + nums[right]

                if curr == target:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif curr < target:
                    left += 1
                else:
                    right -= 1

        return res


        def find_two_sums(arr, target):
            found = []
            left = 0
            right = len(arr) - 1
            while left < right:
                curr = arr[left] + arr[right]
                if curr == target:
                    found.append([-target, arr[left], arr[right]])
                    left += 1
                    right -= 1
                elif curr > target:
                    right -= 1
                else:
                    left += 1
            return found


        n = len(nums)
        nums.sort()
        found_triplets = set()
        res = []
        for i in range(n-2):
            triplets = find_two_sums(nums[i+1:], -nums[i])
            for triple in triplets:
                t = tuple(triple)
                if t not in found_triplets:
                    found_triplets.add(t)
                    res.append(triple[:])
        return res