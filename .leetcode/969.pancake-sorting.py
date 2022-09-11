# @lc app=leetcode id=969 lang=python3
#
# [969] Pancake Sorting
#
# https://leetcode.com/problems/pancake-sorting/description/
#
# algorithms
# Medium (69.94%)
# Likes:    1183
# Dislikes: 1303
# Total Accepted:    77.9K
# Total Submissions: 111.3K
# Testcase Example:  '[3,2,4,1]'
#
# Given an array of integers arr, sort the array by performing a series of
# pancake flips.
#
# In one pancake flip we do the following steps:
#
#
# Choose an integer k where 1 <= k <= arr.length.
# Reverse the sub-array arr[0...k-1] (0-indexed).
#
#
# For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k =
# 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake
# flip at k = 3.
#
# Return an array of the k-values corresponding to a sequence of pancake flips
# that sort arr. Any valid answer that sorts the array within 10 * arr.length
# flips will be judged as correct.
#
#
# Example 1:
#
#
# Input: arr = [3,2,4,1]
# Output: [4,2,4,3]
# Explanation:
# We perform 4 pancake flips, with k values 4, 2, 4, and 3.
# Starting state: arr = [3, 2, 4, 1]
# After 1st flip (k = 4): arr = [1, 4, 2, 3]
# After 2nd flip (k = 2): arr = [4, 1, 2, 3]
# After 3rd flip (k = 4): arr = [3, 2, 1, 4]
# After 4th flip (k = 3): arr = [1, 2, 3, 4], which is sorted.
#
#
# Example 2:
#
#
# Input: arr = [1,2,3]
# Output: []
# Explanation: The input is already sorted, so there is no need to flip
# anything.
# Note that other answers, such as [3, 3], would also be accepted.
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 100
# 1 <= arr[i] <= arr.length
# All integers in arr are unique (i.e. arr is a permutation of the integers
# from 1 to arr.length).
#
#
#

# @lc tags=queue

# @lc imports=start
from imports import *

# @lc imports=end

# @lc idea=start
#
# 给定数组，每次指定k，翻转0到k-1的元素，使最后有序，返回一个可能的k序列。
# 每次把当前最大元素放在第一个，之后在翻转到排序位置。
#
# @lc idea=end

# @lc group=

# @lc rank=


# @lc code=start
class Solution:

    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        nums = arr.copy()
        nums.sort(reverse=True)
        length = len(arr)
        for i, n in enumerate(nums):
            if arr[-1 - i] == n:
                continue
            idx = arr.index(n)
            res.append(idx + 1)
            arr[:idx + 1] = reversed(arr[:idx + 1])
            res.append(length - i)
            arr[:length - i] = reversed(arr[:length - i])
        print(arr)
        return res
        pass


# @lc code=end

# @lc main=start
if __name__ == '__main__':
    print('Example 1:')
    print('Input : ')
    print('arr = [3,2,4,1]')
    print('Exception :')
    print('[4,2,4,3]')
    print('Output :')
    print(str(Solution().pancakeSort([3, 2, 4, 1])))
    print()

    print('Example 2:')
    print('Input : ')
    print('arr = [1,2,3]')
    print('Exception :')
    print('[]')
    print('Output :')
    print(str(Solution().pancakeSort([1, 2, 3])))
    print()

    pass
# @lc main=end