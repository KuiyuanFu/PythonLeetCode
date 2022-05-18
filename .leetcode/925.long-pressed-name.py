# @lc app=leetcode id=925 lang=python3
#
# [925] Long Pressed Name
#
# https://leetcode.com/problems/long-pressed-name/description/
#
# algorithms
# Easy (34.73%)
# Likes:    1625
# Dislikes: 241
# Total Accepted:    93.9K
# Total Submissions: 271.7K
# Testcase Example:  '"alex"\n"aaleex"'
#
# Your friend is typing his name into a keyboard. Sometimes, when typing a
# character c, the key might get long pressed, and the character will be typed
# 1 or more times.
#
# You examine the typed characters of the keyboard. Return True if it is
# possible that it was your friends name, with some characters (possibly none)
# being long pressed.
#
#
# Example 1:
#
#
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
#
#
# Example 2:
#
#
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it was not in the typed
# output.
#
#
#
# Constraints:
#
#
# 1 <= name.length, typed.length <= 1000
# name and typed consist of only lowercase English letters.
#
#
#

# @lc tags=tree

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 输入名字，可能卡键，问是否可能为卡键后的结果。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def isLongPressedName(self, name: str, typed: str) -> bool:

        pre = None
        idx = 0
        for c in name:
            if idx >= len(typed):
                return False
            while idx < len(typed) and typed[idx] != c and typed[idx] == pre:
                idx += 1
            if idx == len(typed) or c != typed[idx]:
                return False
            idx += 1
            pre = c
        while idx < len(typed) and typed[idx] == pre:
            idx += 1
        return idx == len(typed)

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().isLongPressedName("alex", "aaleexa")))
    print('Example 1:')
    print('Input : ')
    print('name = "alex", typed = "aaleex"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isLongPressedName("alex", "aaleex")))
    print()

    print('Example 2:')
    print('Input : ')
    print('name = "saeed", typed = "ssaaedd"')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isLongPressedName("saeed", "ssaaedd")))
    print()

    pass
# @lc main=end