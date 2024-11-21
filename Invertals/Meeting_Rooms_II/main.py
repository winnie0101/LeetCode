from typing import List

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

# Min-Heap
# time complexity: O(nlogn)
# space complexity: O(n)
# class Solution:
#     def minMeetingRooms(self, intervals: List[Interval]) -> int:
#         intervals.sort(key=lambda i: i.start)
#         min_heap = []

#         for interval in intervals:
#             if min_heap and min_heap[0] <= interval.start:
#                 heapq.heappop(min_heap)
#             heapq.heappush(min_heap, interval.end)

#         return len(min_heap)

# Time Line Algo
# time complexity: O(nlogn)
# space complexity: O(n)
# class Solution:
#     def minMeetingRooms(self, intervals: List[Interval]) -> int:
#         room_dict = defaultdict(int)
#         for i in intervals:
#             room_dict[i.start] += 1 #開一個會議室
#             room_dict[i.end] -= 1 #關一個會議室
        
#         prev = 0
#         res = 0
#         # 計算這個時間點最多開了幾間會議室
#         for i in sorted(room_dict.keys()):
#             prev += room_dict[i]
#             res = max(res, prev)

#     return res


# Two Pointer
# time complexity: O(nlogn)
# space complexity: O(n)
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_time = sorted([i.start for i in intervals])
        end_time = sorted([i.end for i in intervals])

        res = count = 0
        s = e = 0
        while s < len(start_time):
            if start_time[s] < end_time[e]:
                # 有新會議開始且沒有舊會議結束，因此需要額外的會議室。
                s += 1
                count += 1
            else: 
                # 在新會議開始之前有舊會議結束，因此會議室-1
                e += 1
                count -= 1
            res = max(res, count)

        return res

