class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # length
        # updates[i] = [startIdx, endIdx, inc]

        # 0:       -2 = -2
        # 1: +2    -2 = 0
        # 2: +2 +3 -2 = 3
        # 3: +2 +3    = 5
        # 4:    +3    = 3

        # prefix sum
        ans = [0] * (length+1)
        for startIdx, endIdx, inc in updates:
            ans[startIdx] += inc
            ans[endIdx + 1] -= inc
        
        total_sum = 0
        for i, num in enumerate(ans):
            total_sum += num
            ans[i] = total_sum
        return ans[:-1]


        # brute force O(len(updates) * n)
        # TLE
        arr = [0] * length
        for startIdx, endIdx, inc in updates:
            for i in range(startIdx, endIdx+1):
                arr[i] += inc
        
        return arr