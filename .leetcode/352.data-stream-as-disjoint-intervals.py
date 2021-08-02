# @lc app=leetcode id=352 lang=python3
#
# [352] Data Stream as Disjoint Intervals
#
# https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/
#
# algorithms
# Hard (49.21%)
# Likes:    511
# Dislikes: 123
# Total Accepted:    44.4K
# Total Submissions: 90.1K
# Testcase Example:  '["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"]\n' +
#   '[[],[1],[],[3],[],[7],[],[2],[],[6],[]]'
#
# Given a data stream input of non-negative integers a1, a2, ..., an, summarize
# the numbers seen so far as a list of disjoint intervals.
#
# Implement the SummaryRanges class:
#
#
# SummaryRanges() Initializes the object with an empty stream.
# void addNum(int val) Adds the integer val to the stream.
# int[][] getIntervals() Returns a summary of the integers in the stream
# currently as a list of disjoint intervals [starti, endi].
#
#
#
# Example 1:
#
#
# Input
# ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals",
# "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
# [[], [1], [], [3], [], [7], [], [2], [], [6], []]
# Output
# [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7,
# 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]
#
# Explanation
# SummaryRanges summaryRanges = new SummaryRanges();
# summaryRanges.addNum(1);      // arr = [1]
# summaryRanges.getIntervals(); // return [[1, 1]]
# summaryRanges.addNum(3);      // arr = [1, 3]
# summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
# summaryRanges.addNum(7);      // arr = [1, 3, 7]
# summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
# summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
# summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
# summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
# summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
#
#
#
# Constraints:
#
#
# 0 <= val <= 10^4
# At most 3 * 10^4 calls will be made to addNum and getIntervals.
#
#
#
# Follow up: What if there are lots of merges and the number of disjoint
# intervals is small compared to the size of the data stream?
#
#

# @lc tags=binary-search;ordered-map

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个非负数数据流，转化为不相交的间隔的格式。
# 直接线段树。
# 这个实现比较糟糕。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Segment:
    def __init__(self, l, r, lp=None, rp=None, fp=None) -> None:
        self.l = l
        self.r = r
        self.lp = lp
        self.rp = rp
        self.fp = fp


class SummaryRanges:
    def __init__(self):
        self.root = None

    def addNum(self, val: int) -> None:
        if not self.root:
            self.root = Segment(val, val)
            return
        p = self.root
        while True:
            if p.l <= val <= p.r:
                return
            elif val < p.l:
                if not p.lp:
                    p.lp = Segment(val, val, fp=p)
                    break
                p = p.lp
            else:
                if not p.rp:
                    p.rp = Segment(val, val, fp=p)
                    break
                p = p.rp
        while p:
            if p.lp and p.lp.r + 1 >= p.l:
                p.l = p.lp.l
                p.lp = p.lp.lp
                p = p.fp
                continue
            if p.rp and p.rp.l - 1 <= p.r:
                p.r = p.rp.r
                p.rp = p.rp.rp
                p = p.fp
                continue
            break

    def getIntervals(self) -> List[List[int]]:

        r = []

        def recursion(p: Segment):
            if not p:
                return
            recursion(p.lp)
            if r and r[-1][1] + 1 >= p.l:
                r[-1][1] = p.r
            else:
                r.append([p.l, p.r])
            recursion(p.rp)

        recursion(self.root)
        return r


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    o = SummaryRanges()
    o.addNum(1)
    print(o.getIntervals())
    o.addNum(3)
    print(o.getIntervals())
    o.addNum(7)
    print(o.getIntervals())
    o.addNum(2)
    print(o.getIntervals())
    o.addNum(6)
    print(o.getIntervals())

    pass
# @lc main=end