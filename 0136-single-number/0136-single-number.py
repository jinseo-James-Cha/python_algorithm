class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        temp = []
        for n in nums:
            if n in temp:
                temp.remove(n)
            else:
                temp.append(n)
        return temp[0]        