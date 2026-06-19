class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        index_stack = [-1]
        res = 0

        for i in range(len(heights)):
            while index_stack[-1] != -1 and heights[index_stack[-1]] >= heights[i]:
                current_height = heights[index_stack.pop()]
                current_width = (i-1) - (index_stack[-1] + 1) + 1
                res = max(res, current_height * current_width)
            index_stack.append(i) # 현재 인덱스를 스택에 푸시, 증가하는 높이 유지.
        

        # 순회가 끝나고 나서, 남은 인덱스들 처리
        # 오른쪽 경계가 배열의 끝(len(heights)-1)이므로, 폭 계산에서 i대신 len(height)사용
        while index_stack[-1] != -1:
            current_height = heights[index_stack.pop()]
            current_width = (len(heights)-1) - (index_stack[-1] + 1) + 1
            res = max(res, current_height * current_width)
        return res
            
        






        # divide and conquer -> AVG O(nlogn), WORST O(n^2) if its sorted
        def calculateArea(heights, start, end):
            if start > end:
                return 0
            min_index = start
            for i in range(start, end+1):
                if heights[min_index] > heights[i]:
                    min_index = i
            
            return max(heights[min_index] * (end-start+1), calculateArea(heights, start, min_index-1), calculateArea(heights, min_index+1, end))
        
        return calculateArea(heights, 0, len(heights) - 1)




        # brute force -> O(n^2) -> 10^3까지 가능  -> 10^5 TLE
        res = 0
        for i in range(len(heights)):
            min_height = heights[i]
            res = max(res, heights[i])
            for j in range(i+1, len(heights)):
                min_height = min(min_height, heights[j])
                res = max(res, min_height * (j-i+1))
        return res

            



        # Two pointer X
        # min_h = min(heights[left:right+1]) -> O(n)
        # so it O(n^2) -> TLE
        # and also, 
        if len(heights) == 1:
            return heights[0]

        left, right = 0, len(heights)-1
        res = 0

        while left <= right:
            min_h = min(heights[left:right+1])
            # print(min_h, right, left)
            res = max(res, min_h * (right-left+1), heights[left], heights[right])
            # print(res)

            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                left += 1
        
        return res

