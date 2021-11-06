# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#
# https://leetcode.com/problems/asteroid-collision/description/
#
# algorithms
# Medium (43.83%)
# Likes:    2695
# Dislikes: 204
# Total Accepted:    153.4K
# Total Submissions: 347.6K
# Testcase Example:  '[5,10,-5]'
#
# We are given an array asteroids of integers representing asteroids in a row.
#
# For each asteroid, the absolute value represents its size, and the sign
# represents its direction (positive meaning right, negative meaning left).
# Each asteroid moves at the same speed.
#
# Find out the state of the asteroids after all collisions. If two asteroids
# meet, the smaller one will explode. If both are the same size, both will
# explode. Two asteroids moving in the same direction will never meet.
#
#
# Example 1:
#
#
# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never
# collide.
#
#
# Example 2:
#
#
# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
#
#
# Example 3:
#
#
# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide
# resulting in 10.
#
#
# Example 4:
#
#
# Input: asteroids = [-2,-1,1,2]
# Output: [-2,-1,1,2]
# Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving
# right. Asteroids moving the same direction never meet, so no asteroids will
# meet each other.
#
#
#
# Constraints:
#
#
# 2 <= asteroids.length <= 10^4
# -1000 <= asteroids[i] <= 1000
# asteroids[i] != 0
#
#
#

# @lc tags=stack

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 行星，相遇时小于等于另一个的会炸。求剩余状态。
# 栈。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        dp = [True] * len(asteroids)
        for i, a in enumerate(asteroids):
            if a > 0:
                s.append((a, i))
            else:
                aabs = -a
                while s and aabs > s[-1][0]:
                    dp[s[-1][1]] = False
                    s.pop()
                if s:
                    dp[i] = False
                    if aabs == s[-1][0]:
                        dp[s[-1][1]] = False
                        s.pop()
        res = []
        for i, f in enumerate(dp):
            if f:
                res.append(asteroids[i])
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('asteroids = [5,10,-5]')
    print('Exception :')
    print('[5,10]')
    print('Output :')
    print(str(Solution().asteroidCollision([5, 10, -5])))
    print()

    print('Example 2:')
    print('Input : ')
    print('asteroids = [8,-8]')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().asteroidCollision([8, -8])))
    print()

    print('Example 3:')
    print('Input : ')
    print('asteroids = [10,2,-5]')
    print('Exception :')
    print('[10]')
    print('Output :')
    print(str(Solution().asteroidCollision([10, 2, -5])))
    print()

    print('Example 4:')
    print('Input : ')
    print('asteroids = [-2,-1,1,2]')
    print('Exception :')
    print('[-2,-1,1,2]')
    print('Output :')
    print(str(Solution().asteroidCollision([-2, -1, 1, 2])))
    print()

    pass
# @lc main=end