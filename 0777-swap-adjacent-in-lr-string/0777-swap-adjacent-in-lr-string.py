class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        # XL -> LX
        # RX -> XR
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
        