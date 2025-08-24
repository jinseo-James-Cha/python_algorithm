class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # perm n+1, range(0, n)
        # if perm[i] < perm[i + 1]:
        #     s[i] == 'I'
        
        # if perm[i] > perm[i + 1]:
        #     s[i] == 'D'

        # two pointer ?
        # left is from 0  / and right is from n + 1?
        n = len(s)
        left = 0
        right = n

        res = []
        for letter in s:
            if letter == 'I':
                res.append(left)
                left += 1
            else:
                res.append(right)
                right -= 1
        res.append(left)
        return res