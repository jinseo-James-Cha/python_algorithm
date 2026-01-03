class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 1 ~ 9
        # only once in a combination

        def backtrack(curr_combi, curr_num):
            if sum(curr_combi) == n and len(curr_combi) == k:
                combinations.append(curr_combi[:])
            elif sum(curr_combi) > n or len(curr_combi) > k:
                return
            
            for num in range(curr_num, 10):
                curr_combi.append(num)
                backtrack(curr_combi, num+1)
                curr_combi.pop()

        combinations = []
        backtrack([], 1)
        return combinations