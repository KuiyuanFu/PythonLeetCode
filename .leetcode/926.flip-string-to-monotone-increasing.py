# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#
# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/
#
# algorithms
# Medium (58.69%)
# Likes:    1973
# Dislikes: 89
# Total Accepted:    92.9K
# Total Submissions: 157.7K
# Testcase Example:  '"00110"'
#
# A binary string is monotone increasing if it consists of some number of 0's
# (possibly none), followed by some number of 1's (also possibly none).
#
# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or
# from 1 to 0.
#
# Return the minimum number of flips to make s monotone increasing.
#
#
# Example 1:
#
#
# Input: s = "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.
#
#
# Example 2:
#
#
# Input: s = "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.
#
#
# Example 3:
#
#
# Input: s = "00011000"
# Output: 2
# Explanation: We flip to get 00000000.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s[i] is either '0' or '1'.
#
#
#

# @lc tags=string

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 整理成单调递增，每次修改一个位置。
# 统计左右01个数。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def minFlipsMonoIncr(self, s: str) -> int:

        length = len(s)
        lefts = [0] * (length + 1)
        for i in range(length):
            lefts[i + 1] = lefts[i] + (1 if s[i] == '1' else 0)
        rights = [0] * (length + 1)
        for i in reversed(range(length)):
            rights[i] = rights[i + 1] + (1 if s[i] == '0' else 0)
        return min((lefts[i] + rights[i]) for i in range(length + 1))

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('s = "00110"')
    print('Exception :')
    print('1')
    print('Output :')
    print(str(Solution().minFlipsMonoIncr("00110")))
    print()

    print('Example 2:')
    print('Input : ')
    print('s = "010110"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().minFlipsMonoIncr("010110")))
    print()

    print('Example 3:')
    print('Input : ')
    print('s = "00011000"')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().minFlipsMonoIncr("00011000")))
    print()

    pass
# @lc main=end