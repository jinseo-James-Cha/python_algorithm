from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = Counter(magazine)
        for c in ransomNote:
            if c not in counts:
                return False
            
            counts[c] -= 1
            if counts[c] < 0:
                return False
        return True













        dict_ransomNote = {}
        for r in ransomNote:
            dict_ransomNote[r] = 1 + dict_ransomNote.get(r, 0)
            # if not r in dict_ransomNote:
            #     dict_ransomNote[r] = 1
            # else:
            #     dict_ransomNote[r] += 1

    

        for key, value in dict_ransomNote.items():
            if key in magazine:
                if dict_ransomNote[key] <= magazine.count(key):
                    continue
                else:
                    return False
            else:
                return False

        return True
        