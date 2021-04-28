# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Medium (35.30%)
# Likes:    2773
# Dislikes: 241
# Total Accepted:    344.3K
# Total Submissions: 973.8K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their
# start times.
#
#
# Example 1:
#
#
# Input: intervals = [[1,3],[6,9]], [2,5]
# Output: [[1,5],[6,9]]
#
#
# Example 2:
#
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
#
# Example 3:
#
#
# Input: intervals = [], [5,7]
# Output: [[5,7]]
#
#
# Example 4:
#
#
# Input: intervals = [[1,5]], [2,3]
# Output: [[1,5]]
#
#
# Example 5:
#
#
# Input: intervals = [[1,5]], [2,7]
# Output: [[1,7]]
#
#
#
# Constraints:
#
#
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= intervals[i][0] <= intervals[i][1] <= 10^5
# intervals is sorted by intervals[i][0] in ascending order.
# newInterval.length == 2
# 0 <= newInterval[0] <= newInterval[1] <= 10^5
#
#
#

# @lc tags=array;sort

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 插入一个时间段到有序的时间段内，若可以合并则合并。
# 主要问题是，需要向前方和后方，两个方向合并。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        import bisect
        index = bisect.bisect(intervals, newInterval)

        l = index - 1
        while l >= 0 and intervals[l][1] >= newInterval[0]:
            newInterval[0] = min(newInterval[0], intervals[l][0])
            newInterval[1] = max(newInterval[1], intervals[l][1])
            l -= 1
        r = index
        while r < len(intervals) and intervals[r][0] <= newInterval[1]:
            newInterval[1] = max(newInterval[1], intervals[r][0])
            newInterval[1] = max(newInterval[1], intervals[r][1])
            r += 1
        return intervals[:l + 1] + [newInterval] + intervals[r:]

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('intervals = [[1,3],[6,9]], [2,5]')
    print('Output :')
    print(str(Solution().insert([[1, 3], [6, 9]], [2, 5])))
    print('Exception :')
    print('[[1,5],[6,9]]')
    print()

    print('Example 2:')
    print('Input : ')
    print('intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]')
    print('Output :')
    print(
        str(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
                              [4, 8])))
    print('Exception :')
    print('[[1,2],[3,10],[12,16]]')
    print()

    print('Example 3:')
    print('Input : ')
    print('intervals = [], [5,7]')
    print('Output :')
    print(str(Solution().insert([], [5, 7])))
    print('Exception :')
    print('[[5,7]]')
    print()

    print('Example 4:')
    print('Input : ')
    print('intervals = [[1,5]], [2,3]')
    print('Output :')
    print(str(Solution().insert([[1, 5]], [2, 3])))
    print('Exception :')
    print('[[1,5]]')
    print()

    print('Example 5:')
    print('Input : ')
    print('intervals = [[1,5]], [2,7]')
    print('Output :')
    print(str(Solution().insert([[1, 5]], [2, 7])))
    print('Exception :')
    print('[[1,7]]')
    print()

    pass
# @lc main=end