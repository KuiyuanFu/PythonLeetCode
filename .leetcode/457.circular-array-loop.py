# @lc app=leetcode id=457 lang=python3
#
# [457] Circular Array Loop
#
# https://leetcode.com/problems/circular-array-loop/description/
#
# algorithms
# Medium (30.85%)
# Likes:    191
# Dislikes: 152
# Total Accepted:    51K
# Total Submissions: 165.1K
# Testcase Example:  '[2,-1,1,2,2]'
#
# You are playing a game involving a circular array of non-zero integers nums.
# Each nums[i] denotes the number of indices forward/backward you must move if
# you are located at index i:
#
#
# If nums[i] is positive, move nums[i] steps forward, and
# If nums[i] is negative, move nums[i] steps backward.
#
#
# Since the array is circular, you may assume that moving forward from the last
# element puts you on the first element, and moving backwards from the first
# element puts you on the last element.
#
# A cycle in the array consists of a sequence of indices seq of length k
# where:
#
#
# Following the movement rules above results in the repeating index sequence
# seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
# Every nums[seq[j]] is either all positive or all negative.
# k > 1
#
#
# Return true if there is a cycle in nums, or false otherwise.
#
#
# Example 1:
#
#
# Input: nums = [2,-1,1,2,2]
# Output: true
# Explanation:
# There is a cycle from index 0 -> 2 -> 3 -> 0 -> ...
# The cycle's length is 3.
#
#
# Example 2:
#
#
# Input: nums = [-1,2]
# Output: false
# Explanation:
# The sequence from index 1 -> 1 -> 1 -> ... is not a cycle because the
# sequence's length is 1.
# By definition the sequence's length must be strictly greater than 1 to be a
# cycle.
#
#
# Example 3:
#
#
# Input: nums = [-2,1,-1,-2,-2]
# Output: false
# Explanation:
# The sequence from index 1 -> 2 -> 1 -> ... is not a cycle because nums[1] is
# positive, but nums[2] is negative.
# Every nums[seq[j]] must be either all positive or all negative.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5000
# -1000 <= nums[i] <= 1000
# nums[i] != 0
#
#
#
# Follow up: Could you solve it in O(n) time complexity and O(1) extra space
# complexity?
#
#

# @lc tags=array;two-pointers

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 数组位置上的数字就是移动的步数，之后判断是否可以回到原点。
# 先判断方向。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        length = len(nums)
        sf, sb = set(), set()
        for i, n in enumerate(nums):
            iNext = (i + n % length + length) % length
            if i == iNext:
                continue
            if n > 0:
                sf.add(i)
            else:
                sb.add(i)
            nums[i] = iNext
        for s in [sf, sb]:
            visited = set()
            i = -1
            while s:
                if i in visited:
                    return True
                if i not in s:
                    i = s.pop()
                    visited.clear()
                visited.add(i)
                i = nums[i]
        return False


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [2,-1,1,2,2]')
    print('Exception :')
    print('true')
    print('Output :')
    print(str(Solution().circularArrayLoop([2, -1, 1, 2, 2])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [-1,2]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().circularArrayLoop([-1, 2])))
    print()

    print('Example 3:')
    print('Input : ')
    print('nums = [-2,1,-1,-2,-2]')
    print('Exception :')
    print('false')
    print('Output :')
    print(str(Solution().circularArrayLoop([-2, 1, -1, -2, -2])))
    print(str(Solution().circularArrayLoop([2, -1, 1, -2, -2])))
    print(str(Solution().circularArrayLoop([1, 1, 2])))
    print()

    pass
# @lc main=end