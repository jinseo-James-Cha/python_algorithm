class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d: # days more than jobs, everyday needs one job
            return -1

        hardest_job_remaining = [0] * n
        hardest_job = 0
        for i in range(n-1, -1, -1):
            hardest_job = max(hardest_job, jobDifficulty[i])
            hardest_job_remaining[i] = hardest_job
        

        def dp(i, day):
            if day == d:
                return hardest_job_remaining[i]        
            
            if (i,day) not in memo:
                best = float("inf")
                hardest = 0
                # Iterate through the options and choose the best
                for j in range(i, n - (d - day)): # Leave at least 1 job per remaining day
                    hardest = max(hardest, jobDifficulty[j])
                    best = min(best, hardest + dp(j + 1, day + 1)) # Recurrence relation
                    memo[(i,day)] = best

            return memo[(i, day)]
            
        memo = {}
        return dp(0, 1)