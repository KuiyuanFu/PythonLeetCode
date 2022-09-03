# @lc app=leetcode id=957 lang=python3
#
# [957] Prison Cells After N Days
#
# https://leetcode.com/problems/prison-cells-after-n-days/description/
#
# algorithms
# Medium (39.24%)
# Likes:    1314
# Dislikes: 1596
# Total Accepted:    147K
# Total Submissions: 374.5K
# Testcase Example:  '[0,1,0,1,1,0,0,1]\n7'
#
# There are 8 prison cells in a row and each cell is either occupied or
# vacant.
#
# Each day, whether the cell is occupied or vacant changes according to the
# following rules:
#
#
# If a cell has two adjacent neighbors that are both occupied or both vacant,
# then the cell becomes occupied.
# Otherwise, it becomes vacant.
#
#
# Note that because the prison is a row, the first and the last cells in the
# row can't have two adjacent neighbors.
#
# You are given an integer array cells where cells[i] == 1 if the i^th cell is
# occupied and cells[i] == 0 if the i^th cell is vacant, and you are given an
# integer n.
#
# Return the state of the prison after n days (i.e., n such changes described
# above).
#
#
# Example 1:
#
#
# Input: cells = [0,1,0,1,1,0,0,1], n = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation: The following table summarizes the state of the prison on each
# day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
#
#
# Example 2:
#
#
# Input: cells = [1,0,0,1,0,0,1,0], n = 1000000000
# Output: [0,0,1,1,1,1,1,0]
#
#
#
# Constraints:
#
#
# cells.length == 8
# cells[i] is either 0 or 1.
# 1 <= n <= 10^9
#
#
#

# @lc tags=stack;greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，如果左右两侧都1或0，此位为1，求经过n次迭代。
# 以cells的内容为key，记录每次迭代结果，如果出现循环，就可以计算。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        length = len(cells)

        idices = [(idx - 1, idx, idx + 1) for idx in range(1, length - 1)]

        def getNext(cells):
            k = 0
            cellsNew = [0] * length
            for i1, i2, i3 in idices:
                v = 1 if cells[i1] == cells[i3] else 0
                cellsNew[i2] = v
                k = k * 2 + v

            return k, cellsNew

        targetKey, cells = getNext(cells)
        n -= 1
        cellss = []
        for _ in range(n):
            cellss.append(cells)
            k, cells = getNext(cells)
            if k == targetKey:
                return cellss[n % len(cellss)]

        return list(cells)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('cells = [0,1,0,1,1,0,0,1], n = 7')
    print('Exception :')
    print('[0,0,1,1,0,0,0,0]')
    print('Output :')
    print(str(Solution().prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7)))
    print()

    print('Example 2:')
    print('Input : ')
    print('cells = [1,0,0,1,0,0,1,0], n = 1000000000')
    print('Exception :')
    print('[0,0,1,1,1,1,1,0]')
    print('Output :')
    print(
        str(Solution().prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0], 1000000000)))
    print()

    pass
# @lc main=end