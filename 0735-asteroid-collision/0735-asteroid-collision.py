class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # relative positing in space..
        # abs value -> size, sign(+right -left )

        # 5 -> 10 -> <- -5

        # stack to meet last element and curr element..

        # 5 10 -5
        res = []
        i = 0
        while i < len(asteroids):
            curr = asteroids[i]
            if not res:
                res.append(curr)
                i += 1
            elif curr > 0:
                res.append(curr)
                i += 1
            elif curr < 0:
                if res[-1] < 0:
                    res.append(curr)
                    i += 1
                elif res[-1] > abs(curr):
                    i += 1
                elif res[-1] == abs(curr):
                    res.pop()
                    i += 1
                else:
                    res.pop()
        return res                    
                    

            