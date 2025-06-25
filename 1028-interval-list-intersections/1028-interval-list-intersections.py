class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # closed intervals -> included
        
        # # sort by start
        # firstList.sort(key= lambda x: x[0])
        # secondList.sort(key= lambda x: x[0])

        intersection = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            # set A and B by start value
            l = max(firstList[i][0], secondList[j][0])
            h = min(firstList[i][1], secondList[j][1])

            if l <= h:
                intersection.append([l, h])
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return intersection
