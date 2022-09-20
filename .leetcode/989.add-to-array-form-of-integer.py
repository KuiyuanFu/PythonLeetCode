# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#
# https://leetcode.com/problems/add-to-array-form-of-integer/description/
#
# algorithms
# Easy (45.51%)
# Likes:    1521
# Dislikes: 161
# Total Accepted:    128.3K
# Total Submissions: 281.9K
# Testcase Example:  '[1,2,0,0]\n34'
#
# The array-form of an integer num is an array representing its digits in left
# to right order.
#
#
# For example, for num = 1321, the array form is [1,3,2,1].
#
#
# Given num, the array-form of an integer, and an integer k, return the
# array-form of the integer num + k.
#
#
# Example 1:
#
#
# Input: num = [1,2,0,0], k = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234
#
#
# Example 2:
#
#
# Input: num = [2,7,4], k = 181
# Output: [4,5,5]
# Explanation: 274 + 181 = 455
#
#
# Example 3:
#
#
# Input: num = [2,1,5], k = 806
# Output: [1,0,2,1]
# Explanation: 215 + 806 = 1021
#
#
#
# Constraints:
#
#
# 1 <= num.length <= 10^4
# 0 <= num[i] <= 9
# num does not contain any leading zeros except for the zero itself.
# 1 <= k <= 10^4
#
#
#

# @lc tags=math;union-find

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 用数组表示的数字，相加
# 相加进位
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def addToArrayForm(self, num1: List[int], k: int) -> List[int]:

        num2 = [int(c) for c in str(k)]
        num1.reverse()
        num2.reverse()
        res = []
        r = 0
        l1, l2 = len(num1), len(num2)
        for i in range(max(l1, l2) + 1):
            n = r + (num1[i] if i < l1 else 0) + (num2[i] if i < l2 else 0)
            r, m = divmod(n, 10)
            res.append(m)
        while res[-1] == 0:
            res.pop()
        res.reverse()
        return res


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('num = [9,9,9,9,9,9,9,9,9,9], k = 1')
    print('Exception :')
    print('[1,0,0,0,0,0,0,0,0,0,0]')
    print('Output :')
    print(str(Solution().addToArrayForm([9, 9, 9, 9, 9, 9, 9, 9, 9, 9], 1)))
    print()
    print('Example 1:')
    print('Input : ')
    print('num = [1,2,0,0], k = 34')
    print('Exception :')
    print('[1,2,3,4]')
    print('Output :')
    print(str(Solution().addToArrayForm([1, 2, 0, 0], 34)))
    print()

    print('Example 2:')
    print('Input : ')
    print('num = [2,7,4], k = 181')
    print('Exception :')
    print('[4,5,5]')
    print('Output :')
    print(str(Solution().addToArrayForm([2, 7, 4], 181)))
    print()

    print('Example 3:')
    print('Input : ')
    print('num = [2,1,5], k = 806')
    print('Exception :')
    print('[1,0,2,1]')
    print('Output :')
    print(str(Solution().addToArrayForm([2, 1, 5], 806)))
    print()

    pass
# @lc main=end