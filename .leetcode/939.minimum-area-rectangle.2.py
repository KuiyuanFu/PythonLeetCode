# @lc app=leetcode id=939 lang=python3
#
# [939] Minimum Area Rectangle
#
# https://leetcode.com/problems/minimum-area-rectangle/description/
#
# algorithms
# Medium (53.57%)
# Likes:    1600
# Dislikes: 242
# Total Accepted:    114.6K
# Total Submissions: 214.5K
# Testcase Example:  '[[1,1],[1,3],[3,1],[3,3],[2,2]]'
#
# You are given an array of points in the X-Y plane points where points[i] =
# [xi, yi].
#
# Return the minimum area of a rectangle formed from these points, with sides
# parallel to the X and Y axes. If there is not any such rectangle, return
# 0.
#
#
# Example 1:
#
#
# Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
#
#
# Example 2:
#
#
# Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= points.length <= 500
# points[i].length == 2
# 0 <= xi, yi <= 4 * 10^4
# All the given points are unique.
#
#
#

# @lc tags=divide-and-conquer;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一系列点，求最小矩形面积。
# 排序，遍历。
# 每个矩形由四个点确定，边是平行的。所以就需要先找平行边，以x轴为基准，那么就可以以x值分组，组内的任意两点组成线段都是平行的。由于矩形是沿一三象限平分线对称的，所以xy可以互换，这里选组数叫少的一组作为基准。
# 之后对每两组进行判断，由于这里已经是竖向的平行线的，需要横向的平行线。那么就需要同样高度在两组中都存在，可以使用集合的并集确定所有的平行线，再对每一对进行求面积。
#
# @lc idea=end

# @lc group=set

# @lc rank=10

# @lc code=start


class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:

        res = inf

        cols = defaultdict(set)
        rows = defaultdict(set)
        for x, y in points:
            rows[x].add(y)
            cols[y].add(x)

        base = cols if len(cols) < len(rows) else rows

        keys = sorted(base.keys())

        for keyR in keys:
            setR = base[keyR]

            for keyL in keys:
                if keyR <= keyL:
                    break
                setL = base[keyL]

                s = setL.intersection(setR)

                l = keyR - keyL

                rest = min([l * (u - b) for b, u in pairwise(sorted(s))],
                           default=inf)
                res = min(res, rest)

        if res == inf:
            res = 0
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('points = [[1,1],[1,3],[3,1],[3,3],[2,2]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [2,
                                                                       2]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]')
    print('Exception :')
    print('2')
    print('Output :')
    print(
        str(Solution().minAreaRect([[1, 1], [1, 3], [3, 1], [3, 3], [4, 1],
                                    [4, 3]])))
    print()

    pass
# @lc main=end