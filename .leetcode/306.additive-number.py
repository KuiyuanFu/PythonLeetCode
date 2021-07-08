# @lc app=leetcode id=306 lang=python3
#
# [306] Additive Number
#
# https://leetcode.com/problems/additive-number/description/
#
# algorithms
# Medium (29.84%)
# Likes:    577
# Dislikes: 551
# Total Accepted:    61.8K
# Total Submissions: 206.8K
# Testcase Example:  '"112358"'
#
# Additive number is a string whose digits can form additive sequence.
#
# A valid additive sequence should contain at least three numbers. Except for
# the first two numbers, each subsequent number in the sequence must be the sum
# of the preceding two.
#
# Given a string containing only digits '0'-'9', write a function to determine
# if it's an additive number.
#
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence
# 1, 2, 03 or 1, 02, 3 is invalid.
#
#
# Example 1:
#
#
# Input: "112358"
# Output: true
# Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5,
# 8.
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
#
#
# Example 2:
#
#
# Input: "199100199"
# Output: true
# Explanation: The additive sequence is: 1, 99, 100, 199.
# 1 + 99 = 100, 99 + 100 = 199
#
#
#
# Constraints:
#
#
# num consists only of digits '0'-'9'.
# 1 <= num.length <= 35
#
#
# Follow up:
# How would you handle overflow for very large input integers?
#
#

# @lc tags=backtracking

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个数字系列，判断其是否可以形成一个加法序列，即相邻的两个元素和等于接下来的元素。
# 直接递归吧。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        length = len(num)

        def rIsAdditiveNumber(ln, rn, index, flag):
            if flag and index == length:
                return True
            result = ln + rn
            resultString = str(result)
            if num[index:index + len(resultString)] == resultString:
                if rIsAdditiveNumber(rn, result, index + len(resultString),
                                     True):
                    return True

        for i in range(1, (length if num[0] != '0' else 2)):
            ln = int(num[:i])
            for j in range(i + 1, (length if num[i] != '0' else (i + 1)) + 1):
                rn = int(num[i:j])
                if rIsAdditiveNumber(ln, rn, j, False):
                    return True
        return False


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().isAdditiveNumber("000")))
    print('Example 1:')
    print('Input : ')
    print('"112358"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isAdditiveNumber("112358")))
    print()

    print('Example 2:')
    print('Input : ')
    print('"199100199"')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().isAdditiveNumber("199100199")))
    print()
    print(str(Solution().isAdditiveNumber("1991400199")))
    pass
# @lc main=end