from collections import defaultdict, Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # sliding window
        if not s or not words:
            return []
        
        word_len = len(words[0])      # 각 단어의 길이
        word_count = len(words)       # 단어의 개수
        total_len = word_len * word_count  # 모든 단어를 붙인 문자열의 길이
        word_map = Counter(words)     # 각 단어 등장 횟수
        res = []

        # 시작 인덱스를 0, 1, ..., word_len-1 로 나누어 검사
        for i in range(word_len):
            left = i   # 윈도우의 시작점
            seen = Counter()
            count = 0  # 현재 윈도우 내 단어 수
            
            # 오른쪽 포인터를 word_len씩 이동
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]
                
                if word in word_map:
                    seen[word] += 1
                    count += 1

                    # 단어가 너무 많이 등장하면 왼쪽 포인터를 이동
                    while seen[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    # 모든 단어가 매칭된 경우
                    if count == word_count:
                        res.append(left)
                        
                        # 윈도우를 한 단어 오른쪽으로 이동
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    # 단어가 목록에 없으면 초기화
                    seen.clear()
                    count = 0
                    left = right + word_len

        return res

        # brute force -> TLE
        m, n  = len(words), len(words[0])
        res = []
        counts = Counter(words)
        for i in range(0, len(s) - m*n + 1):
            curr_total_s = s[i:i+m*n]
            
            j = 0
            c_copy = counts.copy()
            while len(curr_total_s) > j:
                curr_s = curr_total_s[j:j+n]
                if curr_s in c_copy:
                    c_copy[curr_s] -= 1
                    if c_copy[curr_s] == 0:
                        del c_copy[curr_s]
                else:
                    break
                j += n
            
            if not c_copy:
                res.append(i)
        return res