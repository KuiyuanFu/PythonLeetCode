# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#
# https://leetcode.com/problems/guess-number-higher-or-lower/description/
#
# algorithms
# Easy (45.90%)
# Likes:    711
# Dislikes: 2206
# Total Accepted:    215.1K
# Total Submissions: 467.6K
# Testcase Example:  '10\n6'
#
# We are playing the Guess Game. The game is as follows:
#
# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I will tell you whether the number I picked is
# higher or lower than your guess.
#
# You call a pre-defined API int guess(int num), which returns 3 possible
# results:
#
#
# -1: The number I picked is lower than your guess (i.e. pick < num).
# 1: The number I picked is higher than your guess (i.e. pick > num).
# 0: The number I picked is equal to your guess (i.e. pick == num).
#
#
# Return the number that I picked.
#
#
# Example 1:
# Input: n = 10, pick = 6
# Output: 6
# Example 2:
# Input: n = 1, pick = 1
# Output: 1
# Example 3:
# Input: n = 2, pick = 1
# Output: 1
# Example 4:
# Input: n = 2, pick = 2
# Output: 2
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
# 1 <= pick <= n
#
#
#

# @lc tags=binary-search

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 在1-n中猜数字。
# 二分法。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            f = guess(m)
            if f == 0:
                return m
            elif f < 0:
                r = m - 1
            else:
                l = m + 1
        return -1


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 10, pick = 6')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().guessNumber(10, pick=6)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1, pick = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().guessNumber(1, pick=1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 2, pick = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().guessNumber(2, pick=1)))
    print()

    print('Example 4:')
    print('Input : ')
    print('n = 2, pick = 2')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().guessNumber(2, pick=2)))
    print()

    pass
# @lc main=end