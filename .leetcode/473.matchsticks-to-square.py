# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#
# https://leetcode.com/problems/matchsticks-to-square/description/
#
# algorithms
# Medium (40.07%)
# Likes:    1315
# Dislikes: 108
# Total Accepted:    67.1K
# Total Submissions: 167.3K
# Testcase Example:  '[1,1,2,2,2]'
#
# You are given an integer array matchsticks where matchsticks[i] is the length
# of the i^th matchstick. You want to use all the matchsticks to make one
# square. You should not break any stick, but you can link them up, and each
# matchstick must be used exactly one time.
#
# Return true if you can make this square and false otherwise.
#
#
# Example 1:
#
#
# Input: matchsticks = [1,1,2,2,2]
# Output: true
# Explanation: You can form a square with length 2, one side of the square came
# two sticks with length 1.
#
#
# Example 2:
#
#
# Input: matchsticks = [3,3,3,3,4]
# Output: false
# Explanation: You cannot find a way to form a square with all the
# matchsticks.
#
#
#
# Constraints:
#
#
# 1 <= matchsticks.length <= 15
# 1 <= matchsticks[i] <= 10^8
#
#
#

# @lc tags=depth-first-search

# @lc imports=start
import math
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断给定的火柴棍集合能否构成正方形。每个必须用一次。
# 递归遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total // 4
        if max(matchsticks) > target:
            return False
        length = len(matchsticks)
        ls = [0] * 4

        def recur(idx):
            if idx == length:
                return True
            tl = matchsticks[idx]
            for i in range(min(idx + 1, 4)):
                l = ls[i]
                if l + tl <= target:
                    ls[i] += tl
                    if recur(idx + 1):
                        return True
                    ls[i] -= tl
            return False

        return recur(0)
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('matchsticks = [1,1,2,2,2]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().makesquare([1, 1, 2, 2, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('matchsticks = [3,3,3,3,4]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().makesquare([3, 3, 3, 3, 4])))
    print()

    pass
# @lc main=end