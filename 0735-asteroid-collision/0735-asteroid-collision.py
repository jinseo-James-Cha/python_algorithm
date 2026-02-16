class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        """
        + = right
        - = left

        return asteroids after collisions.
        two asterids meet smaller one explode
        a1 > a2 -> remove a2
        a1 == a2 -> remove a1, a2 
        
        -> -> <- inward values are collision
        5 10 -5
           10 and -5 meet and -5 gone because absolute value 10 > 5
        
        -> <-
        8 -8
        removed the both

        -> -> <-
        10 2 -5
           abs(2) < abs(5)  2 gone and 10 > 5 5 gone

        10 2 
            -5
        10 and -5
        """

        # 3 5 -6 2 -1 4
        # stack [3, 5]
        # 5 < 6
        # pop()
        # 3 < 6
        # pop()
        # stack = []
        # stack = [-6]

        # 6 < 2
        stack = []

        for a in asteroids:
            alive = True
            
            # collision
            while alive and stack and stack[-1] > 0 and a < 0:
                if stack[-1] > -a:
                    alive = False
                elif stack[-1] == -a:
                    stack.pop()
                    alive = False
                else:
                    stack.pop()
            
            if alive:
                stack.append(a)

        return stack
                

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
                    

            