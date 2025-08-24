class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)

        res = 0
        for i, col in enumerate(zip(*strs)):
            for i in range(len(col) - 1):
                if col[i] > col[i+1]:
                    res += 1
                    break
        return res