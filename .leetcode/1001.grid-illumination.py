# @lc app=leetcode id=1001 lang=python3
#
# [1001] Grid Illumination
#
# https://leetcode.com/problems/grid-illumination/description/
#
# algorithms
# Hard (36.25%)
# Likes:    489
# Dislikes: 123
# Total Accepted:    16.6K
# Total Submissions: 45.7K
# Testcase Example:  '5\n[[0,0],[4,4]]\n[[1,1],[1,0]]'
#
# There is a 2D grid of size n x n where each cell of this grid has a lamp that
# is initially turned off.
#
# You are given a 2D array of lamp positions lamps, where lamps[i] = [rowi,
# coli] indicates that the lamp at grid[rowi][coli] is turned on. Even if the
# same lamp is listed more than once, it is turned on.
#
# When a lamp is turned on, it illuminates its cell and all other cells in the
# same row, column, or diagonal.
#
# You are also given another 2D array queries, where queries[j] = [rowj, colj].
# For the j^th query, determine whether grid[rowj][colj] is illuminated or not.
# After answering the j^th query, turn off the lamp at grid[rowj][colj] and its
# 8 adjacent lamps if they exist. A lamp is adjacent if its cell shares either
# a side or corner with grid[rowj][colj].
#
# Return an array of integers ans, where ans[j] should be 1 if the cell in the
# j^th query was illuminated, or 0 if the lamp was not.
#
#
# Example 1:
#
#
# Input: n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
# Output: [1,0]
# Explanation: We have the initial grid with all lamps turned off. In the above
# picture we see the grid after turning on the lamp at grid[0][0] then turning
# on the lamp at grid[4][4].
# The 0^th query asks if the lamp at grid[1][1] is illuminated or not (the blue
# square). It is illuminated, so set ans[0] = 1. Then, we turn off all lamps in
# the red square.
#
# The 1^st query asks if the lamp at grid[1][0] is illuminated or not (the blue
# square). It is not illuminated, so set ans[1] = 0. Then, we turn off all
# lamps in the red rectangle.
#
#
#
# Example 2:
#
#
# Input: n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
# Output: [1,1]
#
#
# Example 3:
#
#
# Input: n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
# Output: [1,1,0]
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^9
# 0 <= lamps.length <= 20000
# 0 <= queries.length <= 20000
# lamps[i].length == 2
# 0 <= rowi, coli < n
# queries[j].length == 2
# 0 <= rowj, colj < n
#
#
#

# @lc tags=hash-table

# @lc imports=start
from difflib import restore
from msvcrt import kbhit
from imports import *

# @lc imports=end

# @lc idea=start
#
# 一盏灯可以照明八个方向，每次查询先得到此处是否明亮，再关闭周围共九个位置的灯。
# 用个数组，记录照明位置
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def gridIllumination(self, n: int, lamps: List[List[int]],
                         queries: List[List[int]]) -> List[int]:
        rows = defaultdict(int)
        cols = defaultdict(int)
        rightup = defaultdict(int)
        leftup = defaultdict(int)

        lamps = set(map(tuple, lamps))

        for i, j in lamps:
            rows[i] += 1
            cols[j] += 1
            rightup[i - j] += 1
            leftup[i + j] += 1
        res = []

        ns = [
            [-1, -1],
            [-1, 0],
            [-1, +1],
            [0, -1],
            [0, 0],
            [0, +1],
            [+1, -1],
            [+1, 0],
            [+1, +1],
        ]

        for i, j in queries:
            if rows[i] or cols[j] or rightup[i - j] or leftup[i + j]:
                res.append(1)
            else:
                res.append(0)

            for oi, oj in ns:
                t = i + oi, j + oj
                if t in lamps:
                    lamps.remove(t)
                    i, j = t
                    rows[i] -= 1
                    cols[j] -= 1
                    rightup[i - j] -= 1
                    leftup[i + j] -= 1
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print(
        '6, [[2,5],[4,2],[0,3],[0,5],[1,4],[4,2],[3,3],[1,0]],[[4,3],[3,1],[5,3],[0,5],[4,4],[3,3]]'
    )
    print('Exception :')
    print('[1,0,1,1,0,1]')
    print('Output :')
    print(
        str(Solution().gridIllumination(
            6,
            [[2, 5], [4, 2], [0, 3], [0, 5], [1, 4], [4, 2], [3, 3], [1, 0]],
            [[4, 3], [3, 1], [5, 3], [0, 5], [4, 4], [3, 3]])))
    print()
    print('Example 1:')
    print('Input : ')
    print('n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]')
    print('Exception :')
    print('[1,0]')
    print('Output :')
    print(
        str(Solution().gridIllumination(5, [[0, 0], [4, 4]],
                                        [[1, 1], [1, 0]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]')
    print('Exception :')
    print('[1,1]')
    print('Output :')
    print(
        str(Solution().gridIllumination(5, [[0, 0], [4, 4]],
                                        [[1, 1], [1, 1]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]')
    print('Exception :')
    print('[1,1,0]')
    print('Output :')
    print(
        str(Solution().gridIllumination(5, [[0, 0], [0, 4]],
                                        [[0, 4], [0, 1], [1, 4]])))
    print()

    pass
# @lc main=end