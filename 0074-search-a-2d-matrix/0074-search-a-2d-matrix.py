class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # stair case
        # start from left bottom
        # if its greater than target -> move up
        # if its less than target -> move right

        m, n = len(matrix), len(matrix[0])
        row, col = m-1, 0 # bottom left
        while 0 <= row < m and 0 <= col < n:
            curr_num = matrix[row][col]
            if curr_num == target:
                return True
            elif curr_num > target:
                row -=1
            else:
                col += 1
        
        return False












        # v4 / O(log(n*m))
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = divmod(mid, n)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

        # v3
        # 2d -> 1d and then binary search?
        arr = []
        for i in range(len(matrix)):
            arr.extend(matrix[i])
        
        def binary_search(nums, target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        
        return binary_search(arr, target)


        # V2
        # binary search - > sorted ok
        # first binary search for lower bound for matrix[i][0]
        # second find the exact target in matrix[i]
        m, n = len(matrix), len(matrix[0])
        def get_lower_bound(nums, target):
            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            
            return left-1
        
        def check_target(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return False

        found_row_num = get_lower_bound([matrix[i][0] for i in range(m)], target)
        if found_row_num < 0:
            return False

        return check_target(matrix[found_row_num], target)


        # V1 
        row_num = -1
        for r in range(m):
            if matrix[r][0] == target:
                return True
            elif matrix[r][0] < target:
                row_num = r
        # if not found, return False
        if row_num < 0:
            return False

        for c in range(n):
            if matrix[row_num][c] == target:
                return True

        return False    
