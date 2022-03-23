# @lc app=leetcode id=858 lang=python3
#
# [858] Mirror Reflection
#
# https://leetcode.com/problems/mirror-reflection/description/
#
# algorithms
# Medium (59.55%)
# Likes:    362
# Dislikes: 708
# Total Accepted:    26.1K
# Total Submissions: 43.9K
# Testcase Example:  '2\n1'
#
# There is a special square room with mirrors on each of the four walls. Except
# for the southwest corner, there are receptors on each of the remaining
# corners, numbered 0, 1, and 2.
#
# The square room has walls of length p and a laser ray from the southwest
# corner first meets the east wall at a distance q from the 0^th receptor.
#
# Given the two integers p and q, return the number of the receptor that the
# ray meets first.
#
# The test cases are guaranteed so that the ray will meet a receptor
# eventually.
#
#
# Example 1:
#
#
# Input: p = 2, q = 1
# Output: 2
# Explanation: The ray meets receptor 2 the first time it gets reflected back
# to the left wall.
#
#
# Example 2:
#
#
# Input: p = 3, q = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= q <= p <= 1000
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 正方墙壁，一角发射激光，镜面发射，求射到其他角的编号。
# 求最小公倍数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        g = gcd(p, q)
        # times in height
        heightTimes = q // g
        # width in height
        widthTimes = p // g

        if heightTimes % 2 == 0:
            return 0
        elif widthTimes % 2 == 0:
            return 2
        else:
            return 1

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('p = 2, q = 1')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().mirrorReflection(2, 1)))
    print()

    print('Example 2:')
    print('Input : ')
    print('p = 3, q = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().mirrorReflection(3, 1)))
    print()

    pass
# @lc main=end