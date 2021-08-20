# @lc app=leetcode id=407 lang=python3
#
# [407] Trapping Rain Water II
#
# https://leetcode.com/problems/trapping-rain-water-ii/description/
#
# algorithms
# Hard (45.21%)
# Likes:    2107
# Dislikes: 47
# Total Accepted:    57.2K
# Total Submissions: 126.2K
# Testcase Example:  '[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]'
#
# Given an m x n integer matrix heightMap representing the height of each unit
# cell in a 2D elevation map, return the volume of water it can trap after
# raining.
#
#
# Example 1:
#
#
# Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# Output: 4
# Explanation: After the rain, water is trapped between the blocks.
# We have two small pounds 1 and 3 units trapped.
# The total volume of water trapped is 4.
#
#
# Example 2:
#
#
# Input: heightMap =
# [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# Output: 10
#
#
#
# Constraints:
#
#
# m == heightMap.length
# n == heightMap[i].length
# 1 <= m, n <= 200
# 0 <= heightMap[i][j] <= 2 * 10^4
#
#
#

# @lc tags=heap;breadth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定二维数组，表示高度，看能接多少水。
# 从四周边界向内缩小。从边界最小的位置开始收缩，如果遇到较小的，则可以积水，并继续收缩；否则成为新的边界。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def trapRainWater(self, m: List[List[int]]) -> int:
        rows, cols = len(m), len(m[0])
        if rows < 3 or cols < 3:
            return 0

        border = []
        for i in range(rows):
            border.append((m[i][0], i, 0))
            border.append((m[i][-1], i, cols - 1))
        for j in range(1, cols - 1):
            border.append((m[0][j], 0, j))
            border.append((m[-1][j], rows - 1, j))
        heapify(border)
        visited = set(border)

        waters = 0
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while border:
            stacks = [heappop(border)]
            h = stacks[0][0]
            while stacks:
                nh, ni, nj = stacks.pop()
                for oi, oj in directions:
                    bi, bj = ni + oi, nj + oj
                    if not (0 <= bi < rows and 0 <= bj < cols):
                        continue
                    bh = m[bi][bj]
                    b = (bh, bi, bj)
                    if b in visited:
                        continue
                    visited.add(b)

                    if bh <= h:
                        waters += h - bh
                        stacks.append((bh, bi, bj))
                    else:
                        heappush(border, (bh, bi, bj))
        return waters
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]')
    print('Exception :')
    print('4')
    print('Output :')
    print(
        str(Solution().trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4],
                                      [2, 3, 3, 2, 3, 1]])))
    print()

    print('Example 2:')
    print('Input : ')
    print(
        'heightMap =[[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]'
    )
    print('Exception :')
    print('10')
    print('Output :')
    print(
        str(Solution().trapRainWater([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3],
                                      [3, 2, 1, 2, 3], [3, 2, 2, 2, 3],
                                      [3, 3, 3, 3, 3]])))
    print()

    pass
# @lc main=end