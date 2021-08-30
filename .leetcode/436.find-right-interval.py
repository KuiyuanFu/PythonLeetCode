# @lc app=leetcode id=436 lang=python3
#
# [436] Find Right Interval
#
# https://leetcode.com/problems/find-right-interval/description/
#
# algorithms
# Medium (48.83%)
# Likes:    862
# Dislikes: 209
# Total Accepted:    67.5K
# Total Submissions: 138.1K
# Testcase Example:  '[[1,2]]'
#
# You are given an array of intervals, where intervals[i] = [starti, endi] and
# each starti is unique.
#
# The right interval for an interval i is an interval j such that startj >=
# endi and startj is minimized.
#
# Return an array of right interval indices for each interval i. If no right
# interval exists for interval i, then put -1 at index i.
#
#
# Example 1:
#
#
# Input: intervals = [[1,2]]
# Output: [-1]
# Explanation: There is only one interval in the collection, so it outputs
# -1.
#
#
# Example 2:
#
#
# Input: intervals = [[3,4],[2,3],[1,2]]
# Output: [-1,0,1]
# Explanation: There is no right interval for [3,4].
# The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start
# that is >= end1 = 3.
# The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start
# that is >= end2 = 2.
#
#
# Example 3:
#
#
# Input: intervals = [[1,4],[2,3],[3,4]]
# Output: [-1,2,-1]
# Explanation: There is no right interval for [1,4] and [3,4].
# The right interval for [2,3] is [3,4] since start2 = 3 is the smallest start
# that is >= end1 = 3.
#
#
#
# Constraints:
#
#
# 1 <= intervals.length <= 2 * 10^4
# intervals[i].length == 2
# -10^6 <= starti <= endi <= 10^6
# The start point of each interval is unique.
#
#
#

# @lc tags=binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定间隔，找到每一个间隔右侧的第一个间隔。
# 直接二分搜索。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:

        sl = sorted([(s, i) for i, (s, e) in enumerate(intervals)])
        sl.append((1000000 + 1, -1))
        il = [sl[bisect_left(sl, (e, -1000000))][1] for s, e in intervals]
        return il
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('intervals = [[1,2]]')
    print('Exception :')
    print('[-1]')
    print('Output :')
    print(str(Solution().findRightInterval([[1, 2]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('intervals = [[3,4],[2,3],[1,2]]')
    print('Exception :')
    print('[-1,0,1]')
    print('Output :')
    print(str(Solution().findRightInterval([[3, 4], [2, 3], [1, 2]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('intervals = [[1,4],[2,3],[3,4]]')
    print('Exception :')
    print('[-1,2,-1]')
    print('Output :')
    print(str(Solution().findRightInterval([[1, 4], [2, 3], [3, 4]])))
    print()

    pass
# @lc main=end