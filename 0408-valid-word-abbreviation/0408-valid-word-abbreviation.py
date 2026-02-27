# beat 100%
# O(N)
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        if alpha?
          if not the same? return False
          left += 1
          right += 1
          continue
        
        if right is 0? return False

        starting_num = 0
        for right < len(abbr) and not abbr[right].isalpha:
            starting_num *= 10
            starting_num += abbr[right]
            right += 1
        
        left += int_right_num
        if left > len(word):
            return False

        Time complexity: O(m) => m == len(abbr)
        Space : O(1)

        """
        left = right = 0
        while left < len(word) and right < len(abbr):
            if abbr[right].isalpha():
                if word[left] != abbr[right]:
                    return False
                left += 1
                right += 1
                continue
                
            if  abbr[right] == "0":
                return False

            int_right_num = 0
            while right < len(abbr) and not abbr[right].isalpha():
                int_right_num *= 10
                int_right_num += int(abbr[right])
                right += 1
            
            left += int_right_num
            if left > len(word):
                return False

        if left == len(word) and right == len(abbr):
            return True
        return False