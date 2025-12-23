from collections import Counter, defaultdict
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # close ==> if you can attain one from the other 
        
        # operation 1-> swap any two exisiting char 
        # => a b cd e ->  a e cd b
        
        # operation 2-> transform every occurrence of one existing char into another existing char 
        # => aa c abb -> bb c baa


        # abc , bca
        # a bc -> a cb
        # a c b -> b c a == bca

        # c a bbb a
        # a bb ccc

        # if count is the same we can make CLOSE?!
        if len(word1) != len(word2):
            return False
        
        if set(word1) != set(word2):
            return False


        return sorted(Counter(word1).values()) == sorted(Counter(word2).values())

        