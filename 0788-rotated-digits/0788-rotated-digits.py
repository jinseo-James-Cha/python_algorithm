class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid_but_not_alone = {0, 1, 8}
        valid_digits = {2,5,6,9}
        
        count_good_number = 0
        for i in range(2, n+1):
            str_i = str(i)
            val_not_alone = 0
            val_alone = 0
            not_val = 0
            for a in str_i:
                if int(a) in valid_but_not_alone:
                    val_not_alone += 1
                elif int(a) in valid_digits:
                    val_alone += 1
                else:
                    not_val += 1
            
            if val_alone == 0:
                continue
            
            if not_val > 0:
                continue
            
            count_good_number += 1
            
            
        return count_good_number