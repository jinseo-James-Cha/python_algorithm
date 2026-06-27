class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        1. All capital?
        2. all lowercase?
        3. first is capital?
        """
        all_capital = True
        for ch in word:
            if ch.islower():
                all_capital = False
        
        if all_capital:
            return True
        
        
        all_lowercase = True
        for ch in word:
            if ch.isupper():
                all_lowercase = False
        
        if all_lowercase:
            return True

        first_only_capital = word[0].isupper()
        if first_only_capital:
            for ch in word[1:]:
                if ch.isupper():
                    first_only_capital = False
        if first_only_capital:
            return True
        
        return False

