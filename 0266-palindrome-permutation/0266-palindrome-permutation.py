class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # palindrome has to have even nums
        # add a letter into set and if there is the letter already, remove it
        # check set size -> len s is odd -> size 1 true or false
        s_set = set()
        for a in s:
            if not a in s_set:
                s_set.add(a)
            else:
                s_set.remove(a)
        
        return len(s_set) <= 1

        # I already did the add and remove by even numbers.
        # so s_set_len is already true if <= 1
        # s_set_len = len(s_set)
        # s_len = len(s)
        # if s_len % 2 == 0 and s_set_len == 0:
        #     return True
        # elif s_len % 2 != 0 and s_set_len == 1:
        #     return True
        
        # return False



        