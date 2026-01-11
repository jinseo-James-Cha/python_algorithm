class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        frequency_map = {}
        max_frequency = 0
        
        max_length = 0

        for right in range(len(s)):
            frequency_map[s[right]] = frequency_map.get(s[right], 0) + 1

            max_frequency = max(max_frequency, frequency_map[s[right]])

            is_valid = (right - left + 1 - max_frequency <= k)
            if not is_valid:
                frequency_map[s[left]] -= 1
                left += 1
            
            max_length = right - left + 1
        return max_length