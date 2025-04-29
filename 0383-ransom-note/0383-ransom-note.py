class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_ransomNote = {}
        for r in ransomNote:
            if not r in dict_ransomNote:
                dict_ransomNote[r] = 1
            else:
                dict_ransomNote[r] += 1

        for key, value in dict_ransomNote.items():
            if key in magazine:
                if dict_ransomNote[key] <= magazine.count(key):
                    continue
                else:
                    return False
            else:
                return False

        return True
        