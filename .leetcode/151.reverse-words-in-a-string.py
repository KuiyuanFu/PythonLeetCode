# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#
# https://leetcode.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (24.62%)
# Likes:    1694
# Dislikes: 3284
# Total Accepted:    538K
# Total Submissions: 2.2M
# Testcase Example:  '"the sky is blue"'
#
# Given an input string s, reverse the order of the words.
#
# A word is defined as a sequence of non-space characters. The words in s will
# be separated by at least one space.
#
# Return a string of the words in reverse order concatenated by a single
# space.
#
# Note that s may contain leading or trailing spaces or multiple spaces between
# two words. The returned string should only have a single space separating the
# words. Do not include any extra spaces.
#
#
# Example 1:
#
#
# Input: s = "the sky is blue"
# Output: "blue is sky the"
#
#
# Example 2:
#
#
# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing
# spaces.
#
#
# Example 3:
#
#
# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single
# space in the reversed string.
#
#
# Example 4:
#
#
# Input: s = "  Bob    Loves  Alice   "
# Output: "Alice Loves Bob"
#
#
# Example 5:
#
#
# Input: s = "Alice does not even like bob"
# Output: "bob like even not does Alice"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s contains English letters (upper-case and lower-case), digits, and spaces '
# '.
# There is at least one word in s.
#
#
#
# Follow up: Could you solve it in-place with O(1) extra space?
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将给定的字符串中的每个单词，反序合成新字符串。
# 直接反序合并就可以了。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.strip().split()))


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "the sky is blue"')
    print('Exception :')
    print('"blue is sky the"')
    print('Output :')
    print(str(Solution().reverseWords("the sky is blue")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "  hello world  "')
    print('Exception :')
    print('"world hello"')
    print('Output :')
    print(str(Solution().reverseWords("  hello world  ")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "a good   example"')
    print('Exception :')
    print('"example good a"')
    print('Output :')
    print(str(Solution().reverseWords("a good   example")))
    print()

    print('Example 4:')
    print('Input : ')
    print('s = "  Bob    Loves  Alice   "')
    print('Exception :')
    print('"Alice Loves Bob"')
    print('Output :')
    print(str(Solution().reverseWords("  Bob    Loves  Alice   ")))
    print()

    print('Example 5:')
    print('Input : ')
    print('s = "Alice does not even like bob"')
    print('Exception :')
    print('"bob like even not does Alice"')
    print('Output :')
    print(str(Solution().reverseWords("Alice does not even like bob")))
    print()

    pass
# @lc main=end