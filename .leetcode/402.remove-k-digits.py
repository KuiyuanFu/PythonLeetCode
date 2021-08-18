# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#
# https://leetcode.com/problems/remove-k-digits/description/
#
# algorithms
# Medium (28.78%)
# Likes:    3769
# Dislikes: 160
# Total Accepted:    192.9K
# Total Submissions: 669.1K
# Testcase Example:  '"1432219"\n3'
#
# Given string num representing a non-negative integer num, and an integer k,
# return the smallest possible integer after removing k digits from num.
#
#
# Example 1:
#
#
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219
# which is the smallest.
#
#
# Example 2:
#
#
# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output
# must not contain leading zeroes.
#
#
# Example 3:
#
#
# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with
# nothing which is 0.
#
#
#
# Constraints:
#
#
# 1 <= k <= num.length <= 10^5
# num consists of only digits.
# num does not have any leading zeros except for the zero itself.
#
#
#

# @lc tags=stack;greedy

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将一个整数移除k位，求最大值。
# 判断相邻两个值的大小关系。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return '0'
        if '0' in num:
            zidx = num.index('0')
            if k >= zidx:
                return self.removeKdigits(num[zidx + 1:], k - zidx)

        stack = []
        n = 0
        for c in num:
            while n < k and stack and stack[-1] > c:
                stack.pop()
                n += 1

            stack.append(c)

        res = ''.join(stack[:len(num) - k])
        return res if res else '0'


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print(str(Solution().removeKdigits("212", 1)))
    print('Example 1:')
    print('Input : ')
    print('num = "1432219", k = 3')
    print('Exception :')
    print('"1219"')
    print('Output :')
    print(str(Solution().removeKdigits("1432219", 3)))
    print()

    print('Example 2:')
    print('Input : ')
    print('num = "10200", k = 1')
    print('Exception :')
    print('"200"')
    print('Output :')
    print(str(Solution().removeKdigits("10200", 1)))
    print()

    print('Example 3:')
    print('Input : ')
    print('num = "10", k = 2')
    print('Exception :')
    print('"0"')
    print('Output :')
    print(str(Solution().removeKdigits("10", 2)))
    print()

    pass
# @lc main=end