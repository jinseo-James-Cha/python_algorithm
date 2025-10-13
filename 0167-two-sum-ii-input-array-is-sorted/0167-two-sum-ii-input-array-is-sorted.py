class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # ordered by increasing
        # return the pair of index to match target
        # binary search
        res = []
        left = 0 
        right = len(numbers) - 1
        while left < right:
            curr = numbers[left] + numbers[right]
            if curr == target:
                res = [left+1, right+1]
                break
            elif curr > target:
                right -= 1
            else:
                left += 1
        return res








        res = []
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                res = [left+1, right+1]
                break
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return res