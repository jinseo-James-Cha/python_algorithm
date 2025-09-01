class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 0 : 1 0 0 0
        # 1 : 1 1 0 0
        # 2 : 1 2 1 0
        # 3 : 1 3 3 1

        row = [1] * (rowIndex + 1)

        for i in range(2, rowIndex + 1):
            # 뒤에서부터 업데이트
            for j in range(i-1, 0, -1):
                row[j] = row[j-1] + row[j]

        return row

        if rowIndex < 2:
            return [1] * (rowIndex+1)
        
        prev = [1] * 2
        for i in range(2, rowIndex + 1):
            current = [1] * (len(prev) + 1)
            for j in range(1, i):
                current[j] = prev[j-1] + prev[j]
            prev = current
        return prev



        # dp = [[1] * (rowIndex + 1) for _ in range(rowIndex + 1)]
        
        # # base case
        # for i in range(2, rowIndex + 1):
        #     for j in range(1, i):
        #         dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        # return dp[rowIndex]










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

        # dp = [[1] * i for i in range(1, 3)]
        # if rowIndex <= 1:
        #     return dp[rowIndex]
        
        # # print(dp)
        # # need to add values from rowIndex 2
        # # 1 , 2,  1
        # # row[row][i] = row[row-1][i-1] + [i]
        # for i in range(2, rowIndex + 1):
        #     temp = [1] * (i + 1)
        #     for j in range(1, i):
        #         temp[j] = dp[-1][j-1] + dp[-1][j]
        #     dp.append(temp)
        # return dp[rowIndex]
        