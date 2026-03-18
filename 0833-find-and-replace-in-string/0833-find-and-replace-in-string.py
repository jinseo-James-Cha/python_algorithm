class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # time complexity = O(N + K * L) L: length of a source 
        # =>s[idx: idx + len(src)] → O(len(src)) -> O(L)
        
        changes = {}
        for idx, src, tgt in zip(indices, sources, targets):
            if s[idx: idx + len(src)] == src:
                changes[idx] = (len(src), tgt)

        res = []
        i = 0
        while i < len(s):
            if i in changes:
                jump_length, change = changes[i]
                res.append(change)
                i += jump_length
            else:
                res.append(s[i])
                i += 1
        return "".join(res)