class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_index = word2_index = shortest = float(inf)

        for i, w in enumerate(wordsDict):
            flag = False
            if w == word1:
                word1_index = i
                flag = True
            elif w == word2:
                word2_index = i
                flag = True
            
            if flag:
                shortest = min(shortest, abs(word1_index - word2_index))
        return shortest
                

            