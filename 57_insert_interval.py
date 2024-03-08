class Solution:
    # IDEA
    # if interval before newInterval, add to result
    # if interval overlap with newInterval, merge into newInterval
    # when interval becomes not overlapped, we add newInterval to res
    # and then add the current interval
    # add rest of the intervals.

    # finally, if inserted = False, meaning we haven't yet add the newInterval yet,
    # we add the newInterval
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        inserted = False
        for interval in intervals:
            if interval[1] < newInterval[0]:
                result.append(interval)
            elif interval[0] > newInterval[1]:
                if not inserted:
                    result.append(newInterval)
                    inserted = True
                result.append(interval)
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        if not inserted:
            result.append(newInterval)
        return result