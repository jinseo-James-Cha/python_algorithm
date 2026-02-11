class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        numP, from, to = trips[i]


        sweep line algorithm
        """

        events = []
        for p, f, t in trips:
            events.append((f, p))
            events.append((t, -p))
        
        events.sort()

        curr_p = 0
        for point, score in events:
            curr_p += score
            if curr_p > capacity:
                return False

        return True