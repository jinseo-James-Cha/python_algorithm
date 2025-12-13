from collections import defaultdict
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        # coupons[i] = code[i], businessLine[i], isActive[i]
        # valid coupon
        # 1. code[i] is not empty and only alphanumeric and _
        # 2. four categories.
        # 3. active true
        n = len(code)
        businessLine_hashmap = {"electronics": 0, "grocery": 1, "pharmacy" : 2, "restaurant": 3}
        res = [[] for _ in range(4)]
        for i in range(n):
            if not code[i]:
                continue
            
            if businessLine[i] not in businessLine_hashmap:
                continue
            
            if not isActive[i]:
                continue
            
            codePass = True
            for c in code[i]:
                if not c.isalnum() and c != "_":
                    codePass = False
                    break
            
            if not codePass:
                continue
            
            res[businessLine_hashmap[businessLine[i]]].append(code[i])
        
        ans = []
        for r in res:
            if r:
                r.sort()
                ans.extend(r)
        
        return ans

