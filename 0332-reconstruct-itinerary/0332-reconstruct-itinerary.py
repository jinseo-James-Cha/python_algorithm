class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # tickets[i] = [from, to]
        # JFK -> ....lexical order

        # JFK - MUC
        # MUC - LHR
        # LHR - SFO
        # SFO - SJC
        # can be done in adjacent list

        # JFK - SFO!, ATL!
        # SFO - ATL!
        # ATL - JFK!, SFO!
        # add set((dep, arr)) in visited -> return res

        def dfs(departure):
            while adjacent_list[departure]:
                dfs(adjacent_list[departure].pop())
            res.append(departure)

        adjacent_list = defaultdict(list)
        for d, a in tickets:
            adjacent_list[d].append(a)
        
        for k in adjacent_list:
            adjacent_list[k].sort(reverse=True)

        res = []
        dfs('JFK')
        return res[::-1]
        

