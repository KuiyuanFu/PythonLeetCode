# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#
# https://leetcode.com/problems/interval-list-intersections/description/
#
# algorithms
# Medium (71.35%)
# Likes:    4675
# Dislikes: 93
# Total Accepted:    327.6K
# Total Submissions: 459.1K
# Testcase Example:  '[[0,2],[5,10],[13,23],[24,25]]\n[[1,5],[8,12],[15,24],[25,26]]'
#
# You are given two lists of closed intervals, firstList and secondList, where
# firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list
# of intervals is pairwise disjoint and in sorted order.
#
# Return the intersection of these two interval lists.
#
# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with
# a <= x <= b.
#
# The intersection of two closed intervals is a set of real numbers that are
# either empty or represented as a closed interval. For example, the
# intersection of [1, 3] and [2, 4] is [2, 3].
#
#
# Example 1:
#
#
# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList =
# [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
#
#
# Example 2:
#
#
# Input: firstList = [[1,3],[5,9]], secondList = []
# Output: []
#
#
#
# Constraints:
#
#
# 0 <= firstList.length, secondList.length <= 1000
# firstList.length + secondList.length >= 1
# 0 <= starti < endi <= 10^9
# endi < starti+1
# 0 <= startj < endj <= 10^9
# endj < startj+1
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求交集。
# 双指针
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def intervalIntersection(self, fls: List[List[int]],
                             sls: List[List[int]]) -> List[List[int]]:
        res = []

        fi, si = 0, 0
        flen, rlen = len(fls), len(sls)
        while fi < flen and si < rlen:
            fl, fr = fls[fi]
            sl, sr = sls[si]
            l, r = max(fl, sl), min(fr, sr)
            if l <= r:
                res.append([l, r])
            if fr < sr:
                fi += 1
            else:
                si += 1
        return res

        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        'firstList = [[0,2],[5,10],[13,23],[24,25]], secondList =[[1,5],[8,12],[15,24],[25,26]]'
    )
    print('Exception :')
    print('[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]')
    print('Output :')
    print(
        str(Solution().intervalIntersection(
            [[0, 2], [5, 10], [13, 23], [24, 25]],
            [[1, 5], [8, 12], [15, 24], [25, 26]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('firstList = [[1,3],[5,9]], secondList = []')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().intervalIntersection([[1, 3], [5, 9]], [])))
    print()

    pass
# @lc main=end