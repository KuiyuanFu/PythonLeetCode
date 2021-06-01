# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#
# https://leetcode.com/problems/single-number-ii/description/
#
# algorithms
# Medium (54.44%)
# Likes:    2645
# Dislikes: 405
# Total Accepted:    290.2K
# Total Submissions: 533.1K
# Testcase Example:  '[2,2,3,2]'
#
# Given an integer array nums where every element appears three times except

# for one, which appears exactly once. Find the single element and return it.
#
# You must implement a solution with a linear runtime complexity and use only
# constant extra space.
#
#
# Example 1:
# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:
# Input: nums = [0,1,0,1,0,1,99]
# Output: 99
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# Each element in nums appears exactly three times except for one element which
# appears once.
#
#
#

# @lc tags=bit-manipulation

# @lc imports=start
from pyexpat.errors import XML_ERROR_ENTITY_DECLARED_IN_PE
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个数字数组，只有一个数字出现一次，其他出现三次，找到这个。
# 复杂一点的描述就是，只有一个数字出现p次，而其他出现k次，找到特殊的这个。
# ---
# 考虑每一位，除了特殊的那一个，其他的每一个出现k次，那么这些数字的和在此位一定是k的整数倍，那么就手动实现一个二进制计数器，一旦这个计数器到达k，就置为0，这样就会只剩下出现p次的特殊数字，可以利用p的二进制内容来选择二进制计数器中的位。
# 直接使用整形，来同时计算所有位。
# ---
# 具体实现：
# 1。首先设计计数器x，需要m个，满足 2^m >= k。记输入数字为n，那么:
# x[1] = x[1] ^ n
# x[2] = x[2] ^ (x[1] & n)
# x[m] = x[m] ^ (x[m-1] & ...  & x[1] & n),
# 其中右侧的值，是上一次的值，所以需要从后向前计算，或者使用一块空间存储之前的值。
# 2. 检测溢出，并重置
# 考虑k 的二进制表示，也就对应了计数器中的每一位，如果都匹配，就达到了k，可以将其置为0.
#
#
# @lc idea=end

# @lc group=bit-manipulation

# @lc rank=10


# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        k = 3
        # p = 1

        # compute m satisfy 2 ^m >= k
        m = 0
        kt = k
        while kt:
            kt = kt // 2
            m += 1

        # set flag, when the flag[i] is 1, mean x[i] need to be 1 for reach k
        maskFlag = [0] * m
        kt = k
        for i in range(m):
            maskFlag[i] = kt % 2
            kt = kt // 2

        x = [0] * m
        for n in nums:
            xOld = x
            x = [0] * m
            # accumulate
            for i in range(m):
                x[i] = xOld[i] ^ n
                n = n & xOld[i]
            # test flag, to mask some index
            mask = ~0
            for i in range(m):
                mask = mask & (x[i] if maskFlag[i] == 1 else ~x[i])
            # if reach k, then set it to 0.
            mask = ~mask

            for i in range(m):
                x[i] = x[i] & mask
        result = 0
        for n in x:
            result = result | n
        return result

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,2,3,2]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().singleNumber([2, 2, 3, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0,1,0,1,0,1,99]')
    print('Exception :')
    print('99')
    print('Output :')
    print(str(Solution().singleNumber([0, 1, 0, 1, 0, 1, 99])))
    print()

    pass
# @lc main=end