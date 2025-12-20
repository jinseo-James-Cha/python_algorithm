class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # intuitive solution 3 for loop and O(n^3)
        # optimize to o(n)...


        # 1 2 3 4 5
        # 1
        # 1 2
        # 1 2 3 True

        # 2 1 5 0 4 6
        # 2
        #   1
        #   1 5
        #       0
        #       0 4 
        #       0 4 6
        # 1 1 5

        # 1 1 1 1 1 1
        #   1 1 

        # 1 2 8 1 9 2 7 1 9 2
        # 1 2 8
        #       1 9 
        # 1 2 8   9
        #       1   2

        
        first_num = float('inf')
        second_num = float('inf')
        for num in nums:
            if first_num >= num:
                first_num = num
            elif second_num >= num:
                second_num = num
            else:
                return True
        return False

