
from typing import List

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

# Brute Force
# time complexity: O(n^2)
# space complexity: O(1)
# class Solution:
#     def canAttendMeetings(self, intervals: List[Interval]) -> bool:
#         for i in range(len(intervals)):
#             curr_start = intervals[i].start
#             curr_end = intervals[i].end
#             for j in range(i+1, len(intervals)):
#                 if intervals[j].start >= curr_start and intervals[j].start < curr_end:
#                     return False

#         return True

# Sorting
# time complexity: O(nlogn)
# space complexity: O(1) or O(n)
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True

# Test
intervals = [Interval(0,30), Interval(5,10), Interval(15,20)]
sol = Solution()
print(sol.canAttendMeetings(intervals)) # Expect False