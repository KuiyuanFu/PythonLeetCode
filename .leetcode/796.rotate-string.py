# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#
# https://leetcode.com/problems/rotate-string/description/
#
# algorithms
# Easy (49.58%)
# Likes:    1544
# Dislikes: 78
# Total Accepted:    126.1K
# Total Submissions: 249K
# Testcase Example:  '"abcde"\n"cdeab"'
#
# Given two strings s and goal, return true if and only if s can become goal
# after some number of shifts on s.
#
# A shift on s consists of moving the leftmost character of s to the rightmost
# position.
#
#
# For example, if s = "abcde", then it will be "bcdea" after one shift.
#
#
#
# Example 1:
# Input: s = "abcde", goal = "cdeab"
# Output: true
# Example 2:
# Input: s = "abcde", goal = "abced"
# Output: false
#
#
# Constraints:
#
#
# 1 <= s.length, goal.length <= 100
# s and goal consist of lowercase English letters.
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 判断两个字符串是否可以通过旋转来变换。
# 直接循环。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        l = len(goal)
        for i in range(l):
            f = True
            for j in range(l):
                if s[j] != goal[(i + j) % l]:
                    f = False
                    break
            if f:
                return True
        return False
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "abcde", goal = "cdeab"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().rotateString("abcde", "cdeab")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "abcde", goal = "abced"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().rotateString("abcde", "abced")))
    print()

    pass
# @lc main=end