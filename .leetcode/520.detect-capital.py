# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#
# https://leetcode.com/problems/detect-capital/description/
#
# algorithms
# Easy (54.18%)
# Likes:    917
# Dislikes: 307
# Total Accepted:    203K
# Total Submissions: 374.5K
# Testcase Example:  '"USA"'
#
# We define the usage of capitals in a word to be right when one of the
# following cases holds:
#
#
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
#
#
# Given a string word, return true if the usage of capitals in it is right.
#
#
# Example 1:
# Input: word = "USA"
# Output: true
# Example 2:
# Input: word = "FlaG"
# Output: false
#
#
# Constraints:
#
#
# 1 <= word.length <= 100
# word consists of lowercase and uppercase English letters.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 检测大小写。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        return word == word.upper() or word[1:] == word[1:].lower()


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('word = "USA"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().detectCapitalUse("USA")))
    print()

    print('Example 2:')
    print('Input : ')
    print('word = "FlaG"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().detectCapitalUse("FlaG")))
    print()

    pass
# @lc main=end