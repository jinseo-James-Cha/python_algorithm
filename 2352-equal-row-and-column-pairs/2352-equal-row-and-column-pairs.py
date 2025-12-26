class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.trie = TrieNode()
    
    def insert(self, array):
        curr_trie = self.trie
        for a in array:
            if a not in curr_trie.children:
                curr_trie.children[a] = TrieNode()
            curr_trie = curr_trie.children[a]
        curr_trie.count += 1
        
    def search(self, array):
        curr_trie = self.trie
        for a in array:
            if a not in curr_trie.children:
                return 0
            
            curr_trie = curr_trie.children[a]
        return curr_trie.count


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Trie
        my_trie = Trie()
        count = 0
        for row in grid:
            my_trie.insert(row)
        
        n = len(grid)
        for col in range(n):
            col_array = [grid[i][col] for i in range(n)]
            count += my_trie.search(col_array)
        return count




        # hashmap
        n = len(grid)
        row_hashmap = {}
        for row in grid:
            row_hashmap[tuple(row)] = row_hashmap.get(tuple(row), 0) + 1
        
        res = 0
        for col in zip(*grid):
            if col in row_hashmap:
                res += row_hashmap[col]
        return res