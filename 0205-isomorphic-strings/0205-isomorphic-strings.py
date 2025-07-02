class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
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
