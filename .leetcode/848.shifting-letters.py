# @lc app=leetcode id=848 lang=python3
#
# [848] Shifting Letters
#
# https://leetcode.com/problems/shifting-letters/description/
#
# algorithms
# Medium (45.47%)
# Likes:    833
# Dislikes: 96
# Total Accepted:    70.6K
# Total Submissions: 155.3K
# Testcase Example:  '"abc"\n[3,5,9]'
#
# You are given a string s of lowercase English letters and an integer array
# shifts of the same length.
#
# Call the shift() of a letter, the next letter in the alphabet, (wrapping
# around so that 'z' becomes 'a').
#
#
# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
#
#
# Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x
# times.
#
# Return the final string after all such shifts to s are applied.
#
#
# Example 1:
#
#
# Input: s = "abc", shifts = [3,5,9]
# Output: "rpl"
# Explanation: We start with "abc".
# After shifting the first 1 letters of s by 3, we have "dbc".
# After shifting the first 2 letters of s by 5, we have "igc".
# After shifting the first 3 letters of s by 9, we have "rpl", the answer.
#
#
# Example 2:
#
#
# Input: s = "aaa", shifts = [1,2,3]
# Output: "gfd"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
# shifts.length == s.length
# 0 <= shifts[i] <= 10^9
#
#
#

# @lc tags=Unknown

# @lc imports=start
from operator import length_hint
from imports import *

# @lc imports=end

# @lc idea=start
#
# 转换字符
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = []
        length = len(s)
        n = 0
        orda = ord('a')
        for i in reversed(range(length)):
            c = s[i]
            n += shifts[i]
            res.append(chr((ord(c) - orda + n) % 26 + orda))

        return ''.join(reversed(res))
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "abc", shifts = [3,5,9]')
    print('Exception :')
    print('"rpl"')
    print('Output :')
    print(str(Solution().shiftingLetters("abc", [3, 5, 9])))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "aaa", shifts = [1,2,3]')
    print('Exception :')
    print('"gfd"')
    print('Output :')
    print(str(Solution().shiftingLetters("aaa", [1, 2, 3])))
    print()

    pass
# @lc main=end