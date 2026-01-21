class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        seen = set()

        def backtrack(combination, used_index):
            if combination and tuple(combination) not in seen:
                    seen.add(tuple(combination))

            for i, num in enumerate(tiles):
                if i not in used_index:
                    used_index.add(i)
                    combination.append(num)

                    backtrack(combination, used_index)                    

                    used_index.remove(i)
                    combination.pop()
    
        backtrack([], set())
        return len(seen)