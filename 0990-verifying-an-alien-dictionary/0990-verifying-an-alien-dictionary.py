class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        def check_two_words(word1, word2):
            i = 0

            while i < len(word1) and i < len(word2):
                if order_dict[word1[i]] > order_dict[word2[i]]:
                    return False
                elif order_dict[word1[i]] < order_dict[word2[i]]:
                    return True
                i += 1
            return len(word1) <= len(word2)


        order_dict = {}
        res = []
        for k, v in enumerate(order):
            order_dict[v] = k

        for i in range(len(words)-1):
            if not check_two_words(words[i], words[i+1]):
                return False
        return True
