class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # 1 <= k <= n

        # n children stadning in a QUEUE
        # happiness[i] -> ith child happiness value
        
        # select k children in k turns -> k is the number of turns...
        # each turn, select a child the happiness value of all children that have not been selected till now decreases by 1
        # happiness value cannot become negative....

        # [1, 2, 3] k = 2
        # choose 3 and decrease 1 for others
        # [0, 1] k = 1
        # choose 1 and no decrease
        # [0]
        # return 3 + 1 == 4
        
        # maximize..... choose maximum always... and then -1 for all by each turn
        # cannot choose 0.. and if didn't choose anything then break..

        # to choose maximum first.. so I need to sort desc first?
        happiness.sort(reverse=True)
        res = max(happiness)
        turn = 1
        for i in range(1, k):
            if happiness[i]-i > 0:
                res += happiness[i]-i
        return res
