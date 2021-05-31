# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (53.34%)
# Likes:    3546
# Dislikes: 115
# Total Accepted:    318.7K
# Total Submissions: 597.5K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome. Return all possible palindrome partitioning of s.
#
# A palindrome string is a string that reads the same backward as forward.
#
#
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
# Input: s = "a"
# Output: [["a"]]
#
#
# Constraints:
#
#
# 1 <= s.length <= 16
# s contains only lowercase English letters.
#
#
#

# @lc tags=backtracking

# @lc imports=start
from urllib3 import Retry
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定字符串s，将s分成每一段都是回文。得到所有分法。
# 直接递归求解。
# 加上备忘录，防止重复计算子问题。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    mem = {}

    def partition(self, s: str) -> List[List[str]]:
        if s in self.mem:
            return self.mem[s]

        results = []

        for length in range(1, (len(s) + 1) // 2 + 1):
            s1 = s[:length]

            s2 = (s[length - 1:2 * length - 1])[::-1]
            if s1 == s2:
                l = s[:2 * length - 1]
                if 2 * length - 1 != len(s):
                    rs = self.partition(s[2 * length - 1:])
                    for r in rs:
                        results.append([l] + r)
                else:
                    results.append([l])

            s3 = (s[length:2 * length])[::-1]
            if s1 == s3:
                l = s[:2 * length]
                if 2 * length != len(s):
                    rs = self.partition(s[2 * length:])
                    for r in rs:
                        results.append([l] + r)
                else:
                    results.append([l])
        self.mem[s] = results
        return results
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().partition("aa")))

    print('Example 1:')
    print('Input : ')
    print('s = "aab"')
    print('Exception :')
    print('[["a","a","b"],["aa","b"]]')
    print('Output :')
    print(str(Solution().partition("aab")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "a"')
    print('Exception :')
    print('[["a"]]')
    print('Output :')
    print(str(Solution().partition("a")))
    print()

    pass
# @lc main=end