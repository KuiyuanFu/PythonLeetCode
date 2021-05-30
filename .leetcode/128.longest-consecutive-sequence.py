# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (46.59%)
# Likes:    5247
# Dislikes: 258
# Total Accepted:    411.5K
# Total Submissions: 878.2K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#
# Example 1:
#
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
#
#
# Example 2:
#
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
#
#

# @lc tags=array;union-find

# @lc imports=start

from re import L
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一系列数字，求连续数字最长长度。
# 如果要 On ，那就只能用set，但在python 中没有排序快，因为排序是c写的。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        recards = {}
        for n in nums:
            recards.update({n: 0})
        lengthMax = 0
        for n in list(recards.keys()):

            length = recards[n]
            if length != 0:
                continue
            length = 1
            t = n - 1
            while True:
                l = recards.get(t, -1)
                if l > 0:
                    length += l
                    break
                elif l == 0:
                    length += 1
                    recards[t] = -1
                else:
                    break
                t -= 1
            recards[n] = length
            lengthMax = max(lengthMax, length)
        return lengthMax
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [100,4,200,1,3,2]')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().longestConsecutive([100, 4, 200, 1, 3, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [0,3,7,2,5,8,4,6,0,1]')
    print('Exception :')
    print('9')
    print('Output :')
    print(str(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])))
    print()

    pass
# @lc main=end