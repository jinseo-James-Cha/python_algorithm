class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # one operation -> choose + integer X which is <= smallest element
        # return num of operation making all 0

        # make the array set and check len
        # len - 1 if 0 is in the set

        s = set(nums)
        len_s = len(s)
        return len_s - 1 if 0 in s else len_s