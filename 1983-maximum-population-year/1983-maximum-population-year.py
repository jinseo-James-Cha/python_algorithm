class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # b, d 
        # intervals!!!!!
        # sweep line algorithm?
        # close intervals -> start and end included !
        # but death - 1 is include -> half-open interval

        # sweep line algorithm
        # 1. divide by event
        # 2. sort event
        # 3. count num
        events = []
        for birth, death in logs:
            events.append((birth, 1))
            events.append((death, -1))
        
        events.sort()

        year = 0
        population = 0
        maximum_population = 0
        for k, v in events:
            population += v
            if population > maximum_population:
                maximum_population = population
                year = k
        return year
