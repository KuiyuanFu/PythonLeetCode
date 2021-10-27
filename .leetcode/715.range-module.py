# @lc app=leetcode id=715 lang=python3
#
# [715] Range Module
#
# https://leetcode.com/problems/range-module/description/
#
# algorithms
# Hard (42.22%)
# Likes:    812
# Dislikes: 60
# Total Accepted:    37.3K
# Total Submissions: 87.6K
# Testcase Example:  '["RangeModule","addRange","removeRange","queryRange","queryRange","queryRange"]\n' +
# '[[],[10,20],[14,16],[10,14],[13,15],[16,17]]'
#
# A Range Module is a module that tracks ranges of numbers. Design a data
# structure to track the ranges represented as half-open intervals and query
# about them.
#
# A half-open interval [left, right) denotes all the real numbers x where left
# <= x < right.
#
# Implement the RangeModule class:
#
#
# RangeModule() Initializes the object of the data structure.
# void addRange(int left, int right) Adds the half-open interval [left, right),
# tracking every real number in that interval. Adding an interval that
# partially overlaps with currently tracked numbers should add any numbers in
# the interval [left, right) that are not already tracked.
# boolean queryRange(int left, int right) Returns true if every real number in
# the interval [left, right) is currently being tracked, and false
# otherwise.
# void removeRange(int left, int right) Stops tracking every real number
# currently being tracked in the half-open interval [left, right).
#
#
#
# Example 1:
#
#
# Input
# ["RangeModule", "addRange", "removeRange", "queryRange", "queryRange",
# "queryRange"]
# [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
# Output
# [null, null, null, true, false, true]
#
# Explanation
# RangeModule rangeModule = new RangeModule();
# rangeModule.addRange(10, 20);
# rangeModule.removeRange(14, 16);
# rangeModule.queryRange(10, 14); // return True,(Every number in [10, 14) is
# being tracked)
# rangeModule.queryRange(13, 15); // return False,(Numbers like 14, 14.03,
# 14.17 in [13, 15) are not being tracked)
# rangeModule.queryRange(16, 17); // return True, (The number 16 in [16, 17) is
# still being tracked, despite the remove operation)
#
#
#
# Constraints:
#
#
# 1 <= left < right <= 10^9
# At most 10^4 calls will be made to addRange, queryRange, and removeRange.
#
#
#

# @lc tags=segment-tree;ordered-map

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 闭开区域模型。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class RangeModule:
    def __init__(self):
        self.ranges = [[-1, -1]]

    def addRange(self, left: int, right: int) -> None:
        idxL = bisect_left(self.ranges, [left + 1, 0]) - 1

        rangeT = self.ranges[idxL]
        # Contain the new range, do nothing.
        if rangeT[1] >= right:
            pass
        else:
            # not overlap
            if rangeT[1] < left:
                idxL += 1
            else:
                left = min(left, rangeT[0])
                right = max(right, rangeT[1])

            # Merge the next overlap range.
            idxR = idxL
            while idxR < len(self.ranges):
                if self.ranges[idxR][0] <= right:

                    right = max(right, self.ranges[idxR][1])
                    idxR += 1
                else:
                    break

            self.ranges = self.ranges[:idxL] + [[left, right]
                                                ] + self.ranges[idxR:]

    def queryRange(self, left: int, right: int) -> bool:
        idxL = bisect_left(self.ranges, [left + 1, 0]) - 1
        rangeT = self.ranges[idxL]
        return rangeT[0] <= left and rangeT[1] >= right

    def removeRange(self, left: int, right: int) -> None:

        idxL = bisect_left(self.ranges, [left + 1, 0]) - 1
        rangeT = self.ranges[idxL]
        # RangeT contain the remove range, devide to two ranges.
        if rangeT[1] >= right:
            rs = []
            if rangeT[0] != left:
                rs.append([rangeT[0], left])
            if rangeT[1] >= right:
                rs.append([right, rangeT[1]])
            self.ranges = self.ranges[:idxL] + rs + self.ranges[idxL + 1:]
        else:
            # overlap
            if rangeT[1] > left:
                rangeT[1] = left
                if rangeT[0] == rangeT[1]:
                    idxL -= 1
            idxR = idxL + 1
            while idxR < len(self.ranges):
                self.ranges[idxR][0] = max(self.ranges[idxR][0], right)
                if self.ranges[idxR][1] >= right:
                    break
                idxR += 1
            self.ranges = self.ranges[:idxL + 1] + self.ranges[idxR:]


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    o = RangeModule()
    print(o.addRange(5, 8))
    print(o.queryRange(3, 4))
    print(o.removeRange(5, 6))
    print(o.removeRange(3, 6))
    print(o.addRange(1, 3))
    print(o.queryRange(2, 3))
    print(o.addRange(4, 8))
    print(o.queryRange(2, 3))
    print(o.removeRange(4, 9))
    print()
    o = RangeModule()
    print(o.removeRange(7, 8))
    print(o.addRange(4, 10))
    print(o.queryRange(7, 8))
    print(o.queryRange(5, 7))
    print(o.queryRange(1, 8))
    print(o.addRange(2, 6))
    print(o.addRange(4, 6))
    print(o.removeRange(3, 4))
    print(o.removeRange(5, 7))
    pass
# @lc main=end