class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_s = set(s)
        got_odd = False
        answer = 0
        for a in s_s:
            if s.count(a) >= 2:
                answer += s.count(a)
                if s.count(a) % 2 != 0:
                    answer -= 1
                    got_odd = True
            else:
                got_odd = True

        return answer + int(got_odd)
            


        

        