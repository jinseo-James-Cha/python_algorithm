class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer-Moore voting algorithm
        # There can be at most one majority element which is more than ⌊n/2⌋ times.
        # There can be at most two majority elements which are more than ⌊n/3⌋ times.
        # There can be at most three majority elements which are more than ⌊n/4⌋ times.
        # element1, count1
        # element2, count2
        # However it doesn't gaurantee it is the actual count of its element.

        if not nums:
            return []
        
        element1, element2, count1, count2 = None, None, 0, 0
        for num in nums:
            if element1 == num:
                count1 += 1
            elif element2 == num:
                count2 += 1
            elif count1 == 0:
                element1 = num
                count1 = 1
            elif count2 == 0:
                element2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        n = len(nums)
        res = []
        for element in [element1, element2]:
            if nums.count(element) > n // 3:
                res.append(element)
        return res











        # time = O(n)
        # space = O(n)
        n = len(nums)
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        res = []
        for k, v in count.items():
            if v > n/3:
                res.append(k)
        return res