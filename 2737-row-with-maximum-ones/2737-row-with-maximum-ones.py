class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        # the row that contains the maximum count
        # and the numbers of ones in that row
        # if equal count -> smallest row num
        smallest_row = 0
        count_of_ones = 0

        for i in range(len(mat)):
            current_count_of_ones = 0
            for num in mat[i]:
                if num == 1:
                    current_count_of_ones += 1
            if current_count_of_ones > count_of_ones:
                count_of_ones = current_count_of_ones
                smallest_row = i
        return [smallest_row, count_of_ones]