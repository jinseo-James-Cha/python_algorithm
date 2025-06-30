class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        # brackets[i] = [upper, percent]
        # income 10
        # i == 0 -> upper
        # i > 0 -> upper[i] - upper[i-1]
        # min(upper[i] - upper[i-1], rest of income)

        tax = 0.0
        for i in range(len(brackets)):
            prev_upper = 0
            if i != 0:
                prev_upper = brackets[i-1][0]
            
            cur_upper, percentage = brackets[i]
            
            applying_upper = min(income, cur_upper - prev_upper)
            tax += applying_upper * (percentage / 100)
            income -= applying_upper
        return tax