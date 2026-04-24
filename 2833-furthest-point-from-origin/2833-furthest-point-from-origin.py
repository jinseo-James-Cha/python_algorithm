class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left = 0
        right = 0
        underscore = 0
        for m in moves:
            if m == "L":
                left += 1
            elif m == "R":
                right += 1
            else:
                underscore += 1
        
        return abs(left - right) + underscore