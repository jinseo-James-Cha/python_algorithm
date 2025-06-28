class Solution:
    def reverseVowels(self, s: str) -> str:
        found_index = []
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                found_index.append(i)

        left = 0
        right = len(found_index) - 1
        array_s = list(s)
        while left < right:
            array_s[found_index[left]], array_s[found_index[right]] = array_s[found_index[right]], array_s[found_index[left]]
            left += 1
            right -= 1
        return ''.join(array_s)