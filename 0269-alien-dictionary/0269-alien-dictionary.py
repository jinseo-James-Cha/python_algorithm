from collections import defaultdict, deque, Counter
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # dictionary -> if letter the same, compare next letter
        adj_list = defaultdict(set)
        in_degree = Counter({w: 0 for word in words for w in word})

        for first_w, second_w in zip(words, words[1:]):
            for first_l, second_l in zip(first_w, second_w):
                if first_l != second_l:
                    if second_l not in adj_list[first_l]:
                        adj_list[first_l].add(second_l)
                        in_degree[second_l] += 1
                    break
            else:
                # cannot be longer letter in first_w if they all matched
                if len(first_w) > len(second_w):
                    return ""
        
        # initial data
        pq = deque([c for c in in_degree if in_degree[c] == 0])

        res = []
        while pq:
            node = pq.popleft()
            res.append(node)

            for neighbor in adj_list[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    pq.append(neighbor)

        # if there is a cycle
        if len(res) < len(in_degree):
            return ""
        
        return "".join(res)
