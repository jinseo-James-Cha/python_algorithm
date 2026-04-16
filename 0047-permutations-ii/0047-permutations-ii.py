class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # using one element at each time and make a permutation -> unique
        # get all combination and save only unique -> set

        
        def backtracking(curr_permutation, used_index_set):
            if len(curr_permutation) == len(nums):
                unique_permutation_set.add(tuple(curr_permutation))
                return

            for i in range(len(nums)):
                if i not in used_index_set:
                    curr_permutation.append(nums[i])
                    used_index_set.add(i)
                    
                    backtracking(curr_permutation, used_index_set)

                    curr_permutation.pop()
                    used_index_set.remove(i)
        
        unique_permutation_set = set()
        backtracking([], set())
        return list(unique_permutation_set)
