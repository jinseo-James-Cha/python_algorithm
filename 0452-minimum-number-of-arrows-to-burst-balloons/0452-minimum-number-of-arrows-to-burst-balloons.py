class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #  B    B  B
        #  B  B    B 
        #  A  A A  A => return 4?

        points.sort(key=lambda x:x[1])

        arrows = 1
        curr_end = points[0][1]
        for start, end in points:
            if start > curr_end:
                arrows += 1
                curr_end = end
        return arrows



        """
        [[10,16],[2,8],[1,6],[7,12]]

                            - - - - - - - -
                    - - - - - - - -
          - - - - - - -
        - - - - - - 
        1 2       6 7 8    10    12       16
    curr1 2       0 1      2
    res           1               2
                   - -
                 - -
          -      -
        - -
        1 *2     3 *4 5
    curr-1-2->0 -1
    res       1
        """
        # events = []
        # for start, end points:
        #     events.append((start, -1))
        #     events.append((end, 1))
        
        # events.sort()

        # minimum_number_of_arrows = 0
        # curr_score = 0
        # idx = 0
        # while idx < len(events)
        #     x, score = events[i]
        #     if score == 1 and curr_score < 0: # which is closing, and need to shot
        #         minimum_number_of_arrows += 1
        #         curr_score = 0
        #     else:
        #         curr_score += score
        # return minimum_number_of_arrows
