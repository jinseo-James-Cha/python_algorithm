# 1 <= words.length <= 50
# O(N**2) is possible?!
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1: str, str2: str) -> bool:
            if str1 in str2 and str2.index(str1) == 0:
                if str1[::-1] in str2[::-1] and str2[::-1].index(str1[::-1]) == 0:
                    return True
            return False

        count = 0
        for i in range(len(words) - 1):
            for j in range(i +1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        return count
        