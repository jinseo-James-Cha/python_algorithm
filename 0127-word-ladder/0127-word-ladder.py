from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        DFS
        hit -> ait..cit..zit, hat..hot -> aot...dot -> aot...dot?used..lot-> log -> aog..cog -> endWord
        hit -> hot -> dot -> lot -> log -> cog -> 6 times
        hit -> hot -> dot -> dog -> cog -> 5 times ..

        ideas
        - think infinite loop -> remove used word in wordList, so we cannot go again.
        - update with minimum number of time-> biggest number -> 6 -> 5
        
        edge cases
        - if beginword len != endword len -> return 0
        - if endword not in wordlist -> return 0
        - no add no remove character -> check only the same length word

        time: O((len(beginword) * 26) ^ len(wordList)) -> 26^n -> n!
        space: O(n + n + l) -> O(n)

        BFS
        shortest path? -> bfs?
        hit0 -> hot1 -> dot2 -> lot3 -> log4 -> dog5 -> cog6
                             
                     -> lot2 -> dot3 -> dog4 -> cog5

        ideas
        - hashmap to save each word with minimum path -> hashmap[word] = minimum number to reach this path
        - from the current word -> change a character and check which is in the hashmap and add to the queue
        - save the minimum path by word and keep updating
        - if the saved path > new path -> update and find more ways with this
        - if not, continue
        """
        # BFS
        if len(beginWord) != len(endWord):
            return 0
        
        remain_wordList = set(wordList)
        if endWord not in remain_wordList:
            return 0

        if beginWord in remain_wordList:
            remain_wordList.remove(beginWord)
        
        queue = deque([(1, beginWord)])
        while queue:
            curr_path, curr_word = queue.popleft()
            if curr_word == endWord:
                return curr_path
            
            for i in range(len(beginWord)):
                for j in range(26):
                    c = chr(ord('a') + j)
                    if c == curr_word[i]:
                        continue
                    new_word = curr_word[:i] + c + curr_word[i+1:]
                    if new_word in remain_wordList:
                        remain_wordList.remove(new_word)
                        queue.append((curr_path+1, new_word))
        return 0




        # DFS
        def dfs(beginWord, endWord, curr_wordList, num_transformation):
            nonlocal min_transformation
            if num_transformation == min_transformation:
                return

            if beginWord == endWord:
                min_transformation = min(min_transformation, num_transformation)
                return
            
            # hit
            for i in range(len(beginWord)):
                for j in range(26): # lowercase alphabets
                    new_word = beginWord[:i] + chr(ord('a') + j) + beginWord[i+1:]
                    if new_word in curr_wordList:
                        curr_wordList.remove(new_word)
                        dfs(new_word, endWord, curr_wordList, num_transformation + 1)
                        curr_wordList.add(new_word)

        if len(beginWord) != len(endWord):
            return 0

        if endWord and endWord not in wordList:
            return 0

        # search by o(1) time -> list -> hashset
        curr_wordList = set(wordList)
        min_transformation = float('inf')
        dfs(beginWord, endWord, curr_wordList, 1)
        return min_transformation if min_transformation != float('inf') else 0

        