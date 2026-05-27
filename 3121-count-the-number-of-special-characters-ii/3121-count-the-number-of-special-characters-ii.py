class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        """
        a a A b c B C
          - -
              -   -
                -   -

        lowercase and then uppercase

        so check when uppercase appears -> lower is saved?
        """
        lowercases = {}
        uppercases = {}
        for i, ch in enumerate(word):
            if ch.islower():
                lowercases[ch] = i
            elif ch not in uppercases:
                uppercases[ch] = i

        specials = 0
        for i in range(26):
            curr_alphabet = chr(ord('a') + i)
            if curr_alphabet in lowercases and curr_alphabet.upper() in uppercases and lowercases[curr_alphabet] < uppercases[curr_alphabet.upper()]:
                specials += 1
        return specials