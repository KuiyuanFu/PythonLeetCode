# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (59.45%)
# Likes:    5952
# Dislikes: 372
# Total Accepted:    930.3K
# Total Submissions: 1.6M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Given an integer array nums and an integer k, return the k^th largest element
# in the array.
#
# Note that it is the k^th largest element in the sorted order, not the k^th
# distinct element.
#
#
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#
#
# Constraints:
#
#
# 1 <= k <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
#
#
#

# @lc tags=divide-and-conquer;heap

# @lc imports=start
from heapq import heapify, heappushpop
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，返回第k大的元素。
# 直接用堆，优先队列。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        h = nums[:k]
        heapify(h)
        for i in range(k, len(nums)):
            if nums[i] > h[0]:
                heappushpop(h, nums[i])
        return h[0]
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('nums = [3,2,1,5,6,4], k = 2')
    print('Exception :')
    print('5')
    print('Output :')
    print(str(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)))
    print()

    print('Example 2:')
    print('Input : ')
    print('nums = [3,2,3,1,2,4,5,5,6], k = 4')
    print('Exception :')
    print('4')
    print('Output :')
    print(str(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)))
    print()

    pass
# @lc main=end