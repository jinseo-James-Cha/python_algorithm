from collections import defaultdict
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        res = ""

        for word in dictionary:
            copy_s = s
            fount = 0
            for i, w in enumerate(word):
                if w not in copy_s:
                    break
                copy_s = copy_s[copy_s.index(w)+1:]
                fount += 1
            if fount == len(word):
                if len(word) > len(res):
                    res = word
                elif len(word) == len(res):
                    res = word if word < res else res
        
        return res
                


        # s_map = defaultdict(set)
        # for i, letter in enumerate(s):
        #     s_map[letter].add(i)

        # res = []
        # for d in dictionary:
        #     prev = -1
        #     check_map = s_map
        #     for d_letter in d:
        #         if d_letter not in check_map:
        #             break
        #         elif s_map[d_letter] < prev:
        #             break
                
        #     print(d, prev)
        #     if d[-1] in s_map and prev == s_map[d[-1]]:
        #         res.append(d)
        # print(res)
