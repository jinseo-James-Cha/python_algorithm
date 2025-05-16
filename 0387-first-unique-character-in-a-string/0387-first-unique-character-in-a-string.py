class Solution(object):
    def firstUniqChar(self, s):
         # Create a list to store the frequency of each character
        frequency = [0] * 26  # Assuming only lowercase letters

        # Step 1: Count the frequency of each character
        for char in s:
            frequency[ord(char) - ord('a')] += 1  # Map 'a' to 0, 'b' to 1, ..., 'z' to 25

        # Step 2: Find the first character with a frequency of 1
        for index, char in enumerate(s):
            if frequency[ord(char) - ord('a')] == 1:
                return index  # Return the index of the first unique character

        # Step 3: If no unique character is found, return -1
        return -1

# 1 <= s.length <= 10**5

# TLE caused
# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         # using built in functions
#         d = {}
#         for i in range(len(s)):
#             if s[i] in d and len(d[s[i]]) >= 2:
#                 continue
#             d[s[i]] = d.get(s[i], []) + [i]
        
#         for v in d.values():
#             if len(v) == 1:
#                 return v[0]

#         return -1
        