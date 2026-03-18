class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        
        return [1] + digits



        
        if digits[-1] + 1 < 10:
            digits[-1] += 1
            return digits
        
        carry = 1
        res = []
        for num in reversed(digits):
            res.append((num + carry) % 10)
            carry = (num + carry) // 10 
        
        if carry:
            res.append(1)

        res.reverse()
        return res

        """
        brute force
        join them and convet to int and +1
        """
        
        total_int = 0
        for i in range(len(digits)):
            total_int = total_int*10 + digits[i]
            
        total_int += 1
        
        res = []
        while total_int > 0: # 1 2 4
            res.append(total_int % 10) # 4 2 1
            total_int //= 10 # 12  1 0
            
        return res[::-1]
        