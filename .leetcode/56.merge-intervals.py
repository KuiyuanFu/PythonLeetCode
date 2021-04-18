# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (41.35%)
# Likes:    7006
# Dislikes: 376
# Total Accepted:    862.4K
# Total Submissions: 2.1M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
#
#
# Example 1:
#
#
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
#
#
# Example 2:
#
#
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
#
#
#
# Constraints:
#
#
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
#
#
#
#
#

# @lc tags=array;sort

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 合并时间段。
# 先排序，再合并。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        results = [intervals[0]]
        for i in intervals[1:]:
            if i[0] <= results[-1][1]:
                results[-1][1] = max(i[1], results[-1][1])
            else:
                results.append(i)
        return results


        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('intervals = [[1,3],[2,6],[8,10],[15,18]]')
    print('Output :')
    print(str(Solution().merge([[1,3],[2,6],[8,10],[15,18]])))
    print('Exception :')
    print('[[1,6],[8,10],[15,18]]')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('intervals = [[1,4],[4,5]]')
    print('Output :')
    print(str(Solution().merge([[1,4],[4,5]])))
    print('Exception :')
    print('[[1,5]]')
    print()
    
    pass
# @lc main=end