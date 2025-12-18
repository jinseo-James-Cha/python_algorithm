class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(" ")
        
        reversed_s_list = []
        while s_list:
            curr = s_list.pop()
            if curr:
                reversed_s_list.append(curr)
        
        return " ".join(reversed_s_list)