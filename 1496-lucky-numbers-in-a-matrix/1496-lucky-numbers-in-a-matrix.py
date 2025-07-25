class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        # 3 7 8
        # 9 11 13
        # 15 16 17
        minimum_in_rows = set()
        res = []
        
        for m in matrix:
            minimum_in_rows.add(min(m))
        
        for n in zip(*matrix):
            if max(n) in minimum_in_rows:
                res.append(max(n))
        
        return res