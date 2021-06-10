# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#
# https://leetcode.com/problems/dungeon-game/description/
#
# algorithms
# Hard (33.61%)
# Likes:    2439
# Dislikes: 50
# Total Accepted:    128.5K
# Total Submissions: 381.5K
# Testcase Example:  '[[-2,-3,3],[-5,-10,1],[10,30,-5]]'
#
# The demons had captured the princess and imprisoned her in the bottom-right
# corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D
# grid. Our valiant knight was initially positioned in the top-left room and
# must fight his way through dungeon to rescue the princess.
#
# The knight has an initial health point represented by a positive integer. If
# at any point his health point drops to 0 or below, he dies immediately.
#
# Some of the rooms are guarded by demons (represented by negative integers),
# so the knight loses health upon entering these rooms; other rooms are either
# empty (represented as 0) or contain magic orbs that increase the knight's
# health (represented by positive integers).
#
# To reach the princess as quickly as possible, the knight decides to move only
# rightward or downward in each step.
#
# Return the knight's minimum initial health so that he can rescue the
# princess.
#
# Note that any room can contain threats or power-ups, even the first room the
# knight enters and the bottom-right room where the princess is imprisoned.
#
#
# Example 1:
#
#
# Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
# Output: 7
# Explanation: The initial health of the knight must be at least 7 if he
# follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
#
#
# Example 2:
#
#
# Input: dungeon = [[0]]
# Output: 1
#
#
#
# Constraints:
#
#
# m == dungeon.length
# n == dungeon[i].length
# 1 <= m, n <= 200
# -1000 <= dungeon[i][j] <= 1000
#
#
#

# @lc tags=binary-search;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 地牢游戏，二维图，从左上走到右下，每个格子有生命值加减，求至少需要多少初始的生命值。
# 直接动态规划。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        rows = len(dungeon)
        cols = len(dungeon[0])
        for i in reversed(range(rows - 1)):
            j = -1
            dungeon[i][j] += min(dungeon[i + 1][j], 0)
        for j in reversed(range(cols - 1)):
            i = -1
            dungeon[i][j] += min(dungeon[i][j + 1], 0)
        for i in reversed(range(rows - 1)):
            for j in reversed(range(cols - 1)):
                dungeon[i][j] += min(max(dungeon[i + 1][j], dungeon[i][j + 1]),
                                     0)
        return max(0, -dungeon[0][0]) + 1
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]')
    print('Exception :')
    print('7')
    print('Output :')
    print(
        str(Solution().calculateMinimumHP([[-2, -3, 3], [-5, -10, 1],
                                           [10, 30, -5]])))
    print()

    print('Example 2:')
    print('Input : ')
    print('dungeon = [[0]]')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().calculateMinimumHP([[0]])))
    print()

    pass
# @lc main=end