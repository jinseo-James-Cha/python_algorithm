class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for a in accounts:
            total = sum(a)
            max_wealth = max(total, max_wealth)
        return max_wealth