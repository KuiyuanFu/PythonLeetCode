# @lc app=leetcode id=470 lang=python3
#
# [470] Implement Rand10() Using Rand7()
#
# https://leetcode.com/problems/implement-rand10-using-rand7/description/
#
# algorithms
# Medium (46.25%)
# Likes:    762
# Dislikes: 253
# Total Accepted:    53.7K
# Total Submissions: 116.1K
# Testcase Example:  '1'
#
# Given the API rand7() that generates a uniform random integer in the range
# [1, 7], write a function rand10() that generates a uniform random integer in
# the range [1, 10]. You can only call the API rand7(), and you shouldn't call
# any other API. Please do not use a language's built-in random API.
#
# Each test case will have one internal argument n, the number of times that
# your implemented function rand10() will be called while testing. Note that
# this is not an argument passed to rand10().
#
# Follow up:
#
#
# What is the expected value for the number of calls to rand7() function?
# Could you minimize the number of calls to rand7()?
#
#
#
# Example 1:
# Input: n = 1
# Output: [2]
# Example 2:
# Input: n = 2
# Output: [2,8]
# Example 3:
# Input: n = 3
# Output: [3,8,10]
#
#
# Constraints:
#
#
# 1 <= n <= 10^5
#
#
#

# @lc tags=Unknown

# @lc imports=start
from imports import *
# @lc imports=end

# @lc idea=start
#
# 通过1-7的随机数生成器，实现一个1-10的随机数生成器。
# 目的是，每一个数字的概率相等。
# 将10映射到7*7的矩阵中，重复3次，占用30格，随机两次为横纵坐标，若为其余位置重新赋值。
#
# @lc idea=end

# @lc group=

# @lc rank=


def rand7():
    return 1


# @lc code=start
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


class Solution:
    def rand10(self):
        # 1234 5
        # 6789 10
        while True:
            i, j = rand7() - 1, rand7() - 1
            if i >= 6 or j >= 5:
                continue
            i = i % 2
            return i * 5 + j + 1
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('n = 1')
    print('Exception :')
    print('[2]')
    print('Output :')
    print(str(Solution().rand10()))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('[2,8]')
    print('Output :')
    print(str(Solution().rand10()))
    print()

    print('Example 3:')
    print('Input : ')
    print('n = 3')
    print('Exception :')
    print('[3,8,10]')
    print('Output :')
    print(str(Solution().rand10()))
    print()

    pass
# @lc main=end