# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
# https://leetcode.com/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (45.46%)
# Likes:    2543
# Dislikes: 73
# Total Accepted:    163.3K
# Total Submissions: 358.3K
# Testcase Example:  '[[1,2],[2,3],[3,4],[1,3]]'
#
# Given an array of intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of intervals you need to remove to make the rest of
# the intervals non-overlapping.
#
#
# Example 1:
#
#
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are
# non-overlapping.
#
#
# Example 2:
#
#
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals
# non-overlapping.
#
#
# Example 3:
#
#
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're
# already non-overlapping.
#
#
#
# Constraints:
#
#
# 1 <= intervals.length <= 10^5
# intervals[i].length == 2
# -5 * 10^4 <= starti < endi <= 5 * 10^4
#
#
#

# @lc tags=greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将一些列区间转化为不重叠的区间，问最少需要去掉多少个区间。
# 贪心，排序后遍历，重叠保留右侧最近的。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = 0
        preRight = intervals[0][0] - 1
        for l, r in intervals:
            if l < preRight:
                n += 1
                preRight = min(preRight, r)
            else:
                preRight = r
        return n
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('intervals = [[1,2],[2,3],[3,4],[1,3]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(
        str(Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1,
                                                                       3]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('intervals = [[1,2],[1,2],[1,2]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('intervals = [[1,2],[2,3]]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().eraseOverlapIntervals([[1, 2], [2, 3]])))
    print()

    pass
# @lc main=end