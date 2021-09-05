# @lc app=leetcode id=453 lang=python3
#
# [453] Minimum Moves to Equal Array Elements
#
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/
#
# algorithms
# Easy (52.11%)
# Likes:    1024
# Dislikes: 1367
# Total Accepted:    102.9K
# Total Submissions: 197.4K
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of size n, return the minimum number of moves
# required to make all array elements equal.
#
# In one move, you can increment n - 1 elements of the array by 1.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: 3
# Explanation: Only three moves are needed (remember each move increments two
# elements):
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
#
#
# Example 2:
#
#
# Input: nums = [1,1,1]
# Output: 0
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# The answer is guaranteed to fit in a 32-bit integer.
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，每一次提高1在n-1个元素上，问多少次使所有元素相同。
# 等价于将一个降低1。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = min(nums)
        return sum([n - m for n in nums])
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3]')
    print('Exception :')
    print('3')
    print('Output :')
    print(str(Solution().minMoves([1, 2, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,1,1]')
    print('Exception :')
    print('0')
    print('Output :')
    print(str(Solution().minMoves([1, 1, 1])))
    print()

    pass
# @lc main=end