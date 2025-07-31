class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
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
                curr = root
                for j in range(i, len(s)):
                    c = s[j]
                    if c not in curr.children:
                        break
                    
                    curr = curr.children[c]
                    if curr.is_word:
                        dp[j] = True
        print(dp)
        return dp[-1]