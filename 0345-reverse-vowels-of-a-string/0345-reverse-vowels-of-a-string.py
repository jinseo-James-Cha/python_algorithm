class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        stack = []
        
        res = [None] * len(s)
        
        for i, ch in enumerate(s):
            if ch in vowels:
                stack.append(ch)
            else:
                res[i] = ch
        
        for i,a in enumerate(res):
            if a == None:
                res[i] = stack.pop()
        
        return "".join(res)

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        stack_vowels = []

        for ch in s:
            if ch in vowels:
                stack_vowels.append(ch)
        
        
        # IceCreAm
        # vowels [I, e, e, A]
        res = ""
        for ch in s:
            if ch not in vowels:
                res += ch
            else:
                v = stack_vowels.pop()
                res += v
        
        return res