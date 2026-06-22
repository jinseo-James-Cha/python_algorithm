class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        B - - ->
          B - ->
            B -> 
                    OCEAN VIEW
        """
        # optimized solution
        # monotonic stack -> having index that having lower than stack[-1]
        # time: o(n)
        n = len(heights)
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()
            stack.append(i)
        return stack

        # Brute force
        # 2 nested loops -> check next elements has bigger or not
        # time o(n^2) > 10^5 -> TLE
        n = len(heights)
        res = []
        for i in range(n):
            curr_building = heights[i]
            ocean_view = True
            for j in range(i+1, n):
                if curr_building <= heights[j]:
                    ocean_view = False
                    break
            if ocean_view:
                res.append(i)
        return res


        # optimized solution
        # monotonic stack -> having index that having lower than stack[-1]
        # time o(n)
        monotonic_index_stack = [0]
        for i in range(1, len(heights)):
            while monotonic_index_stack and heights[monotonic_index_stack[-1]] <= heights[i]:
                monotonic_index_stack.pop()

            monotonic_index_stack.append(i)
        
        return monotonic_index_stack

        # brute force
        # O of n squared > 10**5 TLE
        res = []
        n = len(heights)
        for i in range(n):
            flag = True
            for j in range(i+1, n):
                if heights[i] <= heights[j]:
                    flag = False
                    break
            
            if flag:
                res.append(i)
        return res

        """
        questions
        - n buildings -> n = len(heights)
        - ocean is the right side ->

        4 2 3 1
        -
            -
          -
              -
        the rightmost building is always ocean view

        tracking the highest building on rightside and compare with its building
        if curr building is higher than the maximum building on right side, 
        it is the answer.

        <- backward traversal?

        """


        # 4 2 3 1
        
        # res [3]
        # 3 > 1 == res[-1]  O
        # res [3, 2]
        # 2 > 3 == res[2] X
        # res [3, 2]
        # 4 > 3 == res[2] O
        # res [3, 2, 0]

        n = len(heights)
        res = [n-1]
        for i in range(n-2, -1, -1):
            if heights[i] > heights[res[-1]]:
                res.append(i)
        
        # res.reverse()
        return res[::-1]

        
