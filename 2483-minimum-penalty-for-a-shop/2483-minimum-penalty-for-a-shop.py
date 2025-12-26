class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # visit log indexed 0, 'N' or 'Y'
        # if ith is 'Y', customers come at ith hour
        # if 'N', no customer at ith
        # shop closes 'j'th hour
        
        # Panalty calculation
        # 1. shop is open, no customer -> +1
        # 2. shop is close, customer -> +1

        # return earliest hour to have minimize panalty.
        # YYNY
        # 0123
        
        # 0close -> YY Y -> 3 -> how many Y
        # 1close ->  Y Y -> 2
        # 2close ->    Y -> 1
        # 3close ->   NY -> 2
        # 4close ->   N  -> 1
        # 2, 4 is the minimum and 2 is the earliest

        #  YYNY
        # 32121
        n = len(customers)
        
        curr_panalty = sum( ch == "Y" for ch in customers)
        # curr_panalty = 0
        # for hour in range(n):
        #     if customers[hour] == 'Y':
        #         curr_panalty += 1

        minimum_panalty = curr_panalty
        minimum_hour = 0
        for hour in range(n):
            if customers[hour] == 'Y':
                curr_panalty -= 1
            else:
                curr_panalty += 1
            
            if curr_panalty < minimum_panalty:
                minimum_panalty = curr_panalty
                minimum_hour = hour+1
        return minimum_hour