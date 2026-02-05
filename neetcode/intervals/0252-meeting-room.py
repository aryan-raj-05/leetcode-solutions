from typing import List

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        s_i = sorted(intervals, key=lambda i : i.start)

        for i in range(1, len(s_i)):
            if s_i[i - 1].end > s_i[i].start:
                return False

        return True
