# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#
# https://leetcode.com/problems/single-number-iii/description/
#
# algorithms
# Medium (65.53%)
# Likes:    2455
# Dislikes: 136
# Total Accepted:    196.2K
# Total Submissions: 299.2K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# Given an integer array nums, in which exactly two elements appear only once
# and all the other elements appear exactly twice. Find the two elements that
# appear only once. You can return the answer in any order.
#
# You must write an algorithm that runs in linear runtime complexity and uses
# only constant extra space.
#
#
# Example 1:
#
#
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
#
#
# Example 2:
#
#
# Input: nums = [-1,0]
# Output: [-1,0]
#
#
# Example 3:
#
#
# Input: nums = [0,1]
# Output: [1,0]
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 3 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# Each integer in nums will appear twice, only two integers will appear once.
#
#
#

# @lc tags=bit-manipulation

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一组数字，其中之后两个数字出现一次，其他出现两次，找到这两个数。
# 直接异或，可以得到这两个数字的异或值，但怎么分离出来呢？
# 首先得到的值，是两个值的异或，也就是说，相同的位为0，不同的为1，那么就可以个根据一个不同的位，来将所有输入分成两组，分别异或，得到两个值，就是结果。
# 使用 total = total & -total 的方式，找到一个不同的位，取负数，就是补码，取反加一，将表示相同的位的0变成了1，之后再加1，就进位到了第一个0的位置，也就是说得到一个标志位，区分两个数。
#
# @lc idea=end

# @lc group=bit-manipulation

# @lc rank=10


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        total = 0
        for n in nums:
            total ^= n
        total = total & -total
        ret = [0, 0]
        for n in nums:
            if n & total == 0:
                ret[0] ^= n
            else:
                ret[1] ^= n
        return ret
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,1,3,2,5]')
    print('Exception :')
    print('[3,5]')
    print('Output :')
    print(str(Solution().singleNumber([1, 2, 1, 3, 2, 5])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [-1,0]')
    print('Exception :')
    print('[-1,0]')
    print('Output :')
    print(str(Solution().singleNumber([-1, 0])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [0,1]')
    print('Exception :')
    print('[1,0]')
    print('Output :')
    print(str(Solution().singleNumber([0, 1])))
    print()

    pass
# @lc main=end