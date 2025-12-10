class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        """
        n locked computers 0~n-1 -> unique password
        0 -> decrypted and root
        others -> need to unlocked using previous unlocked computer

        
        """
        n = len(complexity)
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0
        
        res = 1
        MOD = 10**9 + 7
        for i in range(2, n):
            res = res * i % MOD
        return res