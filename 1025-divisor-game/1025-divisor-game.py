class Solution:
    def divisorGame(self, n: int) -> bool:
        def can_win(current_n):
            if current_n == 1:
                return False
            
            if current_n not in memo:
                memo[current_n] = False
                for x in range(1, current_n):
                    if current_n % x == 0:
                        if not can_win(current_n - x):
                            memo[current_n] = True            
            return memo[current_n]
        memo = {}
        return can_win(n)


        def getOptimalX(current_n):
            for x_candidate in range(1, current_n):
                if current_n % x_candidate == 0:
                    return x_candidate
            return -1
        
        
        def dp(is_alice_turn, current_max_n): # True, 2 -> optimal_choice -> 1
            # base case if current_max_n == 1: no more choice
            if current_max_n == 1:
                return not is_alice_turn  # return false if alice turn has max range with 1
            
            if (is_alice_turn, current_max_n) not in memo:
                optimal_choice = getOptimalX(current_max_n)
                if optimal_choice == -1:
                    memo[(is_alice_turn, current_max_n)] = False
                else:
                    memo[(is_alice_turn, current_max_n)] = dp(not is_alice_turn, current_max_n - optimal_choice)
            
            return memo[(is_alice_turn, current_max_n)]
        memo = {}
        return dp(True, n)

        # alice -> bob
        # 0 < x < n and n % x == 0 x는 n보다 작은 약수겠군
        # n -= x
        # true if alice win -> 홀수번으로 나오면 이기는거야.
        # 약수의 개수가 2n + 1 이면 True
        
        # 1:  False
        # 2: 1고르고 True
        # 3: 1고르고 -> 1고르고 False
        # 4: 1고르고 -> 1고르고 -> 1고르고 True
        return n % 2 == 0

 