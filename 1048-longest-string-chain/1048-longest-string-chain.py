class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        word-a predecessor of word-b
        insert one letter anywhere in word-a => word-b
        """
        # dp bottom up
        words.sort(key=lambda x:len(x))
        dp = {}

        for word in words:
            dp[word] = 1

            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)

        return max(dp.values())

        # dp top down
        def dfs(word):
            if word in memo:
                return memo[word]
            
            max_len = 1
            for i in range(len(word)): #3  bca -> ca, ba, bc 
                prev = word[:i] + word[i+1:]
                if prev in words_set:
                    max_len = max(max_len, 1 + dfs(prev))

            memo[word] = max_len
            return max_len

        words_set =set(words)
        memo = {}
        return max([dfs(word) for word in words])



        # hashmap
        # time complexity: O(n log n + n * 16^2) => O(n log n)
        chains = {}
        words.sort(key = lambda x:len(x))

        for word in words:
            chains[word] = 1

            for i in range(len(word)):
                pred = word[:i] + word[i+1:]
                if pred in chains:
                    chains[word] = max(chains[word], chains[pred] + 1)
        
        return max(chains.values())