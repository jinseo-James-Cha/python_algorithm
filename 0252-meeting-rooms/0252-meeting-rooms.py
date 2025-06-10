class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # what about [3,5], [5,7] is True
        # uhm.. should only check between the nums

        # wrong answer at [[6,10],[13,14],[12,14]]
        # cuz 13,14 no checked..
        checked = set()
        for start, end in intervals:
            for i in range(start, end):
                if i in checked:
                    return False
                checked.add(i)
        return True