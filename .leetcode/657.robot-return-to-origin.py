# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#
# https://leetcode.com/problems/robot-return-to-origin/description/
#
# algorithms
# Easy (74.56%)
# Likes:    1451
# Dislikes: 707
# Total Accepted:    304.9K
# Total Submissions: 408.4K
# Testcase Example:  '"UD"'
#
# There is a robot starting at the position (0, 0), the origin, on a 2D plane.
# Given a sequence of its moves, judge if this robot ends up at (0, 0) after it
# completes its moves.
#
# You are given a string moves that represents the move sequence of the robot
# where moves[i] represents its i^th move. Valid moves are 'R' (right), 'L'
# (left), 'U' (up), and 'D' (down).
#
# Return true if the robot returns to the origin after it finishes all of its
# moves, or false otherwise.
#
# Note: The way that the robot is "facing" is irrelevant. 'R' will always make
# the robot move to the right once, 'L' will always make it move left, etc.
# Also, assume that the magnitude of the robot's movement is the same for each
# move.
#
#
# Example 1:
#
#
# Input: moves = "UD"
# Output: true
# Explanation: The robot moves up once, and then down once. All moves have the
# same magnitude, so it ended up at the origin where it started. Therefore, we
# return true.
#
#
# Example 2:
#
#
# Input: moves = "LL"
# Output: false
# Explanation: The robot moves left twice. It ends up two "moves" to the left
# of the origin. We return false because it is not at the origin at the end of
# its moves.
#
#
# Example 3:
#
#
# Input: moves = "RRDD"
# Output: false
#
#
# Example 4:
#
#
# Input: moves = "LDRRLRUULR"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= moves.length <= 2 * 10^4
# moves only contains the characters 'U', 'D', 'L' and 'R'.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断机器人是否能回到原点。
# 就是左右两个分量及上下两个分量是否相等。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count(
            'R') == moves.count('L')
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('moves = "UD"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().judgeCircle("UD")))
    print()

    print('Example 2:')
    print('Input : ')
    print('moves = "LL"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().judgeCircle("LL")))
    print()

    print('Example 3:')
    print('Input : ')
    print('moves = "RRDD"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().judgeCircle("RRDD")))
    print()

    print('Example 4:')
    print('Input : ')
    print('moves = "LDRRLRUULR"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().judgeCircle("LDRRLRUULR")))
    print()

    pass
# @lc main=end