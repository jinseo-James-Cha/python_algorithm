class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # BFS


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
        # def dp(i):
        #     if i < 0:
        #         return True
            
        #     if i not in memo:    
        #         memo[i] = False
        #         for word in wordDict:
        #             if s[i - len(word) + 1: i + 1] == word and dp(i - len(word)):
        #                 memo[i] = True
            
        #     return memo[i]
        
        # memo = {}
        # return dp(len(s) - 1)








        # 0. Analysis
        # true -> if s can be segmented into a space-separated sequence
        # True -> s == wordDict[0] + word[1]

        # 1. intuition
        # first thought of this solution is Trie.
        # if trie is is_word true and then go back to the beginning
        # should I use dfs to keep going even tho "cat" is not ok later
        # but "cats" will be ok?


        root = TrieNode()
        for word in wordDict:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_word = True

        dp = [False] * len(s)
        for i in range(len(s)):
            if i == 0 or dp[i - 1]: # 첫 시작이거나 dp로 확인했을때 이전 단어가 true인 경우 leetcodedp에서 c인 경우 같은거지
                curr = root # trie 다시 순회하면서 단어 있나 검색
                for j in range(i, len(s)): # 해당 스펠링부터 끝까지가 기준임
                    c = s[j]  
                    if c not in curr.children: # 없어? 그럼 브레이크 -> False야 그대로
                        break
                    
                    curr = curr.children[c] # 있으면 더 들어가자 
                    if curr.is_word: # 이 단어가 끝이있네? 그럼 true
                        dp[j] = True
        return dp[-1]