# @lc app=leetcode id=818 lang=python3
#
# [818] Race Car
#
# https://leetcode.com/problems/race-car/description/
#
# algorithms
# Hard (41.81%)
# Likes:    823
# Dislikes: 84
# Total Accepted:    31K
# Total Submissions: 74.1K
# Testcase Example:  '3'
#
# Your car starts at position 0 and speed +1 on an infinite number line. Your
# car can go into negative positions. Your car drives automatically according
# to a sequence of instructions 'A' (accelerate) and 'R' (reverse):
#
#
# When you get an instruction 'A', your car does the following:
#
#
# position += speed
# speed *= 2
#
#
# When you get an instruction 'R', your car does the following:
#
# If your speed is positive then speed = -1
# otherwise speed = 1
#
# Your position stays the same.
#
#
# For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3
# --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.
#
# Given a target position target, return the length of the shortest sequence of
# instructions to get there.
#
#
# Example 1:
#
#
# Input: target = 3
# Output: 2
# Explanation:
# The shortest instruction sequence is "AA".
# Your position goes from 0 --> 1 --> 3.
#
#
# Example 2:
#
#
# Input: target = 6
# Output: 5
# Explanation:
# The shortest instruction sequence is "AAARA".
# Your position goes from 0 --> 1 --> 3 --> 7 --> 7 --> 6.
#
#
#
# Constraints:
#
#
# 1 <= target <= 10^4
#
#
#

# @lc tags=math;string

# @lc imports=start

from operator import truediv
from imports import *

# @lc imports=end

# @lc idea=start
#
# 赛车，两种操作。
# - A：前进速度大小，速度翻倍
# - R：位置不变，速度方向相反，置为1
# 求给定目的地的最小步数。
# BFS
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    def racecar(self, target: int) -> int:

        t = 0
        ls = [(0, 1)]
        visited = set(ls)

        while True:
            t += 1
            lsn = []
            while ls:
                p, s = ls.pop()
                pa, sa = p + s, s * 2
                if pa == target:
                    return t
                if (pa, sa) not in visited:
                    lsn.append((pa, sa))
                    visited.add((pa, sa))
                sr = 1 if s < 0 else -1
                if (p, sr) not in visited:
                    lsn.append((p, sr))
                    visited.add((p, sr))
            ls = lsn


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('target = 3')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().racecar(3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('target = 6')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().racecar(6)))
    print()
    print('Input : ')
    print('target = 5')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().racecar(5)))
    print()
    print(str(Solution().racecar(997)))
    print(str(Solution().racecar(998)))
    print(str(Solution().racecar(999)))
    print(str(Solution().racecar(1000)))
    pass
# @lc main=end