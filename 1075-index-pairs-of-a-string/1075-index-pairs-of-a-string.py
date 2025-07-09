class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        # get index i and j to match with each word in words
        
        # need to think duplicate i 
        # starting from the beginning ?
        # brute force -> O(n^3)
        
        # constraints : All the strings of words are unique

        res = set()

        for word in words:
            first = word[0]
            for i, t in enumerate(text):
                if first == t:
                    j =  i + len(word)
                    if word == text[i:j]:
                        res.add((i,j - 1))
        
        res = list(res)
        res.sort(key= lambda x: (x[0], x[1]))
        return res