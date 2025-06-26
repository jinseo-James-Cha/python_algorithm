from collections import defaultdict

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        n = len(word)
        res = 0

        i = 0
        while i < n:
            # 모음 시작 구간 찾기
            if word[i] in vowels:
                j = i
                while j < n and word[j] in vowels:
                    j += 1
                # word[i:j] 는 모음으로만 구성된 substring
                res += self.count_valid_substrings(word[i:j])
                i = j
            else:
                i += 1
        return res

    def count_valid_substrings(self, s: str) -> int:
        # 모음 다섯 개가 모두 나오는 substring 수 세기 (O(n))
        count = 0
        freq = defaultdict(int)
        left = 0
        unique = 0

        for right in range(len(s)):
            if freq[s[right]] == 0:
                unique += 1
            freq[s[right]] += 1

            # 모든 다섯 모음을 다 가질 때까지 왼쪽 확장
            while unique == 5:
                count += len(s) - right  # 오른쪽 확장에 따라 가능한 모든 substring 수
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    unique -= 1
                left += 1
        return count

            
            



# O(n^2)
# class Solution:
#     def countVowelSubstrings(self, word: str) -> int:
#         # brute force
#         vowels = {'a', 'e', 'i', 'o', 'u'}
#         vowel_set = set()
#         res = 0
#         for i in range(len(word) - 4): # 6 - 4 = 2 -> 0 1
#             vowel_set = set()
#             if word[i] not in vowels:
#                 continue
#             for j in range(i, len(word)):
#                 if word[j] in vowels:
#                     vowel_set.add(word[j])
#                 else:
#                     break
                
#                 if len(vowel_set) >= 5:
#                     res += 1
#         return res

