class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # sliding window 

        VOWELS = {'a', 'e', 'i', 'o', 'u'} # only lower case?
        # initial with k 
        curr_vowels = 0
        for i in range(k):
            if s[i] in VOWELS:
                curr_vowels += 1

        max_vowels = curr_vowels
        for i in range(k, len(s)):
            # new character
            if s[i] in VOWELS:
                curr_vowels += 1

            # old character
            if s[i-k] in VOWELS:
                curr_vowels -= 1
            
            max_vowels = max(max_vowels, curr_vowels)
        return max_vowels
            