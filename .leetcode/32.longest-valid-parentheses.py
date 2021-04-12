#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (29.87%)
# Likes:    5043
# Dislikes: 182
# Total Accepted:    367.9K
# Total Submissions: 1.2M
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
#
#
# Example 1:
#
#
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
#
#
# Example 2:
#
#
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
#
#
# Example 3:
#
#
# Input: s = ""
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 3 * 10^4
# s[i] is '(', or ')'.
#
#
#
#
#
# @lc idea=start
#
# 求最长有效括号，使用栈和一个临时变量，栈中存储匹配这个左括号，就会多出多少长度。
#
# @lc idea=end

from typing import *
from collections import *


# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        lengthMax = 0
        length = 0

        for c in s:
            if c == '(':
                stack.append(length)
                length = 0
            else:
                if len(stack) != 0:
                    length += 2 + stack.pop()
                    if length > lengthMax:
                        lengthMax = length
                else:
                    length = 0

        return lengthMax
# @lc code=end
