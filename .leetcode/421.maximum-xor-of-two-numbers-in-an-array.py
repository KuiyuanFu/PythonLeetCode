# @lc app=leetcode id=421 lang=python3
#
# [421] Maximum XOR of Two Numbers in an Array
#
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
#
# algorithms
# Medium (54.96%)
# Likes:    2410
# Dislikes: 230
# Total Accepted:    88.6K
# Total Submissions: 161.3K
# Testcase Example:  '[3,10,5,25,2,8]'
#
# Given an integer array nums, return the maximum result of nums[i] XOR
# nums[j], where 0 <= i <= j < n.
#
#
# Example 1:
#
#
# Input: nums = [3,10,5,25,2,8]
# Output: 28
# Explanation: The maximum result is 5 XOR 25 = 28.
#
# Example 2:
#
#
# Input: nums = [0]
# Output: 0
#
#
# Example 3:
#
#
# Input: nums = [2,4]
# Output: 6
#
#
# Example 4:
#
#
# Input: nums = [8,10,2]
# Output: 10
#
#
# Example 5:
#
#
# Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
# Output: 127
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2 * 10^5
# 0 <= nums[i] <= 2^31 - 1
#
#
#

# @lc tags=bit-manipulation;trie

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 计算给定数组中两个数值异或的最大值。
# 从高位向地位遍历，每次增加一个位，当前最大值为前k位的最大值，使用mask提取每个数字的前k+1位，判断最大值后一位为1的情况是否能够满足，之后保存能达到的最大值。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        maximum = 0
        mask = 0
        for i in reversed(range(32)):
            mask |= (1 << i)
            t = maximum | (1 << i)
            s = set()
            for n in nums:
                s.add(n & mask)
            for n in s:
                if n ^ t in s:
                    maximum = t
                    break
        return maximum


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [3,10,5,25,2,8]')
    print('Exception :')
    print('28')
    print('Output :')
    print(str(Solution().findMaximumXOR([3, 10, 5, 25, 2, 8])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().findMaximumXOR([0])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [2,4]')
    print('Exception :')
    print('6')
    print('Output :')
    print(str(Solution().findMaximumXOR([2, 4])))
    print()

    print('Example 4:')
    print('Input : ')
    print('nums = [8,10,2]')
    print('Exception :')
    print('10')
    print('Output :')
    print(str(Solution().findMaximumXOR([8, 10, 2])))
    print()

    print('Example 5:')
    print('Input : ')
    print('nums = [14,70,53,83,49,91,36,80,92,51,66,70]')
    print('Exception :')
    print('127')
    print('Output :')
    print(
        str(Solution().findMaximumXOR(
            [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70])))
    print()

    pass
# @lc main=end