class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:


        # dp top down
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            currMax = 0
            # 마지막 그룹의 길이 j를 1부터 k까지 시도
            for j in range(1, min(i, k) + 1):
                # i-j는 현재 그룹의 시작 인덱스
                currMax = max(currMax, arr[i - j])
                # 점화식: 이전 상태의 최적값 + 현재 그룹의 합
                dp[i] = max(dp[i], dp[i - j] + currMax * j)
            
        return dp[n]