# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#
# https://leetcode.com/problems/backspace-string-compare/description/
#
# algorithms
# Easy (47.35%)
# Likes:    3679
# Dislikes: 172
# Total Accepted:    393.8K
# Total Submissions: 832.1K
# Testcase Example:  '"ab#c"\n"ad#c"'
#
# Given two strings s and t, return true if they are equal when both are typed
# into empty text editors. '#' means a backspace character.
#
# Note that after backspacing an empty text, the text will continue empty.
#
#
# Example 1:
#
#
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
#
#
# Example 2:
#
#
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
#
#
# Example 3:
#
#
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
#
#
#
# Constraints:
#
#
# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.
#
#
#
# Follow up: Can you solve it in O(n) time and O(1) space?
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 退格
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def bs(s):
            res = []

            for c in s:
                if c == '#':
                    if len(res) > 0:
                        res.pop()
                else:
                    res.append(c)
            return ''.join(res)

        return bs(s) == bs(t)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "ab#c", t = "ad#c"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().backspaceCompare("ab#c", "ad#c")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "ab##", t = "c#d#"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().backspaceCompare("ab##", "c#d#")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "a#c", t = "b"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().backspaceCompare("a#c", "b")))
    print()

    pass
# @lc main=end