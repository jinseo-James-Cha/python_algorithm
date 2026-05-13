class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def include_common_letter(w1, w2):
            for ch in w1:
                if ch in w2:
                    return True
            return False
        
        maximum_length = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not include_common_letter(words[i], words[j]):
                    maximum_length = max(maximum_length, len(words[i]) * len(words[j]))
        return maximum_length

