
# sentence1 = ["great","acting","skills"] 5 6 6
# sentence2 = ["fine","drama","talent"] 4 5 5
# similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]
# True
class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        s1_len = len(sentence1)
        s2_len = len(sentence2)
        if s1_len != s2_len:
            return False
        
        for i in range(s1_len):
            # same word -> similar
            if sentence1[i] == sentence2[i]:
                continue
            else: # if its different
                flag = False
                for x, y in similarPairs:
                    if (x == sentence1[i] and y == sentence2[i]) or (x == sentence2[i] and y == sentence1[i]):
                        flag = True
                if not flag:
                    return False
        return True
        