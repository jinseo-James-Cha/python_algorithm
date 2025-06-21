class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # int h < nums -> valid 
        # h is valid if all values in the array that are strictly greater than "h" are identical.
        # i don't understand h 9 is valie in 10, 8, 10, 8
        # cuz h > all values but 8 > h is not valid
        # For each index i where nums[i] > h, set nums[i] to h.
        # 10 -> h,

        # I got it .
        # the goal is to make all values equal to k
        # and return how many times it needs.
        # 5 2 5 4 5 -> 4 2 4 4 4 -> 2 2 2 2 2 -> return 2
        ### edge case:  if a num is less than k, return -1?!

        # if num[i] > k put into set and check len 
        # if num[i] < k return -1
        s = set()
        for n in nums:
            if n > k:
                s.add(n)
            elif n < k:
                return -1
        
        return len(s)

        