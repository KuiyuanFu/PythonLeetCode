# @lc app=leetcode id=1030 lang=python3
#
# [1030] Matrix Cells in Distance Order
#
# https://leetcode.com/problems/matrix-cells-in-distance-order/description/
#
# algorithms
# Easy (69.39%)
# Likes:    587
# Dislikes: 264
# Total Accepted:    47.9K
# Total Submissions: 69K
# Testcase Example:  '1\n2\n0\n0'
#
# You are given four integers row, cols, rCenter, and cCenter. There is a rows
# x cols matrix and you are on the cell with the coordinates (rCenter,
# cCenter).
#
# Return the coordinates of all cells in the matrix, sorted by their distance
# from (rCenter, cCenter) from the smallest distance to the largest distance.
# You may return the answer in any order that satisfies this condition.
#
# The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 -
# c2|.
#
#
# Example 1:
#
#
# Input: rows = 1, cols = 2, rCenter = 0, cCenter = 0
# Output: [[0,0],[0,1]]
# Explanation: The distances from (0, 0) to other cells are: [0,1]
#
#
# Example 2:
#
#
# Input: rows = 2, cols = 2, rCenter = 0, cCenter = 1
# Output: [[0,1],[0,0],[1,1],[1,0]]
# Explanation: The distances from (0, 1) to other cells are: [0,1,1,2]
# The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.
#
#
# Example 3:
#
#
# Input: rows = 2, cols = 3, rCenter = 1, cCenter = 2
# Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
# Explanation: The distances from (1, 2) to other cells are: [0,1,1,2,2,3]
# There are other answers that would also be accepted as correct, such as
# [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].
#
#
#
# Constraints:
#
#
# 1 <= rows, cols <= 100
# 0 <= rCenter < rows
# 0 <= cCenter < cols
#
#
#

# @lc tags=tree;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定二维矩阵，给定一个中心，按照到其的距离排序所有坐标。
# 直接遍历
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int,
                          cCenter: int) -> List[List[int]]:

        q = [(rCenter, cCenter)]
        v = set(q)
        res = []
        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            qn = []
            while q:
                t = q.pop()
                res.append(list(t))
                for oi, oj in offsets:

                    nt = t[0] + oi, t[1] + oj

                    if 0 <= nt[0] < rows and 0 <= nt[1] < cols and nt not in v:
                        v.add(nt)
                        qn.append(nt)

            q = qn
        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('rows = 1, cols = 2, rCenter = 0, cCenter = 0')
    print('Exception :')
    print('[[0,0],[0,1]]')
    print('Output :')
    print(str(Solution().allCellsDistOrder(1, 2, 0, 0)))
    print()

    print('Example 2:')
    print('Input : ')
    print('rows = 2, cols = 2, rCenter = 0, cCenter = 1')
    print('Exception :')
    print('[[0,1],[0,0],[1,1],[1,0]]')
    print('Output :')
    print(str(Solution().allCellsDistOrder(2, 2, 0, 1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('rows = 2, cols = 3, rCenter = 1, cCenter = 2')
    print('Exception :')
    print('[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]')
    print('Output :')
    print(str(Solution().allCellsDistOrder(2, 3, 1, 2)))
    print()

    pass
# @lc main=end