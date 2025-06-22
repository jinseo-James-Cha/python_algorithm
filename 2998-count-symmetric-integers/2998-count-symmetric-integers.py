class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # x -> 2 * n digits symmetric
        # what is symmetric?!
        # x = 2 * n -> XX XXXX XXXXXX meaning?!
        # if the sum of the first n digits of x is equals to the sum of the last n digits of x
        # the sum of the first n digits of x == the sum of the last n digits of x
        # 0 ~ mid == mid ~ -1 is symmetric
        # 1 <= low <= high <= 10**4 -> cannot use O(N**2)
        
        # convert int to str and cut half and convert back to int
        count = 0
        for num in range(low, high + 1):
            s_num = str(num)
            # skip len odd number
            if len(s_num) % 2 != 0:
                continue

            mid = len(s_num) // 2 # 1234 -> mid 2
            first_half = second_half = 0
            for i in range(len(s_num)):
                if i < mid:
                    first_half += int(s_num[i])
                else:
                    second_half += int(s_num[i])
            
            if first_half == second_half:
                print(s_num)
                print(first_half)
                print(second_half)
                count += 1
        return count
            

        