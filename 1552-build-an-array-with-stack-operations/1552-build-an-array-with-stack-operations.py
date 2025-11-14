class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        s = []
        target_set = set(target)
        for i in range(1, n+1):
            s.append(i)
            res.append("Push")
            if i not in target_set:
                res.append("Pop")
                s.pop()
            
            if s == target:
                break
        return res
