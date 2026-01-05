class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(1, n+1):
            # convert i -> binary and count 1 and save in ans[i]
            curr = i
            num_of_one = 0
            while curr >= 1:
                num_of_one += int(curr % 2 != 0)
                curr = curr // 2
            ans[i] = num_of_one
        return ans
