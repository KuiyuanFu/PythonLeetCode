# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#
# https://leetcode.com/problems/water-and-jug-problem/description/
#
# algorithms
# Medium (32.19%)
# Likes:    534
# Dislikes: 950
# Total Accepted:    51.6K
# Total Submissions: 159.7K
# Testcase Example:  '3\n5\n4'
#
# You are given two jugs with capacities jug1Capacity and jug2Capacity liters.
# There is an infinite amount of water supply available. Determine whether it
# is possible to measure exactly targetCapacity liters using these two jugs.
#
# If targetCapacity liters of water are measurable, you must have
# targetCapacity liters of water contained within one or both buckets by the
# end.
#
# Operations allowed:
#
#
# Fill any of the jugs with water.
# Empty any of the jugs.
# Pour water from one jug into another till the other jug is completely full,
# or the first jug itself is empty.
#
#
#
# Example 1:
#
#
# Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
# Output: true
# Explanation: The famous Die Hard example
#
#
# Example 2:
#
#
# Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
# Output: false
#
#
# Example 3:
#
#
# Input: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
# Output: true
#
#
#
# Constraints:
#
#
# 1 <= jug1Capacity, jug2Capacity, targetCapacity <= 10^6
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定两个容器的容量，判断是否能准确得到目标容积的水。
# 充满、清空、移动。
# 当一个容器是不满的时候，另一个容器一定是空的或者满着。所以可以由另外一个容器倒水到这个容器中，或者导入另一个容器中。
# 假设容器1比容器2容积大，之后j1-j2得到j1r即剩余体积，迭代，直到j1r小于j2，得j1r=j1%j2。之后将水移动到j2中，得到j2r=j1r，将j1加满，倒入j2中，得到j1r=j1 - (j2 - j1%j2)，之后继续倒入空的j2中，得到j1r =(j1 - (j2 - j1%j2))%j2.
# 得到得最小值，是一个关于j2的循环群，最小值是j1和j2的最小公倍数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def canMeasureWater(self, j1: int, j2: int, t: int) -> bool:
        if j1 + j2 < t:
            return False
        if t in [0, j1, j2, j1 + j2]:
            return True
        return t % gcd(j1, j2) == 0


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canMeasureWater(3, 5, 4)))
    print()

    print('Example 2:')
    print('Input : ')
    print('jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canMeasureWater(2, 6, 5)))
    print()

    print('Example 3:')
    print('Input : ')
    print('jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canMeasureWater(1, 2, 3)))
    print()

    pass
# @lc main=end