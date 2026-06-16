class Solution:
    def processStr(self, s: str) -> str:
        """
        Problem:
        lowercase alphabets, *, #, %
        -> new string result

        rules 
        - lowercase -> append
        - * -> remove last character
        - # -> duplicates the current result and append it to itself
        - % -> reverses the current result
        """

        result = []
        for ch in s:
            if ch.isalpha():
                result.append(ch) 
            elif result and ch == "*":
                result.pop()
            elif ch == "#":
                result.extend(result)
            elif ch == "%":
                result.reverse()

        return "".join(result)