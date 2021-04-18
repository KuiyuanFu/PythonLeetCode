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

# @lc tags=string

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
#  求最后一个词的长度，直接求解。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(' ')
        if len(s) == 0:
            return 0
        return  len(s.split(' ')[-1])

        pass
# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "Hello World"')
    print('Output :')
    print(str(Solution().lengthOfLastWord("Hello World")))
    print('Exception :')
    print('5')
    print()
    
    print('Example 2:')
    print('Input : ')
    print('s = " "')
    print('Output :')
    print(str(Solution().lengthOfLastWord(" ")))
    print('Exception :')
    print('0')
    print()
    
    pass
# @lc main=end