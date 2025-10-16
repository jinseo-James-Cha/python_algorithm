class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}
        used = set()
        for i in range(len(s)):
            if s[i] not in char_map:
                if t[i] in used:
                    return False
                char_map[s[i]] = t[i]
                used.add(t[i])
            else:
                if char_map[s[i]] != t[i]:
                    return False
        return True













        char_map = {}

        for sc, tc in zip(s, t):
            if sc in char_map:
                if char_map[sc] != tc:
                    return False
            elif tc in char_map.values():
                return False

            char_map[sc] = tc

        return True

# class Solution:
#     def transformStr(self, s: str) -> str:
#         isomorphic_pairs = {}
#         new_s = []
#         for i, c in enumerate(s):
#             if c not in isomorphic_pairs:
#                 isomorphic_pairs[c] = i
#             new_s.append(str(isomorphic_pairs[c]))
#         return " ".join(new_s)
            
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         return self.transformStr(s) == self.transformStr(t)
