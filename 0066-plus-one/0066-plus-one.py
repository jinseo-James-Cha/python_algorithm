class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] + 1 < 10:
            digits[-1] += 1
            return digits
        
        carry = 1
        res = []
        for num in reversed(digits):
            res.append((num + carry) % 10) # res[0, ]
            carry = int((num + carry) // 10) 
        
        if carry:
            res.append(1)

        res.reverse()
        return res