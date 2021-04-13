#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (33.52%)
# Likes:    1051
# Dislikes: 3124
# Total Accepted:    492.7K
# Total Submissions: 1.5M
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of some words separated by spaces, return the
# length of the last word in the string. If the last word does not exist,
# return 0.
#
# A word is a maximal substring consisting of non-space characters only.
#
#
# Example 1:
# Input: s = "Hello World"
# Output: 5
# Example 2:
# Input: s = " "
# Output: 0
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of only English letters and spaces ' '.
#
#
#
#
#
# @lc idea=start
#
#  求最后一个词的长度，直接求解。
#
# @lc idea=end

from typing import *
from collections import *


# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(' ')
        if len(s) == 0:
            return 0
        return  len(s.split(' ')[-1])

# @lc code=end
