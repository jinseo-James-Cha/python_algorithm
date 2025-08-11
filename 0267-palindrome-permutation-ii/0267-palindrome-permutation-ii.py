class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        d = {}
        for letter in s:
            d[letter] = d.get(letter, 0) + 1  # 이 부분 추가

        is_even_length = len(s) % 2 == 0
        odd_found = 0
        mid_char = ""

        for k, v in d.items():
            if v % 2 != 0:
                if is_even_length:
                    return []
                odd_found += 1
                mid_char = k
                if odd_found > 1:
                    return []

         # 3. 절반 문자열로 백트래킹 준비
        half_chars = []
        for char, count in d.items():
            half_chars.extend([char] * (count // 2))

        res = []
        used = [False] * len(half_chars)

        def backtrack(path):
            if len(path) == len(half_chars):
                half_str = "".join(path)
                res.append(half_str + mid_char + half_str[::-1])
                return

            for i in range(len(half_chars)):
                if used[i]:
                    continue
                if i > 0 and half_chars[i] == half_chars[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(half_chars[i])
                backtrack(path)
                path.pop()                       
                used[i] = False

        backtrack([])
        return res
        
