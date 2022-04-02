# @lc app=leetcode id=874 lang=python3
#
# [874] Walking Robot Simulation
#
# https://leetcode.com/problems/walking-robot-simulation/description/
#
# algorithms
# Medium (37.69%)
# Likes:    63
# Dislikes: 12
# Total Accepted:    31.3K
# Total Submissions: 83K
# Testcase Example:  '[4,-1,3]\n[]'
#
# A robot on an infinite XY-plane starts at point (0, 0) facing north. The
# robot can receive a sequence of these three possible types of commands:
#
#
# -2: Turn left 90 degrees.
# -1: Turn right 90 degrees.
# 1 <= k <= 9: Move forward k units, one unit at a time.
#
#
# Some of the grid squares are obstacles. The i^th obstacle is at grid point
# obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will
# instead stay in its current location and move on to the next command.
#
# Return the maximum Euclidean distance that the robot ever gets from the
# origin squared (i.e. if the distance is 5, return 25).
#
# Note:
#
#
# North means +Y direction.
# East means +X direction.
# South means -Y direction.
# West means -X direction.
#
#
#
# Example 1:
#
#
# Input: commands = [4,-1,3], obstacles = []
# Output: 25
# Explanation: The robot starts at (0, 0):
# 1. Move north 4 units to (0, 4).
# 2. Turn right.
# 3. Move east 3 units to (3, 4).
# The furthest point the robot ever gets from the origin is (3, 4), which
# squared is 3^2 + 4^2 = 25 units away.
#
#
# Example 2:
#
#
# Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# Output: 65
# Explanation: The robot starts at (0, 0):
# 1. Move north 4 units to (0, 4).
# 2. Turn right.
# 3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at
# (1, 4).
# 4. Turn left.
# 5. Move north 4 units to (1, 8).
# The furthest point the robot ever gets from the origin is (1, 8), which
# squared is 1^2 + 8^2 = 65 units away.
#
#
# Example 3:
#
#
# Input: commands = [6,-1,-1,6], obstacles = []
# Output: 36
# Explanation: The robot starts at (0, 0):
# 1. Move north 6 units to (0, 6).
# 2. Turn right.
# 3. Turn right.
# 4. Move south 6 units to (0, 0).
# The furthest point the robot ever gets from the origin is (0, 6), which
# squared is 6^2 = 36 units away.
#
#
#
# Constraints:
#
#
# 1 <= commands.length <= 10^4
# commands[i] is either -2, -1, or an integer in the range [1, 9].
# 0 <= obstacles.length <= 10^4
# -3 * 10^4 <= xi, yi <= 3 * 10^4
# The answer is guaranteed to be less than 2^31.
#
#
#

# @lc tags=two-pointers;stack

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 机器人，走路，遇到障碍停止。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:

        i, j = 0, 0
        oi, oj = 0, 1

        obstacles = set(map(tuple, obstacles))

        res = 0
        for c in commands:
            if c == -2:
                oi, oj = -oj, oi
            elif c == -1:
                oi, oj = oj, -oi
            else:
                for _ in range(c):
                    if (i + oi, j + oj) not in obstacles:
                        i, j = (i + oi, j + oj)
                        res = max(res, i * i + j * j)
                    else:
                        break

        return res

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    # print('Example 1:')
    # print('Input : ')
    # print('commands = [4,-1,3], obstacles = []')
    # print('Exception :')
    # print('25')
    # print('Output :')
    # print(str(Solution().robotSim([4, -1, 3], [])))
    # print()

    print('Example 2:')
    print('Input : ')
    print('commands = [4,-1,4,-2,4], obstacles = [[2,4]]')
    print('Exception :')
    print('65')
    print('Output :')
    print(str(Solution().robotSim([4, -1, 4, -2, 4], [[2, 4]])))
    print()

    print('Example 3:')
    print('Input : ')
    print('commands = [6,-1,-1,6], obstacles = []')
    print('Exception :')
    print('36')
    print('Output :')
    print(str(Solution().robotSim([6, -1, -1, 6], [])))
    print()

    pass
# @lc main=end