from collections import defaultdict, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # alien dictionary == words
        # ["wrt","wrf","er","ett","rftt"]
        # wrt, wrf => t < f => tf
        # er, ett => r < t => rtf
        # w, e, r => w < e < r => wertf

        # - w e r
        # rt rf r tt ftt
        # - t f
        # t f "" t tt


        # if already registed -> invalid -> return ""

        # kahn's algorithm ? topological sorted ?
        adj_list = defaultdict(set)
        in_degree = {}
        for word in words:
            for c in word:
                in_degree[c] = 0
        
        # zip은 짧은쪽 기준으로 알아서 멈춤 따라서 앞뒤로 쌍을 묶어서 끝까지 감.
        for first_word, second_word in zip(words, words[1:]):
            for first_word_letter, second_word_letter in zip(first_word, second_word):
                # order found
                if first_word_letter != second_word_letter:
                    if second_word_letter not in adj_list[first_word_letter]:
                        adj_list[first_word_letter].add(second_word_letter)
                        in_degree[second_word_letter] += 1
                    break
            # for문안에서 break없이 종료되었으면 else문 실행
            # for문 다 돌았는데 다 똑같다면 else실행
            # 앞 단어가 다음 단어보다 길다? ascending order아니다 -> return ""
            else:
                if len(second_word) < len(first_word):
                    return ""
        
        # Kahn's algorithm - topological sort
        res = []
        queue = deque()
        for c in in_degree:
            if in_degree[c] == 0:
                queue.append(c)
        
        while queue:
            c = queue.popleft()
            res.append(c)
            for neighbor in adj_list[c]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(res) < len(in_degree):
            return ""
        
        return "".join(res)
