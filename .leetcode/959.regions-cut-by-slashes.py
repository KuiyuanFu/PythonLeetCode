# @lc app=leetcode id=959 lang=python3
#
# [959] Regions Cut By Slashes
#
# https://leetcode.com/problems/regions-cut-by-slashes/description/
#
# algorithms
# Medium (68.96%)
# Likes:    2402
# Dislikes: 456
# Total Accepted:    40.8K
# Total Submissions: 59.2K
# Testcase Example:  '[" /","/ "]'
#
# An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists
# of a '/', '\', or blank space ' '. These characters divide the square into
# contiguous regions.
#
# Given the grid grid represented as a string array, return the number of
# regions.
#
# Note that backslash characters are escaped, so a '\' is represented as
# '\\'.
#
#
# Example 1:
#
#
# Input: grid = [" /","/ "]
# Output: 2
#
#
# Example 2:
#
#
# Input: grid = [" /","  "]
# Output: 1
#
#
# Example 3:
#
#
# Input: grid = ["/\\","\\/"]
# Output: 5
# Explanation: Recall that because \ characters are escaped, "\\/" refers to
# \/, and "/\\" refers to /\.
#
#
#
# Constraints:
#
#
# n == grid.length == grid[i].length
# 1 <= n <= 30
# grid[i][j] is either '/', '\', or ' '.
#
#
#

# @lc tags=two-pointers

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定二维棋盘，'/'把一个格子分成左上和右下两部分。'\'左下，右上两部分。求一共几部分。
# 将每个格子分成上下左右四分。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def regionsBySlashes(self, grid: List[str]) -> int:

        length = len(grid)
        res = 0
        unvisited = set()
        for i, j in product(range(length), range(length)):
            # up,right,bottom,left
            unvisited.add((i, j, 0))
            unvisited.add((i, j, 1))
            unvisited.add((i, j, 2))
            unvisited.add((i, j, 3))
        while unvisited:
            res += 1
            q = [unvisited.pop()]
            while q:
                i, j, order = q.pop()
                c = grid[i][j]
                ts = []
                if c == ' ':
                    ts.append((i, j, 0))
                    ts.append((i, j, 1))
                    ts.append((i, j, 2))
                    ts.append((i, j, 3))
                    ts.append((i + 1, j, 0))
                    ts.append((i, j - 1, 1))
                    ts.append((i - 1, j, 2))
                    ts.append((i, j + 1, 3))
                elif c == '/':
                    if order == 0 or order == 3:
                        ts.append((i, j, 0))
                        ts.append((i, j, 3))
                        ts.append((i, j - 1, 1))
                        ts.append((i - 1, j, 2))
                    else:
                        ts.append((i, j, 1))
                        ts.append((i, j, 2))
                        ts.append((i + 1, j, 0))
                        ts.append((i, j + 1, 3))
                else:
                    if order == 0 or order == 1:
                        ts.append((i, j, 0))
                        ts.append((i, j, 1))
                        ts.append((i - 1, j, 2))
                        ts.append((i, j + 1, 3))
                    else:
                        ts.append((i, j, 2))
                        ts.append((i, j, 3))
                        ts.append((i + 1, j, 0))
                        ts.append((i, j - 1, 1))
                for t in ts:
                    if t in unvisited:
                        unvisited.remove(t)
                        q.append(t)

        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('grid = [" /","/ "]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().regionsBySlashes([" /", "/ "])))
    print()

    print('Example 2:')
    print('Input : ')
    print('grid = [" /","  "]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().regionsBySlashes([" /", "  "])))
    print()

    print('Example 3:')
    print('Input : ')
    print('grid = ["/\\","\\/"]')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().regionsBySlashes(["/\\", "\\/"])))
    print()

    pass
# @lc main=end