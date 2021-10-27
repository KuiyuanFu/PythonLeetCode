# @lc app=leetcode id=717 lang=python3
#
# [717] 1-bit and 2-bit Characters
#
# https://leetcode.com/problems/1-bit-and-2-bit-characters/description/
#
# algorithms
# Easy (46.28%)
# Likes:    626
# Dislikes: 1604
# Total Accepted:    96.5K
# Total Submissions: 208.2K
# Testcase Example:  '[1,0,0]'
#
# We have two special characters:
#
#
# The first character can be represented by one bit 0.
# The second character can be represented by two bits (10 or 11).
#
#
# Given a binary array bits that ends with 0, return true if the last character
# must be a one-bit character.
#
#
# Example 1:
#
#
# Input: bits = [1,0,0]
# Output: true
# Explanation: The only way to decode it is two-bit character and one-bit
# character.
# So the last character is one-bit character.
#
#
# Example 2:
#
#
# Input: bits = [1,1,1,0]
# Output: false
# Explanation: The only way to decode it is two-bit character and two-bit
# character.
# So the last character is not one-bit character.
#
#
#
# Constraints:
#
#
# 1 <= bits.length <= 1000
# bits[i] is either 0 or 1.
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 0为单位字符，10、11位双位字符。判断是否以单位字符结束。
# dfa。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        dfa = [
            # 0 1
            # 2end
            [2, 1],
            # 2start
            [0, 0],
            # 1end
            [2, 1]
        ]
        s = 0
        for c in bits:
            s = dfa[s][c]
        return s == 2


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('bits = [1,0,0]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isOneBitCharacter([1, 0, 0])))
    print()

    print('Example 2:')
    print('Input : ')
    print('bits = [1,1,1,0]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().isOneBitCharacter([1, 1, 1, 0])))
    print()

    pass
# @lc main=end