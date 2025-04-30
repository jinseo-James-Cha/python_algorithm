# return len(ans) = n + 1
# i 0 <= i <= n
# ans[i] is the number of 1's in the binary representation of i.

class Solution:
    def countBits(self, n: int) -> List[int]:
        def to_binary(n):
            result = ''
            while 0 < n:
                result = str(n % 2) + result
                n //= 2
            return result or '0'

        return [to_binary(a).count('1') for a in range(n+1)]
    

    

    

        