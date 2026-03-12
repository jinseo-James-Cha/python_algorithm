class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        # XL -> LX  => L keeps moving to left side in result
        # RX -> XR => R keeps moving to right side in result

        # two pointer
        # find index where it is not X
        # 1. return False if not the same
        # 2. return False if L is right side in result
        # 3. return False if R is left side in result

        if start.count('X') != result.count('X'):
            return False

        s_idx = r_idx = 0
        while s_idx < len(start) and r_idx < len(result):
            while s_idx < len(start) and start[s_idx] == 'X':
                s_idx += 1
            while r_idx < len(result) and result[r_idx] == 'X':
                r_idx += 1
            
            if s_idx == len(start) or r_idx == len(result):
                return s_idx == len(start) and r_idx == len(result)
            
            if start[s_idx] != result[r_idx]:
                return False
            if start[s_idx] == 'L' and s_idx < r_idx:
                return False
            if start[s_idx] == 'R' and s_idx > r_idx:
                return False
            
            s_idx += 1
            r_idx += 1
        
        return True
        