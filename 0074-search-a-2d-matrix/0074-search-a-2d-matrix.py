class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # matrix[i][j] increasing order
        # matrix[i][0] increasing ordr

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


        # binary search - > sorted ok
        # first binary search for lower bound for matrix[i][0]
        # second find the exact target in matrix[i]
        # m, n = len(matrix), len(matrix[0])
        # def get_lower_bound(nums, target):
        #     left = 0
        #     right = len(nums)
        #     while left < right:
        #         mid = (left + right) // 2
        #         if nums[mid] <= target:
        #             left = mid + 1
        #         else:
        #             right = mid
            
        #     return left-1
        
        # def check_target(nums, target):
        #     left = 0
        #     right = len(nums) - 1
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if nums[mid] == target:
        #             return True
        #         elif nums[mid] > target:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     return False

        # found_row_num = get_lower_bound([matrix[i][0] for i in range(m)], target)
        # if found_row_num < 0:
        #     return False

        # return check_target(matrix[found_row_num], target)


            





        # brute force -> O(n*m)
        # row_num = -1
        # for r in range(m):
        #     if matrix[r][0] == target:
        #         return True
        #     elif matrix[r][0] < target:
        #         row_num = r
        # # if not found, return False
        # if row_num < 0:
        #     return False

        # for c in range(n):
        #     if matrix[row_num][c] == target:
        #         return True

        # return False    
