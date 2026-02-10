class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        s_list = list(s)
        vowels = set("aeiouAEIOU")

        while left < right:
            while left < right and s_list[left] not in vowels:
                left += 1
            
            while left < right and s_list[right] not in vowels:
                right -= 1

            s_list[left], s_list[right] = s_list[right], s_list[left]

            left += 1
            right -= 1
        return "".join(s_list)


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