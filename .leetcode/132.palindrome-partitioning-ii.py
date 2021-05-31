# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#
# https://leetcode.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (31.50%)
# Likes:    1878
# Dislikes: 54
# Total Accepted:    157K
# Total Submissions: 498.3K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
#
# Example 1:
#
#
# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1
# cut.
#
#
# Example 2:
#
#
# Input: s = "a"
# Output: 0
#
#
# Example 3:
#
#
# Input: s = "ab"
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2000
# s consists of lower-case English letters only.
#
#
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 求将一个字符串，分割成全是回文的部分，的最少分割次数。
# 直接递归。加上一点点贪心。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    mem = {}

    def minCut(self, s: str) -> int:
        if s in self.mem:
            return self.mem[s]

        minTimes = len(s)

        for length in range((len(s) + 1) // 2, 0, -1):
            s1 = s[:length]

            s3 = (s[length:2 * length])[::-1]
            if s1 == s3:
                if 2 * length != len(s):
                    minTimes = min(minTimes, self.minCut(s[2 * length:]) + 1)
                    if minTimes == 1:
                        break
                else:
                    minTimes = 0
                    break

            s2 = (s[length - 1:2 * length - 1])[::-1]
            if s1 == s2:
                if 2 * length - 1 != len(s):
                    minTimes = min(minTimes,
                                   self.minCut(s[2 * length - 1:]) + 1)
                    if minTimes == 1:
                        break
                else:
                    minTimes = 0
                    break

        self.mem[s] = minTimes
        return minTimes

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "aab"')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minCut("aab")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "a"')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().minCut("a")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "ab"')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minCut("ab")))
    print()

    pass
# @lc main=end