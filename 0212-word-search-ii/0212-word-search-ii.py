from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def search(self, word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]
        return curr.is_word
    
    def insert(self, word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        def is_within_bound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])

        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(node, i, j, path, visited):
            if node.is_word:
                res.append(path)
                node.is_word = False
            
            visited.add((i, j))
            for dy, dx in DIRS:
                next_i, next_j = dy+i, dx+j
                if is_within_bound(next_i, next_j) and (next_i, next_j) not in visited and board[next_i][next_j] in node.children:
                    dfs(node.children[board[next_i][next_j]], next_i, next_j, path + board[next_i][next_j], visited)
            visited.remove((i,j))
            
        m, n = len(board), len(board[0])
        res = []
        for row in range(m):
            for col in range(n):
                if board[row][col] in trie.root.children:
                    dfs(trie.root.children[board[row][col]], row, col, board[row][col], set())
        return res
    
        

        
        







        # TLE
        def is_within_bounds(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0])
        
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(row, col, word, word_idx, visited):
            if word_idx == len(word)-1:
                found.add(word)
                return
            
            visited.add((row, col))
            for dy, dx in DIRS:
                next_row, next_col = row+dy, col+dx
                if is_within_bounds(next_row, next_col) and (next_row, next_col) not in visited and board[next_row][next_col] == word[word_idx+1]:
                    dfs(next_row, next_col, word, word_idx+1, visited)
            
            visited.remove((row, col))


        hashmap = defaultdict(set)
        for w in words:
            hashmap[w[0]].add(w)

        found = set()
        m, n = len(board), len(board[0])
        for row in range(m):
            for col in range(n):
                if board[row][col] in hashmap: # check the first letter matching
                    for word in hashmap[board[row][col]]:
                        if word not in found:
                            dfs(row, col, word, 0, set())
        res = list(found)
        return res