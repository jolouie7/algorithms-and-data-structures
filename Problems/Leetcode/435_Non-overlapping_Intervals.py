# https://leetcode.com/problems/non-overlapping-intervals/
# 435. Non-overlapping Intervals


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort in ascending order by start
        # remove the interal with longer ending time

        if len(intervals) == 0 or len(intervals[0]) == 0:
            return 0

        intervals.sort(key=lambda x: x[0])
        pre = intervals[0]
        count = 0

        for i in range(1, len(intervals)):
            #check if there is overlap
            if pre[1] > intervals[i][0]:
                #check to see which has a bigger end time
                count += 1
                if pre[1] > intervals[i][1]:
                    pre = intervals[i]
            else:
                pre = intervals[i]

        return count

# Time: O(N log N), because of sorting
# Space: O(1)