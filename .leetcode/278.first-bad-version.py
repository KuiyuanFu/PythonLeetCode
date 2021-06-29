# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#
# https://leetcode.com/problems/first-bad-version/description/
#
# algorithms
# Easy (38.18%)
# Likes:    2377
# Dislikes: 878
# Total Accepted:    589.8K
# Total Submissions: 1.5M
# Testcase Example:  '5\n4'
#
# You are a product manager and currently leading a team to develop a new
# product. Unfortunately, the latest version of your product fails the quality
# check. Since each version is developed based on the previous version, all the
# versions after a bad version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first
# bad one, which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which returns whether version
# is bad. Implement a function to find the first bad version. You should
# minimize the number of calls to the API.
#
#
# Example 1:
#
#
# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.
#
#
# Example 2:
#
#
# Input: n = 1, bad = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= bad <= n <= 2^31 - 1
#
#
#

# @lc tags=binary-search

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 在给定版本号序列中，找到第一个是坏的版本。
# 直接二分法。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 5, bad = 4')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().firstBadVersion(5, bad=4)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 1, bad = 1')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().firstBadVersion(1, bad=1)))
    print()

    pass
# @lc main=end