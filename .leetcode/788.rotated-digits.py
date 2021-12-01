# @lc app=leetcode id=788 lang=python3
#
# [788] Rotated Digits
#
# https://leetcode.com/problems/rotated-digits/description/
#
# algorithms
# Medium (57.32%)
# Likes:    524
# Dislikes: 1651
# Total Accepted:    77.8K
# Total Submissions: 135.7K
# Testcase Example:  '10'
#
# An integer x is a good if after rotating each digit individually by 180
# degrees, we get a valid number that is different from x. Each digit must be
# rotated - we cannot choose to leave it alone.
#
# A number is valid if each digit remains a digit after rotation. For
# example:
#
#
# 0, 1, and 8 rotate to themselves,
# 2 and 5 rotate to each other (in this case they are rotated in a different
# direction, in other words, 2 or 5 gets mirrored),
# 6 and 9 rotate to each other, and
# the rest of the numbers do not rotate to any other number and become
# invalid.
#
#
# Given an integer n, return the number of good integers in the range [1,
# n].
#
#
# Example 1:
#
#
# Input: n = 10
# Output: 4
# Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after
# rotating.
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 0
#
#
# Example 3:
#
#
# Input: n = 2
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^4
#
#
#

# @lc tags=binary-search

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 一个好数是每位旋转后是一个不同的数。给定n，却小于等于n的好数的个数。
# 一个好数，必要包括“2569”中的一个，不包括“347”。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def rotatedDigits(self, n: int) -> int:
        def isGood(i: int):
            s = str(i)

            for c in '347':
                if c in s:
                    return False
            for c in '2569':
                if c in s:
                    return True
            return False

        return [isGood(i) for i in range(1, n + 1)].count(True)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 10')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().rotatedDigits(10)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().rotatedDigits(1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().rotatedDigits(2)))
    print()

    pass
# @lc main=end