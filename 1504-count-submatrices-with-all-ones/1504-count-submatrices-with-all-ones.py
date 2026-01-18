class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        """
          1 0 1
          1 1 0
          1 1 0

        0 0 0 0
        0 1 0 1 = 2
        0 2 2 0 = 5
        0 3 4 0 = 7
        """
        m, n = len(mat), len(mat[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    dp[i][j] = dp[i][j-1] + 1 if j > 0 else 1
        
        """
        [
        [1, 0, 1], 
        [1, 2, 0], 
        [1, 2, 0]
        ]

        """
        res = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0: 
                    continue
                min_width = float('inf')
                # 현재 행(i)부터 위쪽(k)으로 올라가며 가능한 높이를 탐색
                for k in range(i, -1, -1):
                    # 위로 올라갈수록 너비는 가장 짧은 것에 맞춰짐 (교집합)
                    min_width = min(min_width, dp[k][j])
                    
                    # 0을 만나면 더 이상 직사각형 불가
                    if min_width == 0:
                        break
                        
                    res += min_width
                    
        return res