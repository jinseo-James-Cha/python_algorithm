class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # n -> bin(n) -> loop from index 2 to len-1 because of 0b as prefix
        # if i == i+1 return False
        bin_n = bin(n)[2:]
        for i in range(len(bin_n)-1):
            if bin_n[i] == bin_n[i+1]:
                return False
        return True