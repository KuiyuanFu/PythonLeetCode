# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#
# https://leetcode.com/problems/wiggle-sort-ii/description/
#
# algorithms
# Medium (31.15%)
# Likes:    1557
# Dislikes: 700
# Total Accepted:    103.7K
# Total Submissions: 332.8K
# Testcase Example:  '[1,5,1,1,6,4]'
#
# Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2]
# < nums[3]....
#
# You may assume the input array always has a valid answer.
#
#
# Example 1:
#
#
# Input: nums = [1,5,1,1,6,4]
# Output: [1,6,1,5,1,4]
# Explanation: [1,4,1,5,1,6] is also accepted.
#
#
# Example 2:
#
#
# Input: nums = [1,3,2,2,3,1]
# Output: [2,3,1,3,1,2]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5 * 10^4
# 0 <= nums[i] <= 5000
# It is guaranteed that there will be an answer for the given input nums.
#
#
#
# Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?
#

# @lc tags=sort

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 将一系列的数字排列成一低一高交替的顺序，即n[0]<n[1]>n[2]<n[3]。
# 朴素思想是，排序后排列。
# 比较快的是，找中位数，之后排列。
#
# @lc idea=end

# @lc group=

# @lc rank=

# @lc code=start
import random


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        def nsmallest(nums, n):
            start, end = 0, len(nums) - 1
            while True:
                pivot = nums[random.randint(start, end)]
                i, j, k = start, end, start
                while k <= j:
                    if nums[k] < pivot:
                        nums[i], nums[k] = nums[k], nums[i]
                        i += 1
                        k += 1
                    elif nums[k] > pivot:
                        nums[j], nums[k] = nums[k], nums[j]
                        j -= 1
                    else:
                        k += 1
                if i <= n - 1 <= j:
                    return pivot
                elif n - 1 < i:
                    end = i - 1
                else:
                    start = i + 1

        n = len(nums)
        mid = nsmallest(nums, (n + 1) // 2)
        mapIdx = lambda i: (1 + 2 * i) % (n | 1)
        i, j, k = 0, n - 1, 0
        while k <= j:
            if nums[mapIdx(k)] > mid:
                nums[mapIdx(k)], nums[mapIdx(i)] = nums[mapIdx(i)], nums[
                    mapIdx(k)]
                i += 1
                k += 1
            elif nums[mapIdx(k)] < mid:
                nums[mapIdx(k)], nums[mapIdx(j)] = nums[mapIdx(j)], nums[
                    mapIdx(k)]
                j -= 1
            else:
                k += 1
        return nums


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [1,5,1,1,6,4]')
    print('Exception :')
    print('[1,6,1,5,1,4]')
    print('Output :')
    print(str(Solution().wiggleSort([1, 5, 1, 1, 6, 4])))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [1,3,2,2,3,1]')
    print('Exception :')
    print('[2,3,1,3,1,2]')
    print('Output :')
    print(str(Solution().wiggleSort([1, 3, 2, 2, 3, 1])))
    print()

    pass
# @lc main=end