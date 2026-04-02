class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True
    
    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr:
                return False
            curr = curr[ch]
        
        return curr.is_end

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Trie
        # S   l e e t c o d e
        #dp T F F F T F F F T   
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        
        n = len(s)
        dp = [False] * n
        for i in range(n):
            if i == 0 or dp[i-1]:
                curr = trie.root
                for j in range(i, n):
                    if s[j] not in curr.children:
                        break
                    curr = curr.children[s[j]]
                    if curr.is_end:
                        dp[j] = True
        return dp[-1]

        # bottom up
        dp = [False] * len(s)
        
        for i in range(len(s)):
            for word in wordDict:
                if i < len(word) - 1:
                    continue
                if i == len(word) - 1 or dp[i-len(word)]:
                    if s[i - len(word) + 1 : i + 1] == word:
                        dp[i] = True
                        break
        return dp[-1]

        # top down
        def dp(i):
            if i < 0:
                return True
            
            if i not in memo:    
                memo[i] = False
                for word in wordDict:
                    if s[i - len(word) + 1: i + 1] == word and dp(i - len(word)):
                        memo[i] = True
            
            return memo[i]
        
        memo = {}
        return dp(len(s) - 1)

        # BFS
        # add start-end possible word from each letter
        words = set(wordDict) # time = O(m * k) m is length and k is the avg len of each word to get hash
        queue = deque([0])
        seen = set()

        while queue:
            start = queue.popleft() # 0
            if start == len(s):# reach the end
                return True
            
            for end in range(start + 1, len(s) + 1): # check all possible words from start ~ end
                if end in seen: # if end is already true, we don't need to do
                    continue
                
                if s[start:end] in words:
                    queue.append(end)
                    seen.add(end)
        return False