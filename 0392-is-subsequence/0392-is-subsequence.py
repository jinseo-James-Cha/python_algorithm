class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # two pointer?
        # one for s one for t
        # if s[slow] == t[fast]: slow += 1
        # if slow == len(s) - 1 : true or not
        
        # a a 0 0
        # x h 1 1, 1 2 1 3 1 4 1 

        slow = fast = 0
        while slow < len(s) and fast < len(t):
            if s[slow] == t[fast]:
                slow += 1
            fast += 1
        
        return slow == len(s)