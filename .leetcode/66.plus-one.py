# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (42.24%)
# Likes:    2276
# Dislikes: 3152
# Total Accepted:    817.1K
# Total Submissions: 1.9M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of decimal digits representing a non-negative
# integer, increment one to the integer.
#
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contains a single digit.
#
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
#
#
# Example 1:
#
#
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#
#
# Example 2:
#
#
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#
#
# Example 3:
#
#
# Input: digits = [0]
# Output: [1]
#
#
#
# Constraints:
#
#
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
#
#
#
#
#

# @lc tags=array

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个数组，每一个元素表示整数中的一位，正序，使其加一。
# 直接迭代即可。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = 1
        for index in range(len(digits) - 1, -1, -1):
            digits[index] += i
            i = digits[index] // 10
            digits[index] = digits[index] % 10
            if i == 0:
                break
        if i == 1:
            digits = [1] + digits
        return digits
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('digits = [1,2,3]')
    print('Output :')
    print(str(Solution().plusOne([1, 2, 3])))
    print('Exception :')
    print('[1,2,4]')
    print()

    print('Example 2:')
    print('Input : ')
    print('digits = [4,3,2,1]')
    print('Output :')
    print(str(Solution().plusOne([4, 3, 2, 1])))
    print('Exception :')
    print('[4,3,2,2]')
    print()

    print('Example 3:')
    print('Input : ')
    print('digits = [0]')
    print('Output :')
    print(str(Solution().plusOne([0])))
    print('Exception :')
    print('[1]')
    print()

    pass
# @lc main=end