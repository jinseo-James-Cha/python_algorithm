class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        Using a word Balloon to cover the given text
        and return how many Balloon I need to use.

        - lowercase alphabet only
        - order doesn't matter
        """

        original = {'b':1, 'a': 1, 'l': 2, 'o':2, 'n':1}
        letter_cnt = defaultdict(int)
        for ch in text:
            if ch in original:
                letter_cnt[ch] += 1
        
        res = float('inf')
        for ch, cnt in original.items():
            res = min(res, letter_cnt[ch] // cnt)

        return res
