from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        n people
        0 1 2 3 ... n-1

        n tickets

        2 3 2 and k = 2
            S

        1second 1 3 2 -> 3 2 1
        2second 2 2 1 -> 2 1 2
        ...
        kth person's ticket is done.. -> 6seconds
        """
        # double ended queue
        queue = deque()
        for i, ticket in enumerate(tickets):
            queue.append((i, ticket))

        seconds = 0
        while queue:
            person, curr_ticket = queue.popleft()
            curr_ticket -= 1

            seconds += 1

            if curr_ticket == 0:
                if person == k:
                    break
            else:
                queue.append((person, curr_ticket))
        return seconds
            
