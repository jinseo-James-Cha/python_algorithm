class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        # convert to bit and stack pop in index check
        def convertToBit(x: int) -> List[int]:
            res = []
            while x > 0:
                remainder = x % 2
                res.append(remainder)
                x //= 2
            return res

        bit_n = convertToBit(n)
        print(bit_n)
        res = [0, 0]
        for i, n in enumerate(bit_n):
            if n == 0:
                continue
            
            if i % 2 == 0:
                res[0] += 1
            else:
                res[1] += 1
        return res
            
