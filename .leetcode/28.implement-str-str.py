# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (35.34%)
# Likes:    2270
# Dislikes: 2326
# Total Accepted:    857.2K
# Total Submissions: 2.4M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
#
# Clarification:
#
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
#
#
# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Example 3:
# Input: haystack = "", needle = ""
# Output: 0
#
#
# Constraints:
#
#
# 0 <= haystack.length, needle.length <= 5 * 10^4
# haystack and needle consist of only lower-case English characters.
#
#
#

# @lc tags=two-pointers;string

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 在字符串中找到指定字符串的索引值，没有则返回 -1。
# 使用转化为数字取模来生成字符串的一个特征码。再进行比较，只需要遍历一次。
# (40 ms) 26.26 %
# 这就是python 太慢了，否则会比直接提取字符串要快。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        if len(needle) == 0:
            return 0

        mod = 67108863
        mod26 = mod * 26
        assciA = 97
        target = 0
        num = 1
        length = len(needle)
        for n in needle:
            target = (target + ord(n) - assciA) * 26 % mod
            num = (num * 26) % mod
        now = 0
        for n in haystack[:length - 1]:
            now = (now + ord(n) - assciA) * 26 % mod

        for i in range(len(haystack) - length + 1):
            now = (now + ord(haystack[i + length - 1]) - assciA) * 26 % mod
            if now == target:
                return i
            now = (now + mod26 - (ord(haystack[i]) - assciA) * num) % mod
        return -1

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('haystack = "hello", needle = "ll"')
    print('Output :')
    print(str(Solution().strStr("hello", "ll")))
    print('Exception :')
    print('2')
    print()

    print('Example 2:')
    print('Input : ')
    print('haystack = "aaaaa", needle = "bba"')
    print('Output :')
    print(str(Solution().strStr("aaaaa", "bba")))
    print('Exception :')
    print('-1')
    print()

    print('Example 3:')
    print('Input : ')
    print('haystack = "", needle = ""')
    print('Output :')
    print(str(Solution().strStr("", "")))
    print('Exception :')
    print('0')
    print()

    pass
# @lc main=end