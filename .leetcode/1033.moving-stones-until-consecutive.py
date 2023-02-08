# @lc app=leetcode id=1033 lang=python3
#
# [1033] Moving Stones Until Consecutive
#
# https://leetcode.com/problems/moving-stones-until-consecutive/description/
#
# algorithms
# Medium (46.08%)
# Likes:    182
# Dislikes: 621
# Total Accepted:    21.6K
# Total Submissions: 46.8K
# Testcase Example:  '1\n2\n5'
#
# There are three stones in different positions on the X-axis. You are given
# three integers a, b, and c, the positions of the stones.
#
# In one move, you pick up a stone at an endpoint (i.e., either the lowest or
# highest position stone), and move it to an unoccupied position between those
# endpoints. Formally, let's say the stones are currently at positions x, y,
# and z with x < y < z. You pick up the stone at either position x or position
# z, and move that stone to an integer position k, with x < k < z and k != y.
#
# The game ends when you cannot make any more moves (i.e., the stones are in
# three consecutive positions).
#
# Return an integer array answer of length 2 where:
#
#
# answer[0] is the minimum number of moves you can play, and
# answer[1] is the maximum number of moves you can play.
#
#
#
# Example 1:
#
#
# Input: a = 1, b = 2, c = 5
# Output: [1,2]
# Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to
# 3.
#
#
# Example 2:
#
#
# Input: a = 4, b = 3, c = 2
# Output: [0,0]
# Explanation: We cannot make any moves.
#
#
# Example 3:
#
#
# Input: a = 3, b = 5, c = 1
# Output: [1,2]
# Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to
# 4.
#
#
#
# Constraints:
#
#
# 1 <= a, b, c <= 100
# a, b, and c have different values.
#
#
#

# @lc tags=math;greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定三个位置，每个位置上一个石头，每次可以移动最外侧两个中的一个，将其移动到范围内一个空的位置上，直到三个石头相邻。求移动的最小值和最大值。
#
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:

        a, b, c = sorted([a, b, c])
        res = [0, 0]
        if b - a == c - b == 1:
            res[0] = 0
        elif b - a <= 2 or c - b <= 2:
            res[0] = 1
        else:
            res[0] = 2

        res[1] = b - a - 1 + c - b - 1
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('a = 1, b = 2, c = 5')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().numMovesStones(1, 2, 5)))
    print()

    print('Example 2:')
    print('Input : ')
    print('a = 4, b = 3, c = 2')
    print('Exception :')
    print('[0,0]')
    print('Output :')
    print(str(Solution().numMovesStones(4, 3, 2)))
    print()

    print('Example 3:')
    print('Input : ')
    print('a = 3, b = 5, c = 1')
    print('Exception :')
    print('[1,2]')
    print('Output :')
    print(str(Solution().numMovesStones(3, 5, 1)))
    print()

    pass
# @lc main=end