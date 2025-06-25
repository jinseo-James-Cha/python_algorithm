class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        # words separated by space -> sentence.split(" ")
        # lower, upper case letters
        # Goat Latin ?!
        # case 1. start with [aeiou] abc -> abc + ma
        # case 2. start with not[aeiou] bca -> cab + ma
        # case 3. add a on each words
        # index 0 -> a 
        # index 1 -> aa

        vowels = {'a', 'e', 'i', 'o', 'u'} # include uppercases
        res = []
        endA = 'a'
        for word in sentence.split(" "):
            firstLetter = word[0]

            # case 1
            # if firstLetter.lower() in vowels:
            #     word += "ma"
            # case 2
            if not firstLetter.lower() in vowels: 
                word = word[1:] + firstLetter
            
            # case 1 & case 2
            word += "ma"
            
            word += endA
            endA += "a"
            res.append(word)
        return " ".join(res)
        
            