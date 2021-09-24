# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#
# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (73.87%)
# Likes:    1787
# Dislikes: 120
# Total Accepted:    297.6K
# Total Submissions: 399.3K
# Testcase Example:  `"Let's take LeetCode contest"`
#
# Given a string s, reverse the order of characters in each word within a
# sentence while still preserving whitespace and initial word order.
#
#
# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:
# Input: s = "God Ding"
# Output: "doG gniD"
#
#
# Constraints:
#
#
# 1 <= s.length <= 5 * 10^4
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 翻转每一个单词。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([w[::-1] for w in s.split()])


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "Let\'s take LeetCode contest"')
    print('Exception :')
    print('"s\'teL ekat edoCteeL tsetnoc"')
    print('Output :')
    print(str(Solution().reverseWords("Let's take LeetCode contest")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "God Ding"')
    print('Exception :')
    print('"doG gniD"')
    print('Output :')
    print(str(Solution().reverseWords("God Ding")))
    print()

    pass
# @lc main=end