class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        word-a predecessor of word-b
        insert one letter anywhere in word-a => word-b

        """
        chains = {}
        words.sort(key = lambda x:len(x))

        for word in words:
            chains[word] = 1

            for i in range(len(word)):
                pred = word[:i] + word[i+1:]
                if pred in chains:
                    chains[word] = max(chains[word], chains[pred] + 1)
        
        return max(chains.values())