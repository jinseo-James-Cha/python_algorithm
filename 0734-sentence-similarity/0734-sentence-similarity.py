# defaultdict(set)
# 'truck': {'car'}, 'car': {'automobile', 'vehicle', 'wagon', 'auto', 'truck'},
# 'wagon': {'car'}, 'automobile': {'car'}, 'auto': {'car'}, 'vehicle': {'car'}

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        # this is the kick
        wordToSimilarWords = defaultdict(set)
        for x, y in similarPairs:
            wordToSimilarWords[x].add(y)
            wordToSimilarWords[y].add(x)
        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i] or sentence2[i] in wordToSimilarWords[sentence1[i]]:
                continue
            return False
        return True

# My answer time : O(N^2) needs to optimize by choosing different data structure
# class Solution:
#     def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
#         s1_len = len(sentence1)
#         s2_len = len(sentence2)
#         if s1_len != s2_len:
#             return False
        
#         for i in range(s1_len):
#             # same word -> similar
#             if sentence1[i] == sentence2[i]:
#                 continue
#             else: # if its different
#                 flag = False
#                 for x, y in similarPairs:
#                     if (x == sentence1[i] and y == sentence2[i]) or (x == sentence2[i] and y == sentence1[i]):
#                         flag = True
#                 if not flag:
#                     return False
#         return True
        