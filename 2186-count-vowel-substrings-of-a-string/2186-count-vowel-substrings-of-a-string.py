class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        # brute force
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_set = set()
        res = 0
        for i in range(len(word) - 4): # 6 - 4 = 2 -> 0 1
            vowel_set = set()
            if word[i] not in vowels:
                continue
            for j in range(i, len(word)):
                if word[j] in vowels:
                    vowel_set.add(word[j])
                else:
                    break
                
                if len(vowel_set) >= 5:
                    res += 1
        return res



        # two pointer or sliding window.
        # dynamic sliding window len >= 5

        # only consists of aeiou and has all five
        # sliding_window = set()

