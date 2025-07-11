class Solution:
    def removeVowels(self, s: str) -> str:
        res = ""
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for ch in s:
            if ch not in vowels:
                res += ch
        print(vowels)
        return res
