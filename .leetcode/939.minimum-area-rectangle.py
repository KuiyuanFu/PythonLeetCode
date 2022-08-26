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
# 每个矩形由四个点确定，边是平行的。所以就需要先找平行边，这里以x轴为基准，那么就可以以x值分组，组内的任意两点组成线段都是平行的。
# 之后需要保证y轴平行，就以y轴两点作为key，找所有已经出现过的相同key的线段，由于是找最小的矩形，那么只需要保存key相同的线段中，最近出现的一条线段。保存的值为x值，那么就可以计算矩形大小。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def minAreaRect(self, points: List[List[int]]) -> int:

        res = (4 * 10**4) * (4 * 10**4)
        points.sort()

        lines = {}

        preX = points[0][0] - 1
        preYIdx = -1
        for idx in range(len(points)):
            x, y = points[idx]
            r, u = x, y
            if x != preX:
                preX = x
                preYIdx = idx
            else:
                for idxB in range(preYIdx, idx):
                    b = points[idxB][1]
                    k = str(u) + '.' + str(b)
                    if k in lines:
                        l = lines[k]
                        res = min(res, (u - b) * (r - l))
                    lines[k] = r

        if res == (4 * 10**4) * (4 * 10**4):
            res = 0
        return res


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