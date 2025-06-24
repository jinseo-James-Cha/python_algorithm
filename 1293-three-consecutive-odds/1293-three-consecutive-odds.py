class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds = []
        for a in arr:
            if a % 2 != 0:
                odds.append(a)
            else:
                odds = []
            
            if len(odds) == 3:
                return True
        return False