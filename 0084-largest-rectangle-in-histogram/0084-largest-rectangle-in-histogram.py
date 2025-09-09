class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack - Monotonic stack
        # 기본적인 구성으로는 stack에 index를 담고 빼고하는 작업을 한다
        # 담는 기준은 이전의 막대 길이가 현재 길이보다 작으면, 즉 담겨있는 index는 막대길이가 오름차순인것
        # 이전 막대가 현재 막대보다 짧으면 팝해나가면서 그 넓이를 구한다

        index_stack = [-1] # sentinel -1, prove it is empty
        res = 0

        for i in range(len(heights)): # 모든 막대를 왼쪽 -> 오른쪽으로 한번씩 순회 o(n)

            # 현재 막대 heights[i]가 이전 막대의 높이(heights[index_stack[-1]]) 보다 작거나 같으면
            # 인덱스를 팝해서, 그 팝한 막대를 '최소 높이로 간주하여' 넓이 계산
            while index_stack[-1] != -1 and heights[index_stack[-1]] >= heights[i]:
                current_height = heights[index_stack.pop()] # 팝한 인덱스의 막대길이는 지금구하려는 직사각형의 높이

                # 구하고자 하는 넓이의 오른쪽 경계는 i-1 왼쪽 경계는 stack[-1]+1이므로
                # width = (i-1) - (stack[-1] + 1) + 1
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

