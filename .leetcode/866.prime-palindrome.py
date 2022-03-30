# @lc app=leetcode id=866 lang=python3
#
# [866] Prime Palindrome
#
# https://leetcode.com/problems/prime-palindrome/description/
#
# algorithms
# Medium (25.77%)
# Likes:    312
# Dislikes: 702
# Total Accepted:    25.2K
# Total Submissions: 97.7K
# Testcase Example:  '6'
#
# Given an integer n, return the smallest prime palindrome greater than or
# equal to n.
#
# An integer is prime if it has exactly two divisors: 1 and itself. Note that 1
# is not a prime number.
#
#
# For example, 2, 3, 5, 7, 11, and 13 are all primes.
#
#
# An integer is a palindrome if it reads the same from left to right as it does
# from right to left.
#
#
# For example, 101 and 12321 are palindromes.
#
#
# The test cases are generated so that the answer always exists and is in the
# range [2, 2 * 10^8].
#
#
# Example 1:
# Input: n = 6
# Output: 7
# Example 2:
# Input: n = 8
# Output: 11
# Example 3:
# Input: n = 13
# Output: 101
#
#
# Constraints:
#
#
# 1 <= n <= 10^8
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求大于目标值的最小回文质数。
# 直接暴力迭代
# 其中所有偶数的回文都不是质数，因为会被11整除，当然了，除了11.
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def primePalindrome(self, N: int) -> int:
        def isPrime(x):
            if x < 2 or x % 2 == 0: return x == 2
            for i in range(3, int(x**0.5) + 1, 2):
                if x % i == 0: return False
            return True

        if 8 <= N <= 11: return 11
        for x in range(10**(len(str(N)) // 2), 10**5):
            y = int(str(x) + str(x)[-2::-1])
            if y >= N and isPrime(y): return y
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 6')
    print('Exception :')
    print('7')
    print('Output :')
    print(str(Solution().primePalindrome(6)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 8')
    print('Exception :')
    print('11')
    print('Output :')
    print(str(Solution().primePalindrome(8)))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 13')
    print('Exception :')
    print('101')
    print('Output :')
    print(str(Solution().primePalindrome(13)))
    print()

    pass
# @lc main=end