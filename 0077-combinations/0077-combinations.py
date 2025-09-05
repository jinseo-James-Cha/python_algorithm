class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, current):
            if len(current) == k:
                res.append(current[:])
                return
            
            for i in range(start, n+1):
                current.append(i)
                backtrack(i+1, current)
                current.pop()
            
        res = []
        backtrack(1, [])
        return res




















        # 1. intuition
        # I don't know the loop's depths -> backtracking?
        # no duplications -> [1,2] == [2, 1]
        # using for loop in range(1, n+1)
        # 1 -> 2 and pop and call backtrack 1 -> 3 ~~~
        # len == k -> put res and pop

        # 2. complexity
        # Backtrack: no duplication -> N^N
        # 20^20 -> is it possible to use backtrack?

        # 3. data structure
        # res: [][] no duplication
        # cur: []

        def backtrack(start: int, cur: List[int]):
            if len(cur) == k:
                res.append(cur[:])
                return
            for i in range(start, n + 1):
                cur.append(i)
                backtrack(i + 1, cur)
                cur.pop()
        
        res = []
        backtrack(1, [])
        return res
    
    
