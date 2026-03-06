class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        i = 1
        total_sum = 0
        while i * i <= num:
            if num % i == 0:
                total_sum += i
                if i * i != num:
                    total_sum += num / i
            i+=1
        return total_sum - num == num



        # TLE
        total_sum = 0
        
        for i in range(1, num):
            if num % i == 0:
                total_sum += i
        return total_sum == num