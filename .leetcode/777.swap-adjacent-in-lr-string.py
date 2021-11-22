# @lc app=leetcode id=777 lang=python3
#
# [777] Swap Adjacent in LR String
#
# https://leetcode.com/problems/swap-adjacent-in-lr-string/description/
#
# algorithms
# Medium (35.79%)
# Likes:    647
# Dislikes: 573
# Total Accepted:    43.3K
# Total Submissions: 120.9K
# Testcase Example:  '"RXXLRXRXL"\n"XRLXXRRLX"'
#
# In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a
# move consists of either replacing one occurrence of "XL" with "LX", or
# replacing one occurrence of "RX" with "XR". Given the starting string start
# and the ending string end, return True if and only if there exists a sequence
# of moves to transform one string to the other.
#
#
# Example 1:
#
#
# Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
# Output: true
# Explanation: We can transform start to end following these steps:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX
#
#
# Example 2:
#
#
# Input: start = "X", end = "L"
# Output: false
#
#
# Example 3:
#
#
# Input: start = "LLR", end = "RRL"
# Output: false
#
#
# Example 4:
#
#
# Input: start = "XL", end = "LX"
# Output: true
#
#
# Example 5:
#
#
# Input: start = "XLLR", end = "LXLX"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= start.length <= 10^4
# start.length == end.length
# Both start and end will only consist of characters in 'L', 'R', and 'X'.
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 交换相邻的字符，是否，可以达到目标。
# 可以交换XL 到 LX，RX 到 XR。L只能左移，R只能右移。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def canTransform(self, start: str, end: str) -> bool:

        start, end = list(start), list(end)
        length = len(start)

        for i in range(length):
            if start[i] == end[i]:
                continue
            # RX to XR
            if end[i] == 'X':
                r = i
                while r < length and start[r] == 'R':
                    r += 1
                if r == length or start[r] != 'X':
                    return False
                start[r] = 'R'
            # XL to LX
            elif end[i] == 'L':
                r = i
                while r < length and start[r] == 'X':
                    r += 1
                if r == length or start[r] != 'L':
                    return False
                start[r] = 'X'
            else:
                return False
        return True


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('start = "RXXLRXRXL", end = "XRLXXRRLX"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canTransform("RXXLRXRXL", "XRLXXRRLX")))
    print()

    print('Example 2:')
    print('Input : ')
    print('start = "X", end = "L"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canTransform("X", "L")))
    print()

    print('Example 3:')
    print('Input : ')
    print('start = "LLR", end = "RRL"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canTransform("LLR", "RRL")))
    print()

    print('Example 4:')
    print('Input : ')
    print('start = "XL", end = "LX"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().canTransform("XL", "LX")))
    print()

    print('Example 5:')
    print('Input : ')
    print('start = "XLLR", end = "LXLX"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().canTransform("XLLR", "LXLX")))
    print()

    pass
# @lc main=end