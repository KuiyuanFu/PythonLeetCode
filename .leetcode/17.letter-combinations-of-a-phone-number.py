#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (49.52%)
# Likes:    5831
# Dislikes: 515
# Total Accepted:    815.5K
# Total Submissions: 1.6M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.
#
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
#
#
#
#
# Example 1:
#
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
# Example 2:
#
#
# Input: digits = ""
# Output: []
#
#
# Example 3:
#
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
#
# Constraints:
#
#
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
#
#
#
# @lc idea=start
#
# 递归，很简单的思想
#
# @lc idea=end

from typing import *


# @lc code=start
class Solution:
    pads = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        ls = self.pads[int(digits[0])]
        rs = self.letterCombinations(digits[1:])
        result = []
        for l in ls:
            for r in rs:
                result.append(l+r)
        return result if len(result) != 0 else ls


# @lc code=end
