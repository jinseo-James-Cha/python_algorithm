class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0

        # Step 1: Iterate through each pair of words
        for i in range(n):
            for j in range(i + 1, n):
                str1 = words[i]
                str2 = words[j]

                # Step 2: Skip if the first string is larger than the second
                if len(str1) > len(str2):
                    continue

                # Step 3: Check if str1 is both the prefix and suffix of str2
                if str2.startswith(str1) and str2.endswith(str1):
                    count += 1

        # Step 4: Return the total count of prefix-suffix pairs
        return count

# 1 <= words.length <= 50
# O(N**2) is possible?!
# class Solution:
#     def countPrefixSuffixPairs(self, words: List[str]) -> int:
#         def isPrefixAndSuffix(str1: str, str2: str) -> bool:
#             if str1 in str2 and str2.index(str1) == 0:
#                 if str1[::-1] in str2[::-1] and str2[::-1].index(str1[::-1]) == 0:
#                     return True
#             return False

#         count = 0
#         for i in range(len(words) - 1):
#             for j in range(i +1, len(words)):
#                 if isPrefixAndSuffix(words[i], words[j]):
#                     count += 1
#         return count
        