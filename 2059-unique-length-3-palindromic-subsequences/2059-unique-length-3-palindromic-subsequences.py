class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        



        # 10**5 -> o(N) or O(n log n)
        # a a b c a
        # a a b c a
        # if a 1 1 1 a ? find the same letters  and then res += distance between ?
        # if a is done, continue
        # anyway I need to search on count >= 2 
        # missed unique part 
        d = defaultdict(list)
        for i, ch in enumerate(s):
            d[ch].append(i)
        
        seen = set()
        for k, v in d.items():
            if len(v) < 2:
                continue
            
            # same letter get the first index and last index
            first_index = v[0]
            last_index = v[-1]
            if last_index - first_index > 1:
                for i in range(first_index+1, last_index):
                    seen.add((k+s[i]+k))
        return len(seen)







        # unique subsequence -> set? and return len(set)?
        # length three combinations -> backtrack?
        # btw, three len palindromic means curr[0] == curr[2] ?
        # TLE O(n**3)
        def backtrack(curr, start):
            if len(curr) == 3:
                if curr[0] == curr[2]:
                    res.add(tuple(curr[:]))
                return
            
            for i in range(start, len(s)):
                curr.append(s[i])
                backtrack(curr, i+1)
                curr.pop()

        res = set()
        backtrack([], 0)
        return len(res)