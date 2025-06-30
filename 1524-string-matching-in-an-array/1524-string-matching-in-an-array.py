class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # it's too simple to check with "in"
        # is there any better idea for better performance 
        # brute force o(n^2)
        res = []
        words
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                else:
                    if words[i] in words[j]:
                        res.append(words[i])
                        break
        return res