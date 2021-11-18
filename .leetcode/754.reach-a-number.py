# @lc app=leetcode id=754 lang=python3
#
# [754] Reach a Number
#
# https://leetcode.com/problems/reach-a-number/description/
#
# algorithms
# Medium (40.96%)
# Likes:    924
# Dislikes: 615
# Total Accepted:    35.5K
# Total Submissions: 85.7K
# Testcase Example:  '2'
#
# You are standing at position 0 on an infinite number line. There is a
# destination at position target.
#
# You can make some number of moves numMoves so that:
#
#
# On each move, you can either go left or right.
# During the i^th move (starting from i == 1 to i == numMoves), you take i
# steps in the chosen direction.
#
#
# Given the integer target, return the minimum number of moves required (i.e.,
# the minimum numMoves) to reach the destination.
#
#
# Example 1:
#
#
# Input: target = 2
# Output: 3
# Explanation:
# On the 1^st move, we step from 0 to 1 (1 step).
# On the 2^nd move, we step from 1 to -1 (2 steps).
# On the 3^rd move, we step from -1 to 2 (3 steps).
#
#
# Example 2:
#
#
# Input: target = 3
# Output: 2
# Explanation:
# On the 1^st move, we step from 0 to 1 (1 step).
# On the 2^nd move, we step from 1 to 3 (2 steps).
#
#
#
# Constraints:
#
#
# -10^9 <= target <= 10^9
# target != 0
#
#
#

# @lc tags=math;depth-first-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 移动到目标值，第i次移动i格。
# 深度优先遍历。不行太慢，要数学方法。
# 首先目标值大于零与小于零是等价的。
# 都向正方向，将特定的反方向。
# 如果正向的超过，目标值是偶数倍，就可以了。
#
# @lc idea=end

# @lc group=math;depth-first-search

# @lc rank=10


# @lc code=start
class Solution:
    def reachNumber(self, target: int) -> int:

        target = abs(target)
        baseCount = int(sqrt(1 + target * 8) - 1) // 2
        position = (1 + baseCount) * baseCount // 2
        while position < target or (position - target) % 2 == 1:
            baseCount += 1
            position += baseCount
        return baseCount


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('target = 2')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().reachNumber(2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('target = 3')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().reachNumber(3)))
    print()
    print('Example 2:')
    print('Input : ')
    print('target = 5')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().reachNumber(5)))
    print()
    print(str(Solution().reachNumber(1000000000)))
    pass
# @lc main=end