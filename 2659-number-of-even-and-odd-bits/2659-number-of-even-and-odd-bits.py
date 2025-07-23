class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        # convert to bit and stack pop in index check
        def convertToBit(x: int) -> List[int]:
            res = []
            while x > 0:
                res.append(x % 2)
                x //= 2
            return res 

        bit_n = convertToBit(n)
        res = [0, 0]
        for i, bit in enumerate(bit_n):
            if bit == 1:
                res[i % 2] += 1
        return res
            
