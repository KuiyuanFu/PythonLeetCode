#
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
# @lc idea=start
#
# 找字符串中找到指定字符串的索引值，没有则-1。
# (40 ms) 26.26 % 
# 这就是python 太慢了，否则会比直接提取字符串要快。
#
# @lc idea=end

from typing import *
from collections import *

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
        for n in haystack[:length-1]:
            now = (now + ord(n) - assciA) * 26 % mod

        for i in range(len(haystack) - length+1):
            now = (now + ord(haystack[i+length-1]) - assciA) * 26 % mod
            if now == target:
                return i
            now = (now+mod26 - (ord(haystack[i]) - assciA)*num) % mod
        return -1


# @lc code=end

if __name__ == '__main__':
    print(Solution().strStr("hello", "ll"))
