class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # days : 1 ~ 365
        # ways : 3  
        # costs
        # 1way. 1day - costs[0]
        # 2way. 7day - costs[1]
        # 3way. 30 day - costs[2]

        # days 1, 4, 6, 7, 8, 20 costs 2, 7, 15
        # day 1 -> 1day pass -> costs[0] -> $2 -> day 1~2
        # day 3 -> 7day pass -> costs[1] -> $7 -> day 3, 4, 5, 6, 7 ,8 ,9
        # day 20 -> 1day pass -> costs[0] -> $2 -> day 20

        # DP
        # state
        # days -> i
        
        # bottom up
        last_day = days[-1]
        days_set = set(days)
        dp = [0] * (last_day + 1)

        for i in range(1, last_day + 1):
            if i not in days_set:
                dp[i] = dp[i-1]
            else:
                day_pass = dp[i-1] + costs[0]
                week_pass = dp[max(0, i-7)] + costs[1]
                month_pass = dp[max(0, i-30)] + costs[2]
                dp[i] = min(day_pass, week_pass, month_pass)
        
        return dp[last_day]
            

        # top down
        @cache
        def dp(i):
            if i > days[-1]:
                return 0
            
            if i not in days_set:
                return dp(i+1)
            
            day_pass = costs[0] + dp(i+1)
            week_pass = costs[1] + dp(i+7)
            month_pass = costs[2] + dp(i+30)

            return min(day_pass, week_pass, month_pass)

        days_set = set(days)
        return dp(0)
        

        travel_days = set(days) # to look up faster
        last_day = days[-1] # ascending order 
        
        @cache
        def dp(i):
            if i > last_day:
                return 0
            
            if i not in travel_days:
                return dp(i+1)
            
            # choices
            day_pass = costs[0] + dp(i+1)
            week_pass = costs[1] + dp(i+7)
            month_pass = costs[2] + dp(i+30)

            return min(day_pass, week_pass, month_pass)
        
        return dp(1)
        


        
