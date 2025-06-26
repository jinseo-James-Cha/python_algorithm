class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # equal len s1 == s2
        # bank  kanb
        # 0123  3120 -> True

        # attack defend
        # 012345 012345

        # 1 is different means 2 letters index are different
        # get difference number and return count <= 2

        # edge case
        # 1. acac acbb -> we need to save the letter as well?
        # 2. aa   ac   -> we need to use set to remove and check whether its empty?
        
        different_flag = False
        saved_s1_letter = set()
        saved_s2_letter = set()
        for i in range(len(s1)): # len s1 == s2
            if s1[i] != s2[i]:
                if different_flag:
                    return False

                if saved_s1_letter and saved_s2_letter:
                    if s2[i] not in saved_s1_letter or s1[i] not in saved_s2_letter:
                        return False
                    else:
                        saved_s1_letter.remove(s2[i])
                        saved_s2_letter.remove(s1[i])
                        different_flag = True
                else:
                    saved_s1_letter.add(s1[i])
                    saved_s2_letter.add(s2[i])
        
        return not saved_s1_letter and not saved_s2_letter