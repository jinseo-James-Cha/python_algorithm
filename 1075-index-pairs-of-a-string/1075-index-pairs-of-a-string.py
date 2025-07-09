class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.is_word = True

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        # v2 Trie - prefix tree
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        res = []
        for i in range(len(text)):
            node = trie.root
            for j in range(i, len(text)):
                if text[j] not in node.children:
                    break
                node = node.children[text[j]]
                if node.is_word:
                    res.append([i, j])
        return res

        # V1
        # get index i and j to match with each word in words
        
        # need to think duplicate i 
        # starting from the beginning ?
        # brute force -> O(n^3)
        
        # constraints : All the strings of words are unique

        # res = set()

        # for word in words:
        #     first = word[0]
        #     for i, t in enumerate(text):
        #         if first == t:
        #             j =  i + len(word)
        #             if word == text[i:j]:
        #                 res.add((i,j - 1))
        
        # res = list(res)
        # res.sort(key= lambda x: (x[0], x[1]))
        # return res