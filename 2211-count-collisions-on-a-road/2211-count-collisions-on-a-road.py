class Solution:
    def countCollisions(self, directions: str) -> int:
        # n cars 0~ n-1 indexed
        # directions[i] = L, R, or S

        # R L R S L L
        #  2   1 1 1

        # L L R R
        # case
        # -> move  
        # count R number and if not R -> res += count R and count = 0

        # <- move
        # count L number and if not L -> res += count L and count 0


        n = len(directions)
        res = 0

        # move ->
        r_count = 0
        for d in directions:
            if d == "R":
                r_count += 1
            else:
                res += r_count
                r_count = 0
        
        l_count = 0
        for r_d in reversed(directions):
            if r_d == "L":
                l_count += 1
            else:
                res += l_count
                l_count = 0
        
        return res