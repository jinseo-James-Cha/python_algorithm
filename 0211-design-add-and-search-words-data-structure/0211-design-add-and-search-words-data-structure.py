class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.is_word = True
        

    def search(self, word: str) -> bool:
        def search_in_node(word, node):
            for i, ch in enumerate(word):
                if ch not in node.children:
                    if ch == ".":
                        for x in node.children:
                            if x != "$" and search_in_node(word[i+1:], node.children[x]):
                                return True
                    return False
                else:
                    node = node.children[ch]
            return node.is_word

        return search_in_node(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)