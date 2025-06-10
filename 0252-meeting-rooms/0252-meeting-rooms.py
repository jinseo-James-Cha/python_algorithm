# v2 sorting 
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key= lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][0] < intervals[i+1][0] and intervals[i][1] <= intervals[i+1][0]:
                continue
            else:
                return False
        return True

# Brute force?! beat 5.49
# let me optimize 
# class Solution:
#     def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # what about [3,5], [5,7] is True
        # uhm.. should only check between the nums

        # wrong answer at [[6,10],[13,14],[12,14]]
        # cuz 13,14 no checked..
        # checked = set()
        # for start, end in intervals:
        #     for i in range(start, end):
        #         if i in checked:
        #             return False
        #         checked.add(i)
        # return True