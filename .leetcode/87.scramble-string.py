# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#
# https://leetcode.com/problems/scramble-string/description/
#
# algorithms
# Hard (34.81%)
# Likes:    778
# Dislikes: 811
# Total Accepted:    123.7K
# Total Submissions: 355.2K
# Testcase Example:  '"great"\n"rgeat"'
#
# We can scramble a string s to get a string t using the following
# algorithm:
#
#
# If the length of the string is 1, stop.
# If the length of the string is > 1, do the following:
#
# Split the string into two non-empty substrings at a random index, i.e., if
# the string is s, divide it to x and y where s = x + y.
# Randomly decide to swap the two substrings or to keep them in the same order.
# i.e., after this step, s may become s = x + y or s = y + x.
# Apply step 1 recursively on each of the two substrings x and y.
#
#
#
#
# Given two strings s1 and s2 of the same length, return true if s2 is a
# scrambled string of s1, otherwise, return false.
#
#
# Example 1:
#
#
# Input: s1 = "great", s2 = "rgeat"
# Output: true
# Explanation: One possible scenario applied on s1 is:
# "great" --> "gr/eat" // divide at random index.
# "gr/eat" --> "gr/eat" // random decision is not to swap the two substrings
# and keep them in order.
# "gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both
# substrings. divide at ranom index each of them.
# "g/r / e/at" --> "r/g / e/at" // random decision was to swap the first
# substring and to keep the second substring in the same order.
# "r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively,
# divide "at" to "a/t".
# "r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both
# substrings in the same order.
# The algorithm stops now and the result string is "rgeat" which is s2.
# As there is one possible scenario that led s1 to be scrambled to s2, we
# return true.
#
#
# Example 2:
#
#
# Input: s1 = "abcde", s2 = "caebd"
# Output: false
#
#
# Example 3:
#
#
# Input: s1 = "a", s2 = "a"
# Output: true
#
#
#
# Constraints:
#
#
# s1.length == s2.length
# 1 <= s1.length <= 30
# s1 and s2 consist of lower-case English letters.
#
#
#

# @lc tags=string;dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定两个字符串，判断是否可能是转换得来的。
# 转换的规则是，随机选定一个索引，将字符串分为两个子字符串，之后可以交换位置或不变。再对这两个子字符串递归转换。直到长度为1。
# 朴素的想法是直接按照这个规律转换遍历一遍。
# 首先判断字符是否一样，之后再依次遍历。
# 超时了，加备忘录，变成动态规划。
# 也是很慢。
#
# @lc idea=end

# @lc group=dynamic-programming

# @lc rank=8


# @lc code=start
class Solution:
    mem = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        if (s1, s2) in self.mem:
            return self.mem[(s1, s2)]
        ret = False
        if not self.isSameChar(s1, s2):
            ret = False
        elif s1 == s2:
            ret = True
        else:
            for i in range(1, len(s1)):
                s1L, s1R = s1[:i], s1[i:]
                s2L, s2R = s2[:i], s2[i:]
                if self.isScramble(s1L, s2L) and self.isScramble(s1R, s2R):
                    ret = True
                    break
                s2L, s2R = s2[len(s1) - i:], s2[:len(s1) - i]
                if self.isScramble(s1L, s2L) and self.isScramble(s1R, s2R):
                    ret = True
                    break
        self.mem[(s1, s2)] = ret
        self.mem[(s2, s1)] = ret
        return ret
        pass

    def isSameChar(self, s1, s2):
        buff = [0] * 26
        for c in s1:
            buff[ord(c) - 97] += 1
        for c in s2:
            index = ord(c) - 97
            buff[index] -= 1
            if buff[index] < 0:
                return False
        return True


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(
        str(Solution().isScramble("eebaacbcbcadaaedceaaacadccd",
                                  "eadcaacabaddaceacbceaabeccd")))
    print('Example 1:')
    print('Input : ')
    print('s1 = "great", s2 = "rgeat"')
    print('Output :')
    print(str(Solution().isScramble("great", "rgeat")))
    print('Exception :')
    print('true')
    print()

    print('Example 2:')
    print('Input : ')
    print('s1 = "abcde", s2 = "caebd"')
    print('Output :')
    print(str(Solution().isScramble("abcde", "caebd")))
    print('Exception :')
    print('false')
    print()

    print('Example 3:')
    print('Input : ')
    print('s1 = "a", s2 = "a"')
    print('Output :')
    print(str(Solution().isScramble("a", "a")))
    print('Exception :')
    print('true')
    print()

    pass
# @lc main=end