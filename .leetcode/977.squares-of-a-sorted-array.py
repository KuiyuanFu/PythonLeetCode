# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#
# https://leetcode.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (71.86%)
# Likes:    6382
# Dislikes: 163
# Total Accepted:    1.2M
# Total Submissions: 1.6M
# Testcase Example:  '[-4,-1,0,3,10]'
#
# Given an integer array nums sorted in non-decreasing order, return an array
# of the squares of each number sorted in non-decreasing order.
#
#
# Example 1:
#
#
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
#
#
# Example 2:
#
#
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in non-decreasing order.
#
#
#
# Follow up: Squaring each element and sorting the new array is very trivial,
# could you find an O(n) solution using a different approach?
#

# @lc tags=dynamic-programming

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定一个递增数组，求每个元素平方后的有序数组。
# 从0开始，向两侧遍历。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        r = bisect_right(nums, 0)
        l = r - 1
        length = len(nums)
        while True:
            f1, f2 = l == -1, r == length

            if not f1 and not f2:
                q1, q2 = nums[l]**2, nums[r]**2
                if q1 <= q2:
                    res.append(q1)
                    l -= 1
                else:
                    res.append(nums[r]**2)
                    r += 1
            elif f1 and not f2:
                res.append(nums[r]**2)
                r += 1
            elif not f1 and f2:
                res.append(nums[l]**2)
                l -= 1
            elif f1 and f2:
                return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [-4,-1,0,3,10]')
    print('Exception :')
    print('[0,1,9,16,100]')
    print('Output :')
    print(str(Solution().sortedSquares([-4, -1, 0, 3, 10])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [-7,-3,2,3,11]')
    print('Exception :')
    print('[4,9,9,49,121]')
    print('Output :')
    print(str(Solution().sortedSquares([-7, -3, 2, 3, 11])))
    print()

    pass
# @lc main=end