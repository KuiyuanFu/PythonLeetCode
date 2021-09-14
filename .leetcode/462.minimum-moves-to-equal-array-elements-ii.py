# @lc app=leetcode id=462 lang=python3
#
# [462] Minimum Moves to Equal Array Elements II
#
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/
#
# algorithms
# Medium (55.80%)
# Likes:    1055
# Dislikes: 63
# Total Accepted:    74.7K
# Total Submissions: 133.8K
# Testcase Example:  '[1,2,3]'
#
# Given an integer array nums of size n, return the minimum number of moves
# required to make all array elements equal.
#
# In one move, you can increment or decrement an element of the array by 1.
#
# Test cases are designed so that the answer will fit in a 32-bit integer.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3]
# Output: 2
# Explanation:
# Only two moves are needed (remember each move increments or decrements one
# element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
#
#
# Example 2:
#
#
# Input: nums = [1,10,2,9]
# Output: 16
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
#
#

# @lc tags=math

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 最小移动次数，使所有元素相等。每次只能增减1.
# 找个中位值即可。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        midian = nums[len(nums) // 2]
        return sum([abs(n - midian) for n in nums])

        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,2,3]')
    print('Exception :')
    print('2')
    print('Output :')
    print(str(Solution().minMoves2([1, 2, 3])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,10,2,9]')
    print('Exception :')
    print('16')
    print('Output :')
    print(str(Solution().minMoves2([1, 10, 2, 9])))
    print()

    pass
# @lc main=end