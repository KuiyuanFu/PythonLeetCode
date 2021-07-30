# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Easy (71.29%)
# Likes:    4498
# Dislikes: 231
# Total Accepted:    392K
# Total Submissions: 549.6K
# Testcase Example:  '2'
#
# Given an integer n, return an array ans of length n + 1 such that for each i
# (0 <= i <= n), ans[i] is the number of 1's in the binary representation of
# i.
#
#
# Example 1:
#
#
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
#
#
# Example 2:
#
#
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
#
#
#
# Constraints:
#
#
# 0 <= n <= 10^5
#
#
#
# Follow up:
#
#
# It is very easy to come up with a solution with a runtime of O(n log n). Can
# you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like
# __builtin_popcount in C++)?
#
#
#

# @lc tags=dynamic-programming;bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个整数，求0-n每个数字的二进制表示中的1的个数。
# 直接模拟累加器。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        legnth = 32
        numFlag = [False] * legnth
        times = 0
        result = [0] * (n + 1)
        for i in range(1, n + 1):
            t = True
            for j in range(legnth):
                if not t:
                    break
                if numFlag[j]:
                    times -= 1
                else:
                    t = not t
                    times += 1
                numFlag[j] = not numFlag[j]
            result[i] = times
        return result
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':

    print('Example 1:')
    print('Input : ')
    print('n = 85723')
    print('Output :')
    print(str(Solution().countBits(2)))
    print()

    print('Example 1:')
    print('Input : ')
    print('n = 2')
    print('Exception :')
    print('[0,1,1]')
    print('Output :')
    print(str(Solution().countBits(2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('n = 5')
    print('Exception :')
    print('[0,1,1,2,1,2]')
    print('Output :')
    print(str(Solution().countBits(5)))
    print()

    pass
# @lc main=end