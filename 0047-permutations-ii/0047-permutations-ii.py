class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        # time complexity - o(n * n!) if [1,2,3,..] all different, if all the same [1,1,1] => o(n)
        #                 - O(n * k) # k = number of unique permutations
        # space complexity - o(n * k)
        nums.sort()
        result = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack(path)

                path.pop()
                used[i] = False

        backtrack([])
        return result


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
