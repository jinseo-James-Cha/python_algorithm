class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 0 1 2 3
        # 0: 1
        # 1: 1 1
        # 2: 1 2 1      for i in range(1, 2) -> row[row][i] = row[row-1][i-1] + [i] 
        # 3: 1 3 3 1 -> for i in range(1, 3) 
        # -> row[3][1] = row[2][0] + row[2][1]
        # -> row[3][2] = row[2][1] + row[2][2]

        # dp?
        # 0 dp[0] = [1]
        # 1 dp[1] = [1, 1]
        # 2 dp[2] = [1, 2, 1] 
        # 3 dp[3]

        dp = [[1] * i for i in range(1, 3)]
        if rowIndex <= 1:
            return dp[rowIndex]
        
        # print(dp)
        # need to add values from rowIndex 2
        # 1 , 2,  1
        # row[row][i] = row[row-1][i-1] + [i]
        for i in range(2, rowIndex + 1):
            temp = [0] * (i + 1)
            temp[0] = temp[-1] = 1
            for j in range(1, i):
                print(dp[-1])
                temp[j] = dp[-1][j-1] + dp[-1][j]
            dp.append(temp)
        return dp[rowIndex]
        