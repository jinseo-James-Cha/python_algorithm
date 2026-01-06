class TrieNode:
    def __init__(self):
        self.children = {}
        self.alphabets = [False] * 26
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.result_buffer = []
    
    def search(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return False
            curr = curr.children[letter]
        return curr.is_word
    
    def insert(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
                curr.alphabets[ord(letter) - ord('a')] = True
            curr = curr.children[letter]
        curr.is_word = True
    
    # def startWith(self, prefix):
    #     curr = self.root
    #     for letter in prefix:
    #         if letter not in curr.children:
    #             return False
    #         curr = curr.children[letter]
    #     return True
    
    def dfs_with_prefix(self, curr: Node, word: str):
        if len(self.result_buffer) == 3:
            return
        
        if curr.is_word:
            self.result_buffer.append(word)

        # 사전순(a-z)으로 자식 노드 방문
        # 파이썬 딕셔너리는 순서가 보장되지 않으므로 정렬된 키를 순회합니다.
        for i, alpha in enumerate(curr.alphabets):
            if alpha:
                letter = chr(i + ord('a'))
                self.dfs_with_prefix(curr.children[letter], word + letter)
    
    def get_words_starting_with(self, prefix):
        self.result_buffer = []
        curr = self.root
        
        for char in prefix:
            if char not in curr.children:
                return []
            curr = curr.children[char]
        
        # 접두사 끝 노드부터 DFS 시작
        self.dfs_with_prefix(curr, prefix)
        return self.result_buffer
            


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # search suggestions system ! like google search .
        # when I type a letter of searchWord, it shows up to 3 products.
        # return len == len(searchWord)

        # Trie. TrieNode.
        # but how to get three lexicographically minimums products. -> need to use min_heap instead of hashmap?
        # if I don't use min_heap, I can use alpha->number alphabet[ord(ch) - ord('a')]
        """
        products = ["mobile","mouse","moneypot","monitor","mousepad"]
        searchWord = "mouse"

        type m
        m -> len(1) -> o -> b len(1)-> mobile
        m -> len(1) -> o -> n len(2) -> moneypot
                                     -> monitor
        if len == 3 -> return them
        """
        trie = Trie()
        for product in products:
            trie.insert(product)
        
        res = []
        prefix = ""
        for letter in searchWord:
            prefix += letter
            res.append(trie.get_words_starting_with(prefix))

        return res             
            