# @lc app=leetcode id=885 lang=python3
#
# [885] Spiral Matrix III
#
# https://leetcode.com/problems/spiral-matrix-iii/description/
#
# algorithms
# Medium (72.30%)
# Likes:    499
# Dislikes: 540
# Total Accepted:    33.6K
# Total Submissions: 46.4K
# Testcase Example:  '1\n4\n0\n0'
#
# You start at the cell (rStart, cStart) of an rows x cols grid facing east.
# The northwest corner is at the first row and column in the grid, and the
# southeast corner is at the last row and column.
#
# You will walk in a clockwise spiral shape to visit every position in this
# grid. Whenever you move outside the grid's boundary, we continue our walk
# outside the grid (but may return to the grid boundary later.). Eventually, we
# reach all rows * cols spaces of the grid.
#
# Return an array of coordinates representing the positions of the grid in the
# order you visited them.
#
#
# Example 1:
#
#
# Input: rows = 1, cols = 4, rStart = 0, cStart = 0
# Output: [[0,0],[0,1],[0,2],[0,3]]
#
#
# Example 2:
#
#
# Input: rows = 5, cols = 6, rStart = 1, cStart = 4
# Output:
# [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
#
#
#
# Constraints:
#
#
# 1 <= rows, cols <= 100
# 0 <= rStart < rows
# 0 <= cStart < cols
#
#
#

# @lc tags=ordered-map

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定二维数组，及起点，以顺时针遍历所有元素。
# 判断当前是否可以向右转。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, i: int,
                        j: int) -> List[List[int]]:
        res = []
        totalNumber = rows * cols
        visited = set()
        oi, oj = 0, 1
        while True:
            if 0 <= i < rows and 0 <= j < cols:
                res.append([i, j])
                if len(res) == totalNumber:
                    return res
            visited.add((i, j))
            i, j = i + oi, j + oj
            oni, onj = oj, -oi
            if (i + oni, j + onj) not in visited:
                oi, oj = oni, onj

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('rows = 1, cols = 4, rStart = 0, cStart = 0')
    print('Exception :')
    print('[[0,0],[0,1],[0,2],[0,3]]')
    print('Output :')
    print(str(Solution().spiralMatrixIII(1, 4, 0, 0)))
    print()

    print('Example 2:')
    print('Input : ')
    print('rows = 5, cols = 6, rStart = 1, cStart = 4')
    print('Exception :')
    print(
        '[[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]'
    )
    print('Output :')
    print(str(Solution().spiralMatrixIII(5, 6, 1, 4)))
    print()

    pass
# @lc main=end