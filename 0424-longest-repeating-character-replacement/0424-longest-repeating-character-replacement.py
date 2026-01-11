class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # I can change any character and change it to any other up
        """

        ABAB
        L
        F
        """

        all_letters = set(s)
        max_length = 0
        for letter in all_letters:
            start = 0
            count = 0
            for end in range(len(s)):
                if s[end] == letter:
                    count += 1
                
                while not end - start +1 - count <= k:
                    if s[start] == letter:
                        count -= 1
                    start+=1
                
                max_length = max(max_length, end - start +1)
        return max_length