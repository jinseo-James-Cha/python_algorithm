class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds = []
        for a in arr:
            if a % 2 != 0:
                odds.append(a)
                # if not odds:
                #     odds.append(a)
                # else:
                #     if odds[-1] < a:
                #         odds.append(a)
                #     else:
                #         print(odds)
                #         odds = [a]
            else:
                odds = []
            
            if len(odds) == 3:
                return True
        return False